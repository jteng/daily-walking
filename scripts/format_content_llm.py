#!/usr/bin/env python3
"""
LLM-powered content formatter using Ollama.
Provides smarter, context-aware formatting decisions.
"""

import json
import requests
import argparse
from pathlib import Path
from typing import Optional


OLLAMA_API_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "qwen2.5:1.5b"

FORMATTING_PROMPT = """你是一个专业的中文内容格式化助手。请将以下灵修内容格式化为HTML片段，使其更易读。

重要规则：
1. 只输出HTML片段，不要包含<!DOCTYPE>、<html>、<head>、<body>等标签
2. 在主题转换处添加段落分隔（使用<p>标签包裹每个段落）
3. 将引用的话（用「」或『』标记的内容）用<blockquote>标签包裹
4. 将多个相关问题组织成项目列表（使用<ul>和<li>标签）
5. 将章节标题或重点（以：结尾的文本）加粗（使用<strong>标签）
6. 保持原有的表格和HTML结构不变
7. 绝对不要插入任何指向外部网站的超链接（<a>标签）
8. 如果原文中存在以「注释：」开头的内容，将其包裹在 <div class="commentary-box"> 中，并在内部使用 <h5>注释</h5> 作为标题，内容若有列表则使用 <ol> 或 <ul>。并且务必将此部分（整个div）移动到所有内容的最后面。注意：只格式化原文中已有的注释内容，不要创建新的注释。
9. 在表格中，不要添加<br>标签，不要在中文字符之间添加空格
10. 保持表格单元格内容紧凑，不要添加换行符

原始内容：
{content}

请直接输出格式化后的HTML片段，不要添加任何解释、说明或额外的HTML结构。"""


def check_ollama_running() -> bool:
    """Check if Ollama service is running."""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        return response.status_code == 200
    except:
        return False


def format_content_heuristic(content: str) -> Optional[str]:
    """
    Simple heuristic formatting as fallback when LLM fails.
    Adds basic paragraph breaks and structure.
    """
    # Skip if already formatted
    if '<p>' in content or '<ul>' in content:
        return None
    
    # Skip very short content
    if len(content) < 200:
        return None
    
    # Split into sentences and group into paragraphs
    sentences = content.split('。')
    paragraphs = []
    current_para = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        
        # Skip if has HTML tags
        if '<' in sentence and '>' in sentence:
            if current_para:
                paragraphs.append('。'.join(current_para) + '。')
                current_para = []
            paragraphs.append(sentence)
            continue
        
        current_para.append(sentence)
        
        # Create paragraph after 2-3 sentences
        if len(current_para) >= 2:
            paragraphs.append('。'.join(current_para) + '。')
            current_para = []
    
    # Add remaining
    if current_para:
        paragraphs.append('。'.join(current_para) + '。')
    
    # Wrap in <p> tags
    formatted_paragraphs = []
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if para.startswith('<'):
            formatted_paragraphs.append(para)
        else:
            formatted_paragraphs.append(f'<p>{para}</p>')
    
    return '\n\n'.join(formatted_paragraphs)


def format_with_llm(content: str, model: str = DEFAULT_MODEL, force: bool = False) -> Optional[str]:
    """
    Format content using local LLM via Ollama.
    
    Args:
        content: Original content to format
        model: Ollama model name
        force: Force formatting even if already formatted
    
    Returns:
        Formatted content or None if failed
    """
    # Skip if already formatted (unless forced)
    if not force and ('<p>' in content or '<ul>' in content):
        return None
    
    # Skip very short content
    if len(content) < 200:
        return None
    
    prompt = FORMATTING_PROMPT.format(content=content)
    
    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,  # Lower temperature for more consistent formatting
                    "top_p": 0.9,
                }
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            formatted = result.get('response', '').strip()
            
            # Clean up the response
            # Remove markdown code blocks if present
            if formatted.startswith('```html'):
                formatted = formatted[7:]  # Remove ```html
            if formatted.startswith('```'):
                formatted = formatted[3:]  # Remove ```
            if formatted.endswith('```'):
                formatted = formatted[:-3]  # Remove trailing ```
            formatted = formatted.strip()
            
            # Remove unwanted HTML wrapper tags
            # The LLM sometimes returns full HTML documents despite instructions
            import re
            
            # Remove DOCTYPE
            formatted = re.sub(r'<!DOCTYPE[^>]*>', '', formatted, flags=re.IGNORECASE)
            
            # Extract content from <body> if present
            body_match = re.search(r'<body[^>]*>(.*)</body>', formatted, re.DOTALL | re.IGNORECASE)
            if body_match:
                formatted = body_match.group(1).strip()
            
            # Remove <html>, <head>, and their closing tags
            formatted = re.sub(r'</?html[^>]*>', '', formatted, flags=re.IGNORECASE)
            formatted = re.sub(r'<head>.*?</head>', '', formatted, flags=re.DOTALL | re.IGNORECASE)
            
            # Clean up extra whitespace
            formatted = formatted.strip()
            
            # Validate we got actual HTML content
            if not formatted or len(formatted) < 50:
                print("Warning: LLM didn't return formatted HTML (too short or empty)")
                return None
            
            # Check if it's actually formatted (has HTML tags)
            if '<' not in formatted or '>' not in formatted:
                print("Warning: LLM response doesn't contain HTML tags")
                return None
            
            return formatted
        else:
            print(f"Error: Ollama API returned {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error formatting with LLM: {e}")
        return None


def format_single_entry(entry: dict, model: str = DEFAULT_MODEL, force: bool = False) -> bool:
    """
    Format a single entry using LLM.
    
    Args:
        entry: Entry dict with 'content' field
        model: Ollama model name
        force: Force formatting even if already formatted
    
    Returns:
        True if formatted, False if skipped
    """
    original = entry['content']
    formatted = format_with_llm(original, model, force=force)
    
    if formatted and formatted != original:
        entry['content'] = formatted
        return True
    return False


def test_formatting(json_path: Path, model: str = DEFAULT_MODEL):
    """Test formatting on a single entry."""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Test on Week 1 Day 1
    test_entry = data[0]
    print(f"Testing on: {test_entry['day_label']} - {test_entry['title']}")
    print(f"\nOriginal content (first 200 chars):")
    print(test_entry['content'][:200])
    print("\n" + "="*80)
    
    formatted = format_with_llm(test_entry['content'], model)
    
    if formatted:
        print(f"\nFormatted content (first 400 chars):")
        print(formatted[:400])
        print("\n" + "="*80)
        print("\n✓ Formatting successful!")
        print(f"Original length: {len(test_entry['content'])}")
        print(f"Formatted length: {len(formatted)}")
    else:
        print("\n✗ Formatting failed or content already formatted")


import time

def format_all_entries(json_path: Path, model: str = DEFAULT_MODEL, indices: Optional[list] = None, limit: Optional[int] = None, force: bool = False):
    """Format entries in bibleData.json with retry and fallback."""
    # Load data
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    target_indices = []
    if indices:
        target_indices = indices
    else:
        # If no specific indices, use all (subjest to limit)
        target_indices = list(range(len(data)))
        
    if limit:
        target_indices = target_indices[:limit]
        
    print(f"Formatting {len(target_indices)} entries with {model} (force={force})...")
    
    formatted_count = 0
    skipped_count = 0
    failed_indices = []  # Track failed entries for retry
    
    start_time = time.time()
    
    # First pass
    for i in target_indices:
        entry = data[i]
        try:
            entry_start = time.time()
            if format_single_entry(entry, model, force=force):
                elapsed = time.time() - entry_start
                formatted_count += 1
                print(f"✓ [{i+1}/{len(data)}] {entry['day_label']}: Formatted ({elapsed:.2f}s)")
            else:
                elapsed = time.time() - entry_start
                skipped_count += 1
                print(f"  [{i+1}/{len(data)}] {entry['day_label']}: Skipped ({elapsed:.2f}s)")
        except Exception as e:
            failed_indices.append(i)
            print(f"⚠ [{i+1}/{len(data)}] {entry['day_label']}: Failed (will retry)")


    
    # Save progress coverage
    # Note: We are saving the WHOLE data list, but only modified specific entries
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # Retry failed (only those in our target set)
    if failed_indices:
        print(f"\n🔄 Retrying {len(failed_indices)} failed entries...")
        retry_failed = []
        
        for i in failed_indices:
            entry = data[i]
            try:
                if format_single_entry(entry, model):
                    formatted_count += 1
                    print(f"✓ [{i+1}/{len(data)}] {entry['day_label']}: Formatted (retry)")
                else:
                    retry_failed.append(i)
            except Exception as e:
                retry_failed.append(i)
                print(f"⚠ [{i+1}/{len(data)}] {entry['day_label']}: Failed again")
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        if retry_failed:
             print(f"\n🔧 Using heuristic fallback for {len(retry_failed)} entries...")
             for i in retry_failed:
                 entry = data[i]
                 try:
                     formatted = format_content_heuristic(entry['content'])
                     if formatted:
                         entry['content'] = formatted
                         formatted_count += 1
                         print(f"✓ [{i+1}/{len(data)}] {entry['day_label']}: Formatted (heuristic)")
                     else:
                         print(f"✗ [{i+1}/{len(data)}] {entry['day_label']}: Heuristic failed")
                 except Exception as e:
                     print(f"✗ [{i+1}/{len(data)}] {entry['day_label']}: Error - {e}")
             
             with open(json_path, 'w', encoding='utf-8') as f:
                 json.dump(data, f, ensure_ascii=False, indent=2)

    total_time = time.time() - start_time
    print(f"\n✅ Done in {total_time:.2f}s!")
    print(f"  Targeted: {len(target_indices)}")
    print(f"  Formatted: {formatted_count}")
    print(f"  Skipped: {skipped_count}")
    print(f"  Avg time/entry: {total_time/len(target_indices) if target_indices else 0:.2f}s")


def main():
    parser = argparse.ArgumentParser(description='Format content using local LLM')
    parser.add_argument('--test', action='store_true', help='Test on a single entry')
    parser.add_argument('--all', action='store_true', help='Format all entries')
    parser.add_argument('--indices', type=str, help='Comma-separated list of indices (e.g. 0,1,2)')
    parser.add_argument('--limit', type=int, help='Limit number of entries')
    parser.add_argument('--model', default=DEFAULT_MODEL, help='Ollama model to use')
    parser.add_argument('--force', action='store_true', help='Force re-formatting')
    args = parser.parse_args()
    
    # Check if Ollama is running
    # if not check_ollama_running(): ... (Keep existing check if needed, or skip for speed if confident)
    
    json_path = Path('bibleData.json')
    if not json_path.exists():
        print(f"Error: {json_path} not found")
        return
    
    if args.test:
        test_formatting(json_path, args.model)
    elif args.indices:
        indices = [int(x.strip()) for x in args.indices.split(',')]
        format_all_entries(json_path, args.model, indices=indices, limit=args.limit, force=args.force)
    elif args.all:
        confirm = input(f"This will format all entries using {args.model}. Continue? (y/n): ")
        if confirm.lower() == 'y':
            format_all_entries(json_path, args.model, limit=args.limit, force=args.force)
    else:
        # Default behavior or help
        print("Please specify --test, --all, or --indices")

if __name__ == '__main__':
    main()

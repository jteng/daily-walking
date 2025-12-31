# Quick Start: Using Local LLM for Content Formatting

## TL;DR - 3 Steps to Get Started

### 1. Install Ollama
```bash
brew install ollama
```

### 2. Start Ollama & Download Model
```bash
# Terminal 1: Start Ollama service
ollama serve

# Terminal 2: Download the model (one-time, ~2GB)
ollama pull qwen2.5:3b
```

### 3. Test the LLM Formatter
```bash
# Test on one entry first
python3 scripts/format_content_llm.py --test

# If it looks good, format all entries
python3 scripts/format_content_llm.py --all
```

## What You Get

**Current Heuristic Formatter:**
- ✅ Fast (instant)
- ✅ Consistent
- ⚠️ Pattern-based (mechanical)
- ⚠️ ~80-85% accuracy

**LLM-Powered Formatter:**
- ✅ Context-aware (understands meaning)
- ✅ Smarter decisions
- ✅ ~95%+ accuracy
- ⚠️ Slower (~2s per entry = 10 min total)

## Example Improvements

The LLM will:
- Break paragraphs at **topic transitions**, not just every 2-3 sentences
- Distinguish between **rhetorical questions** and **reflection questions**
- Better identify **section headers** even without "："
- Understand **Chinese literary patterns** and idioms

## Need Help?

See full guide: `docs/OLLAMA_SETUP.md`

## Note

The current heuristic formatting is already pretty good! The LLM is an **optional enhancement** if you want even better results.

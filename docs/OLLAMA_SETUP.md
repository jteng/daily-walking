# Setting Up Local LLM with Ollama

This guide will help you install and use Ollama to run local LLMs for better content formatting.

## Step 1: Install Ollama

### Option A: Using Homebrew (Recommended)
```bash
brew install ollama
```

### Option B: Download from Website
1. Visit https://ollama.ai
2. Download the macOS installer
3. Run the installer

## Step 2: Start Ollama Service

```bash
# Start Ollama in the background
ollama serve
```

Leave this running in a terminal window.

## Step 3: Download a Model

Open a new terminal and run:

```bash
# Download a small, fast model (recommended for this task)
ollama pull qwen2.5:3b

# OR download a larger, more capable model (if you have 16GB+ RAM)
ollama pull qwen2.5:7b
```

**Why Qwen2.5?**
- Excellent Chinese language understanding
- Fast inference
- Good at following formatting instructions
- 3b model: ~2GB, runs on most Macs
- 7b model: ~4GB, better quality but slower

## Step 4: Test the Model

```bash
ollama run qwen2.5:3b "你好，请用中文回答：什么是段落？"
```

You should see a Chinese response about paragraphs.

## Step 5: Use the LLM Formatter

Once Ollama is running, you can use the new formatter:

```bash
# Format a single entry for testing
python3 scripts/format_content_llm.py --test

# Format all entries (takes ~10-15 minutes for 311 entries)
python3 scripts/format_content_llm.py --all
```

## Troubleshooting

### "Connection refused" error
- Make sure `ollama serve` is running in another terminal

### Model download is slow
- Models are large (2-4GB), be patient
- Download happens only once

### Out of memory errors
- Use the 3b model instead of 7b
- Close other applications

## Performance Expectations

| Model | Speed | Quality | RAM Needed |
|-------|-------|---------|------------|
| qwen2.5:3b | ~2s/entry | Very Good | 8GB |
| qwen2.5:7b | ~4s/entry | Excellent | 16GB |

Total time for 311 entries:
- 3b model: ~10 minutes
- 7b model: ~20 minutes

## Next Steps

After installation, the LLM formatter will:
1. Understand context and semantic meaning
2. Make smarter paragraph break decisions
3. Better identify quotes, questions, and sections
4. Provide more natural, readable formatting

Enjoy your enhanced Bible reading PWA! 📖✨

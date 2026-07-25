# SRT Word Splitter

**Automatically adjust SRT subtitle files to display 2-3 words per line with perfect timing sync.**

Perfect for YouTube Shorts, TikTok, Instagram Reels, and faceless content creators who need meme-style caption pacing.

---

## Why You Need This

When you generate captions from AI voiceovers (ElevenLabs, Synthesia, etc.), they often come as full sentences or long blocks. This creates **rushed, hard-to-read subtitles**.

**SRT Word Splitter** automatically breaks captions into bite-sized chunks (2-3 words) so viewers can actually read them at a natural pace — just like meme captions.

### Before vs After
```
Before (Hard to read):
"I've been on this entire journey learning how to code"

After (Easy to read):
"I've been" → "on this" → "entire journey" → "learning how" → "to code"
```

---

## Features

✅ **Automatic word distribution** — splits captions into 2-3 word chunks  
✅ **Perfect timing sync** — proportionally adjusts timestamps  
✅ **No external dependencies** — pure Python, runs anywhere  
✅ **Batch processing** — process multiple files  
✅ **Customizable pacing** — choose 2, 3, 4+ words per line  
✅ **Preserves formatting** — maintains SRT structure perfectly  

---

## Installation

### Option 1: Direct Download
1. Download `srt_word_splitter.py`
2. Make sure Python 3.6+ is installed
3. Done — no dependencies needed

### Option 2: Clone Repository
```bash
git clone https://github.com/JosephOnifade1/srt-word-splitter.git
cd srt-word-splitter
python srt_word_splitter.py --help
```

---

## Quick Start

### Basic Usage
```bash
python srt_word_splitter.py input.srt output.srt 3
```

### Parameters
- `input.srt` — your original SRT file
- `output.srt` — where to save the new file
- `3` — words per line (default: 3)

### Examples

**Standard pacing (3 words per line):**
```bash
python srt_word_splitter.py captions.srt captions_split.srt 3
```

**Slower, more dramatic (2 words per line):**
```bash
python srt_word_splitter.py captions.srt captions_split.srt 2
```

**Faster, more energetic (4 words per line):**
```bash
python srt_word_splitter.py captions.srt captions_split.srt 4
```

---

## Workflow: From Voiceover to YouTube Shorts

1. **Generate voiceover**  
   ```
   ElevenLabs / Synthesia / Google TTS → audio file
   ```

2. **Get captions**  
   ```
   Descript / YouTube auto-captions / Opus Clip → SRT file
   ```

3. **Split captions**  
   ```bash
   python srt_word_splitter.py captions.srt captions_split.srt 3
   ```

4. **Import to video editor**  
   ```
   CapCut / DaVinci Resolve / Premiere → import SRT
   ```

5. **Add styling**  
   ```
   Apply caption template (yellow/black, meme-style)
   ```

6. **Export & Upload**  
   ```
   YouTube Shorts / TikTok / Instagram Reels
   ```

---

## Output Example

**Input SRT:**
```
1
00:00:00,000 --> 00:00:03,000
I've been on this entire journey learning how to code from scratch

2
00:00:03,500 --> 00:00:07,000
and it's been the most rewarding experience of my life
```

**Output SRT (3 words per line):**
```
1
00:00:00,000 --> 00:00:00,750
I've been on

2
00:00:00,750 --> 00:00:01,500
this entire journey

3
00:00:01,500 --> 00:00:02,250
learning how to

4
00:00:02,250 --> 00:00:03,000
code from scratch

5
00:00:03,500 --> 00:00:04,500
and it's been

6
00:00:04,500 --> 00:00:05,500
the most rewarding

7
00:00:05,500 --> 00:00:06,500
experience of my

8
00:00:06,500 --> 00:00:07,000
life
```

---

## Use Cases

### YouTube Shorts & TikTok
- Faceless content (how-to, motivation, stories)
- AI-generated videos with voiceovers
- Meme-style captions
- High view-to-retention ratio

### Educational Content
- Tutorial videos
- Course content
- Explainer videos
- Language learning

### Social Media
- Instagram Reels
- YouTube Shorts
- TikTok
- Any platform with short-form video

### Content Creators
- Podcast clips
- Gaming highlights
- Commentary videos
- Reaction videos

---

## Troubleshooting

### "The system cannot execute the specified program"
**Solution:** Python isn't in your PATH. Try:
```bash
py srt_word_splitter.py input.srt output.srt 3
```

Or use the full Python path:
```bash
C:\Users\YourName\AppData\Local\Programs\Python\Python314\python.exe srt_word_splitter.py input.srt output.srt 3
```

### "No such file or directory"
**Solution:** Make sure your SRT file is in the same folder as the script, or use the full path:
```bash
python srt_word_splitter.py C:\path\to\captions.srt C:\path\to\captions_split.srt 3
```

### "File not found" error
**Solution:** Check that your input SRT file exists and the filename is spelled correctly.

### Output timing feels off
**Solution:** Increase words per line (4-5) for faster speech, or decrease (2) for slower speech.

---

## Command Line Options

```bash
python srt_word_splitter.py input.srt output.srt [words_per_line]

Positional arguments:
  input.srt              Input SRT subtitle file
  output.srt             Output SRT file (where results are saved)
  words_per_line         Words per line (default: 3)

Examples:
  python srt_word_splitter.py captions.srt split.srt
  python srt_word_splitter.py captions.srt split.srt 2
  python srt_word_splitter.py captions.srt split.srt 4
```

---

## Advanced: Batch Processing

Process multiple SRT files at once:

**On Windows (create `batch_split.bat`):**
```batch
@echo off
for %%F in (*.srt) do (
    python srt_word_splitter.py "%%F" "%%~NF_split.srt" 3
)
echo All files processed!
pause
```

**On Mac/Linux (create `batch_split.sh`):**
```bash
#!/bin/bash
for file in *.srt; do
    python srt_word_splitter.py "$file" "${file%.srt}_split.srt" 3
done
echo "All files processed!"
```

Run it:
```bash
./batch_split.sh  # Mac/Linux
batch_split.bat   # Windows
```

---

## Requirements

- **Python 3.6+**
- No external libraries (pure Python)

That's it! No pip installs, no dependencies to manage.

---

## How It Works

1. **Parse SRT** — reads timecodes and caption text
2. **Split words** — breaks each caption into N-word chunks
3. **Calculate timing** — distributes timestamps proportionally
4. **Output** — writes new SRT with proper formatting

The algorithm ensures:
- Perfect sync (words appear as spoken)
- Proportional timing (fast speech = faster chunks)
- Valid SRT structure (no formatting errors)

---

## Performance

- **Speed:** Process 100+ subtitles in <1 second
- **Accuracy:** Character-perfect timing preservation
- **File size:** Minimal overhead (SRT files are tiny)

---

## Contributing

Have ideas? Found a bug? Submit issues or PRs!

Areas for contribution:
- Better word-breaking algorithms
- Support for other subtitle formats (VTT, ASS)
- GUI version
- Language-specific handling
- Batch processing improvements

---

## License

MIT License — use this however you want (personal, commercial, etc.)

---

## Made For

- **YouTube Shorts creators**
- **TikTok content creators**
- **Faceless video producers**
- **AI content generators**
- **Podcast clip editors**
- **Anyone making short-form video content**

---

## Questions?

- Check the **Troubleshooting** section above
- Open an issue on GitHub
- Check example SRT files in `/examples`

---

**Made to save content creators hours of manual caption editing.**

Star ⭐ if this helped you!

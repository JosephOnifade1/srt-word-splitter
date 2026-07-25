# Quick Start (5 Minutes)

Get up and running in minutes.

---

## For Windows Users

### 1. Make sure Python is installed
```bash
python --version
```

Should show `Python 3.x.x`. If not, install from [python.org](https://www.python.org)

### 2. Download the script
- Download `srt_word_splitter.py` from this repository
- Save it to a folder (e.g., `C:\Users\YourName\Documents\srt_tool`)

### 3. Get your SRT file
- Export captions from Descript, YouTube, or Opus Clip as SRT
- Save it in the **same folder** as the script
- Example: `captions.srt`

### 4. Open Command Prompt
- Press `Win + R`
- Type `cmd` and press Enter

### 5. Navigate to your folder
```bash
cd Documents\srt_tool
```

### 6. Run the script
```bash
python srt_word_splitter.py captions.srt captions_split.srt 3
```

### 7. Done!
- A new file `captions_split.srt` appears in the same folder
- Open it in your video editor (CapCut, DaVinci Resolve, Premiere, etc.)
- Import and apply caption styling

---

## For Mac/Linux Users

### 1. Check Python
```bash
python3 --version
```

Should show `Python 3.x.x`

### 2. Download the script
- Save `srt_word_splitter.py` to a folder

### 3. Get your SRT file
- Export from Descript or YouTube as SRT
- Save in the same folder as the script

### 4. Open Terminal
- Press `Cmd + Space`, type `terminal`, press Enter

### 5. Navigate to your folder
```bash
cd path/to/your/folder
```

### 6. Run the script
```bash
python3 srt_word_splitter.py captions.srt captions_split.srt 3
```

### 7. Done!
- New file created: `captions_split.srt`
- Import into your video editor

---

## Customizing Word Count

Want different pacing?

```bash
# Slower (2 words per line) - more dramatic
python srt_word_splitter.py captions.srt output.srt 2

# Standard (3 words per line) - balanced
python srt_word_splitter.py captions.srt output.srt 3

# Faster (4 words per line) - energetic
python srt_word_splitter.py captions.srt output.srt 4
```

---

## Video Editor Import

### CapCut
1. Import video → Timeline
2. Text → Import subtitle file
3. Choose `captions_split.srt`
4. Apply caption style/template

### DaVinci Resolve
1. Edit → Import Captions
2. Choose `captions_split.srt`
3. Timeline → Captions (adjust styling)

### Adobe Premiere
1. File → Import
2. Choose `captions_split.srt`
3. Drag to timeline
4. Edit caption styling

### Other Editors
Most video editors support SRT import. Check your editor's documentation.

---

## Troubleshooting

### "Python not found"
- Make sure Python is installed
- Restart Command Prompt/Terminal
- Try `py` instead of `python`

### "No such file or directory"
- Make sure SRT file is in the same folder
- Check filename spelling (case-sensitive on Mac/Linux)

### "Wrong timing"
- Increase words per line if speech is fast
- Decrease words per line if speech is slow

---

## Next Steps

1. ✅ Get your SRT file split
2. ✅ Import into video editor
3. ✅ Add caption styling (yellow/black, bold fonts)
4. ✅ Export to YouTube Shorts / TikTok
5. 🎉 Watch it perform

---

**Need help?** Open an issue on GitHub or check the full README.md

**Made for content creators. Happy creating!**

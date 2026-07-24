#!/usr/bin/env python3
"""
SRT Word Splitter - Automatically adjusts SRT captions to show 2-3 words per line
Usage: python srt_word_splitter.py input.srt output.srt [words_per_line]
Default: 3 words per line
"""

import re
import sys
from datetime import timedelta

def parse_srt(filename):
    """Parse SRT file and return list of subtitles"""
    subtitles = []
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by double newlines to separate subtitle blocks
    blocks = content.strip().split('\n\n')
    
    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) >= 3:
            try:
                index = int(lines[0])
                timecode = lines[1]
                text = ' '.join(lines[2:])  # Join multiple lines of text
                subtitles.append({
                    'index': index,
                    'timecode': timecode,
                    'text': text
                })
            except ValueError:
                continue
    
    return subtitles

def timecode_to_ms(timecode):
    """Convert SRT timecode to milliseconds"""
    pattern = r'(\d{2}):(\d{2}):(\d{2}),(\d{3})'
    match = re.match(pattern, timecode)
    if match:
        hours, mins, secs, ms = map(int, match.groups())
        total_ms = hours * 3600000 + mins * 60000 + secs * 1000 + ms
        return total_ms
    return 0

def ms_to_timecode(ms):
    """Convert milliseconds to SRT timecode"""
    hours = ms // 3600000
    ms %= 3600000
    minutes = ms // 60000
    ms %= 60000
    seconds = ms // 1000
    milliseconds = ms % 1000
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def split_subtitle(subtitle, words_per_line):
    """Split a subtitle into multiple lines with proportional timing"""
    start_end = subtitle['timecode'].split(' --> ')
    start_ms = timecode_to_ms(start_end[0])
    end_ms = timecode_to_ms(start_end[1])
    
    text = subtitle['text']
    words = text.split()
    
    if len(words) <= words_per_line:
        return [subtitle]
    
    # Split words into chunks
    chunks = []
    for i in range(0, len(words), words_per_line):
        chunks.append(' '.join(words[i:i + words_per_line]))
    
    # Calculate timing for each chunk
    duration_ms = end_ms - start_ms
    chunk_duration = duration_ms / len(chunks)
    
    new_subs = []
    for i, chunk in enumerate(chunks):
        chunk_start = start_ms + (i * chunk_duration)
        chunk_end = chunk_start + chunk_duration
        
        new_subs.append({
            'index': subtitle['index'] + i,
            'timecode': f"{ms_to_timecode(int(chunk_start))} --> {ms_to_timecode(int(chunk_end))}",
            'text': chunk
        })
    
    return new_subs

def write_srt(filename, subtitles):
    """Write subtitles to SRT file"""
    with open(filename, 'w', encoding='utf-8') as f:
        for i, sub in enumerate(subtitles, 1):
            f.write(f"{i}\n")
            f.write(f"{sub['timecode']}\n")
            f.write(f"{sub['text']}\n\n")

def main():
    if len(sys.argv) < 3:
        print("Usage: python srt_word_splitter.py input.srt output.srt [words_per_line]")
        print("Example: python srt_word_splitter.py captions.srt captions_split.srt 3")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    words_per_line = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    
    try:
        print(f"Reading {input_file}...")
        subtitles = parse_srt(input_file)
        print(f"Found {len(subtitles)} subtitles")
        
        print(f"Splitting to {words_per_line} words per line...")
        split_subs = []
        for sub in subtitles:
            split_subs.extend(split_subtitle(sub, words_per_line))
        
        print(f"Writing {len(split_subs)} subtitle blocks to {output_file}...")
        write_srt(output_file, split_subs)
        print(f"✓ Done! Output saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

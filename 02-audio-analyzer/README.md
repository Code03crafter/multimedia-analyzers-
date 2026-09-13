# Audio Analyzer (Task 3)

Extracts and prints metadata from an audio file: file info (name, size,
container, duration), audio stream details (codec, channels, sampling
rate, bit rate), and any embedded tags (title, artist, album, etc.).

## Setup
Requires ffmpeg/ffprobe on your PATH:
- Windows: https://ffmpeg.org/download.html
- Mac: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg`

Check it worked: `ffprobe -version`

## Usage
```bash
python audio_analyzer.py path/to/song.mp3
```

## Supported Formats
MP3, WAV, FLAC, OGG, M4A, AAC (anything ffprobe can read)

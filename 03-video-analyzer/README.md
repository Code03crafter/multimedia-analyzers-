# Video Analyzer (Task 2 / LAB 3)

Extracts and prints metadata from a video file: file info (name, size,
container, duration), video stream details (resolution, frame rate, bit
rate, codec), audio stream details (codec, channels, sampling rate, bit
rate), and any embedded metadata tags.

## Setup
Requires ffmpeg/ffprobe on your PATH:
- Windows: https://ffmpeg.org/download.html
- Mac: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg`

Check it worked: `ffprobe -version`

## Usage
```bash
python video_analyzer.py path/to/video.mp4
```

## Supported Formats
MP4, AVI, MOV, MKV, WEBM (anything ffprobe can read)

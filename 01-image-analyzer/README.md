# Image Analyzer (Task 1)

Extracts and prints metadata from an image file: file info (name, size,
format, dimensions, color mode) plus EXIF metadata (camera, date taken,
orientation, and any other available EXIF tags).

## Setup
```bash
pip install pillow
```

## Usage
```bash
python image_analyzer.py path/to/image.jpg
```

## Supported Formats
- Minimum: JPG/JPEG, PNG
- Bonus: TIFF, WEBP, BMP

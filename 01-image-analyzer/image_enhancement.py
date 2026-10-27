from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import os





def load_image(path):
    """Load image from given path"""
    img = Image.open(path).convert('RGB')
    print(f"Image loaded successfully: {path}")
    print(f"Image Resolution : {img.size[0]} x {img.size[1]} pixels")
    return img


# ─── BASIC ENHANCEMENTS ──────────────────────────────

def adjust_brightness(img, factor=1.8):
    """Increase or decrease image brightness"""
    enhancer = ImageEnhance.Brightness(img)
    result = enhancer.enhance(factor)
    print("Brightness adjustment applied successfully")
    return result


def adjust_contrast(img, factor=2.0):
    """Enhance image contrast"""
    enhancer = ImageEnhance.Contrast(img)
    result = enhancer.enhance(factor)
    print("Contrast adjustment applied successfully")
    return result


def apply_sharpening(img, factor=3.0):
    """Apply sharpening filter"""
    enhancer = ImageEnhance.Sharpness(img)
    result = enhancer.enhance(factor)
    print("Sharpening filter applied successfully")
    return result


def apply_blur(img):
    """Apply Gaussian blur for smoothing"""
    result = img.filter(ImageFilter.GaussianBlur(radius=5))
    print("Gaussian blur applied successfully")
    return result


def grayscale(img):
    """Convert color image to grayscale"""
    result = img.convert('L').convert('RGB')
    print("Grayscale conversion applied successfully")
    return result


def apply_sepia(img):
    """Apply vintage sepia tone filter"""
    img_array = np.array(img, dtype=np.float64)
    r = img_array[:, :, 0]
    g = img_array[:, :, 1]
    b = img_array[:, :, 2]
    new_r = np.clip(r * 0.393 + g * 0.769 + b * 0.189, 0, 255)
    new_g = np.clip(r * 0.349 + g * 0.686 + b * 0.168, 0, 255)
    new_b = np.clip(r * 0.272 + g * 0.534 + b * 0.131, 0, 255)
    sepia = np.stack([new_r, new_g, new_b], axis=2).astype(np.uint8)
    result = Image.fromarray(sepia)
    print("Sepia filter applied successfully")
    return result


# ─── ADVANCED ENHANCEMENTS ───────────────────────────

def edge_detection(img):
    """Detect edges using PIL edge filter"""
    result = img.filter(ImageFilter.FIND_EDGES)
    print("Edge detection applied successfully")
    return result


def emboss_effect(img):
    """Apply emboss effect"""
    result = img.filter(ImageFilter.EMBOSS)
    print("Emboss effect applied successfully")
    return result


def smooth_enhance(img):
    """Apply smooth enhancement filter"""
    result = img.filter(ImageFilter.SMOOTH_MORE)
    print("Smooth enhancement applied successfully")
    return result


def detail_enhance(img):
    """Enhance fine details in image"""
    result = img.filter(ImageFilter.DETAIL)
    print("Detail enhancement applied successfully")
    return result


def contour_effect(img):
    """Apply contour detection effect"""
    result = img.filter(ImageFilter.CONTOUR)
    print("Contour effect applied successfully")
    return result


def color_enhance(img, factor=2.0):
    """Enhance color saturation"""
    enhancer = ImageEnhance.Color(img)
    result = enhancer.enhance(factor)
    print("Color enhancement applied successfully")
    return result


# ─── VISUALIZATION ───────────────────────────────────

def show_comparison(original, enhanced, title):
    """Display original vs enhanced image side by side"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].imshow(original)
    axes[0].set_title('Original Image', fontsize=13, fontweight='bold')
    axes[0].axis('off')

    axes[1].imshow(enhanced)
    axes[1].set_title(title, fontsize=13, fontweight='bold')
    axes[1].axis('off')

    plt.suptitle(
        f'Image Enhancement — {title}',
        fontsize=15,
        fontweight='bold',
        color='#1F4E79'
    )
    plt.tight_layout()

    output_filename = f'outputs/output_{title.replace(" ", "_")}.png'
    plt.savefig(output_filename, dpi=150, bbox_inches='tight')
    plt.show()
    print(f"Output saved: {output_filename}")


# ─── MAIN ────────────────────────────────────────────

def main():
    print("=" * 55)
    print("   IMAGE ENHANCEMENT PROJECT")
    print("   Author  : Ranu Patidar")
    print("   Roll No : IC-2K22-66")
    print("   College : IIPS")
    print("=" * 55)

    # Create output directory
    os.makedirs('outputs', exist_ok=True)

    # Search for input image
    possible_paths = [
        'Untitled-1.png',
        '../Untitled-1.png',
        '../../Untitled-1.png',
    ]

    img_path = None
    for path in possible_paths:
        if os.path.exists(path):
            img_path = path
            break

    if img_path is None:
        print("ERROR: Input image not found.")
        print("Please place Untitled-1.png inside the 01-image-analyzer folder.")
        return

    # Load image
    img = load_image(img_path)

    # ── BASIC ENHANCEMENTS ──
    print("\n" + "=" * 55)
    print("   BASIC ENHANCEMENTS")
    print("=" * 55)

    show_comparison(img, adjust_brightness(img, 1.8),  "Brightness")
    show_comparison(img, adjust_contrast(img, 2.0),    "Contrast")
    show_comparison(img, apply_sharpening(img, 3.0),   "Sharpening")
    show_comparison(img, apply_blur(img),               "Gaussian Blur")
    show_comparison(img, grayscale(img),                "Grayscale")
    show_comparison(img, apply_sepia(img),              "Sepia Filter")
    show_comparison(img, color_enhance(img, 2.0),       "Color Enhancement")

    # ── ADVANCED ENHANCEMENTS ──
    print("\n" + "=" * 55)
    print("   ADVANCED ENHANCEMENTS")
    print("=" * 55)

    show_comparison(img, edge_detection(img),   "Edge Detection")
    show_comparison(img, emboss_effect(img),    "Emboss Effect")
    show_comparison(img, smooth_enhance(img),   "Smooth Enhancement")
    show_comparison(img, detail_enhance(img),   "Detail Enhancement")
    show_comparison(img, contour_effect(img),   "Contour Effect")

    # ── FINAL SUMMARY ──
    print("\n" + "=" * 55)
    print("   IMAGE ENHANCEMENT COMPLETED SUCCESSFULLY")
    print("   Total Enhancements Applied : 12")
    print("   Output Location            : outputs/ folder")
    print("=" * 55)


if __name__ == "__main__":
    main()
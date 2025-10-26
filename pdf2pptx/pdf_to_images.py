#!/usr/bin/env python3
"""
PDF to Images Converter Module
"""

import os
from pathlib import Path

try:
    from pdf2image import convert_from_path
    PDF2IMAGE_AVAILABLE = True
except ImportError:
    PDF2IMAGE_AVAILABLE = False
    convert_from_path = None


def convert_pdf_to_images(pdf_path, output_dir, dpi=300):
    """
    Convert PDF to images
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save the images
        dpi: Resolution of output images (default: 300)
        
    Returns:
        List of paths to generated images
    """
    if not PDF2IMAGE_AVAILABLE:
        raise ImportError(
            "pdf2image library not found.\n"
            "Please install it using: pip install pdf2image\n"
            "Note: You also need poppler installed on your system:\n"
            "  - macOS: brew install poppler\n"
            "  - Ubuntu/Debian: sudo apt-get install poppler-utils\n"
            "  - Windows: Download from https://github.com/oschwartz10612/poppler-windows/releases/"
        )
    
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Check if PDF file exists
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file '{pdf_path}' not found!")
    
    print(f"Converting '{pdf_path}' to images...")
    print(f"Output directory: '{output_dir}'")
    print(f"DPI: {dpi}")
    
    # Convert PDF to images
    images = convert_from_path(pdf_path, dpi=dpi)
    
    print(f"Total pages: {len(images)}")
    
    # Save each page as an image
    image_paths = []
    for i, image in enumerate(images, start=1):
        image_path = output_path / f"page_{i:03d}.png"
        image.save(image_path, "PNG")
        print(f"  Saved: {image_path.name}")
        image_paths.append(str(image_path))
    
    print(f"✓ Successfully converted {len(images)} pages to images!")
    
    return image_paths


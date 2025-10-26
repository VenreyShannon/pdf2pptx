#!/usr/bin/env python3
"""
PDF to PowerPoint Converter
Main conversion logic
"""

import shutil
import tempfile
from pathlib import Path
from .pdf_to_images import convert_pdf_to_images
from .images_to_ppt import convert_images_to_ppt


def pdf_to_ppt(pdf_path, output_path=None, dpi=300):
    """
    Convert PDF to PowerPoint presentation
    
    Args:
        pdf_path: Path to the PDF file (str or Path)
        output_path: Path to the output PowerPoint file (str or Path, optional)
                    If not provided, defaults to same directory and name as PDF
        dpi: Resolution for image conversion (default: 300)
    
    Returns:
        Path to the generated PowerPoint file
    """
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file '{pdf_path}' not found!")
    
    # Get PDF directory and filename
    pdf_dir = pdf_path.parent
    pdf_name = pdf_path.stem
    
    # Create temporary directory for images in system temp folder
    temp_images_dir = tempfile.mkdtemp(prefix=f"pdf2ppt_{pdf_name}_")
    
    # Determine output path
    if output_path:
        output_ppt = Path(output_path)
    else:
        # Default: same directory as PDF with .pptx extension
        output_ppt = pdf_dir / f"{pdf_name}.pptx"
    
    try:
        print("=" * 60)
        print(f"Converting PDF to PowerPoint")
        print("=" * 60)
        print(f"Temporary directory: {temp_images_dir}")
        
        # Step 1: Convert PDF to images
        print("\nStep 1: Converting PDF to images...")
        convert_pdf_to_images(pdf_path, temp_images_dir, dpi=dpi)
        
        # Step 2: Convert images to PPT
        print("\nStep 2: Creating PowerPoint presentation...")
        result = convert_images_to_ppt(temp_images_dir, output_ppt)
        
        print("=" * 60)
        print(f"✓ Conversion complete!")
        print(f"Output: {output_ppt.absolute()}")
        print("=" * 60)
        
        return result
        
    finally:
        # Clean up temporary images directory
        if Path(temp_images_dir).exists():
            print(f"\nCleaning up temporary files...")
            shutil.rmtree(temp_images_dir)
            print(f"✓ Temporary files removed")


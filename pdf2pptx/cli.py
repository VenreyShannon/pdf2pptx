#!/usr/bin/env python3
"""
Command-line interface for pdf2pptx
"""

import argparse
import sys
from pathlib import Path
from .converter import pdf_to_ppt


def main():
    """Main function to handle command line arguments"""
    parser = argparse.ArgumentParser(
        description='将 PDF 文件转换为 PowerPoint 演示文稿',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  pdf2ppt -f input.pdf                        # 使用默认设置
  pdf2ppt -f input.pdf -d output.pptx         # 指定输出文件
  pdf2ppt -f input.pdf -q 150                 # 使用较低质量（更小的文件）
  pdf2ppt -f input.pdf -d output.pptx -q 600  # 指定输出文件和高质量
        '''
    )
    
    # 必须参数
    parser.add_argument(
        '-f', '--file',
        required=True,
        help='PDF 文件路径（必需）'
    )
    
    # 可选参数
    parser.add_argument(
        '-d', '--destination',
        help='输出 PPTX 文件路径（可选，默认为与 PDF 同目录同名）'
    )
    
    parser.add_argument(
        '-q', '--quality',
        type=int,
        default=300,
        help='图片质量（DPI），默认为 300。数值越大质量越高但文件越大'
    )
    
    args = parser.parse_args()
    
    # 验证输出路径
    if args.destination:
        output_path = Path(args.destination)
        if not output_path.suffix.lower() == '.pptx':
            print(f"❌ 错误：输出文件必须以 .pptx 结尾")
            print(f"   您指定的路径: {args.destination}")
            sys.exit(1)
    else:
        output_path = None
    
    # 验证 DPI 值
    if args.quality <= 0:
        print(f"❌ 错误：质量（DPI）必须大于 0")
        sys.exit(1)
    
    # 执行转换
    try:
        pdf_to_ppt(args.file, output_path=output_path, dpi=args.quality)
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()


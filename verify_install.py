#!/usr/bin/env python3
"""
验证 pdf2pptx 安装是否正确
"""

import sys
import subprocess

def check_python_version():
    """检查 Python 版本"""
    version = sys.version_info
    print(f"✓ Python 版本: {version.major}.{version.minor}.{version.micro}")
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("  ⚠️  警告: 建议使用 Python 3.7 或更高版本")
        return False
    return True

def check_package_installed():
    """检查包是否安装"""
    try:
        import pdf2pptx
        print(f"✓ pdf2pptx 包已安装，版本: {pdf2pptx.__version__}")
        return True
    except ImportError:
        print("✗ pdf2pptx 包未安装")
        print("  请运行: pip install .")
        return False

def check_dependencies():
    """检查依赖是否安装"""
    deps = {
        'pdf2image': 'pdf2image',
        'pptx': 'python-pptx',
        'PIL': 'Pillow'
    }
    
    all_installed = True
    for module, package in deps.items():
        try:
            __import__(module)
            print(f"✓ {package} 已安装")
        except ImportError:
            print(f"✗ {package} 未安装")
            print(f"  请运行: pip install {package}")
            all_installed = False
    
    return all_installed

def check_poppler():
    """检查 Poppler 是否安装"""
    try:
        result = subprocess.run(['pdfinfo', '-v'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if result.returncode == 0:
            print("✓ Poppler 已安装")
            return True
        else:
            print("✗ Poppler 未安装或不在 PATH 中")
            return False
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("✗ Poppler 未安装")
        print("  macOS: brew install poppler")
        print("  Ubuntu/Debian: sudo apt-get install poppler-utils")
        return False

def check_command():
    """检查命令行工具是否可用"""
    try:
        result = subprocess.run(['pdf2ppt', '--help'], 
                              capture_output=True, 
                              text=True,
                              timeout=5)
        if result.returncode == 0:
            print("✓ pdf2ppt 命令可用")
            return True
        else:
            print("✗ pdf2ppt 命令不可用")
            return False
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("✗ pdf2ppt 命令未找到")
        print("  可能需要重新安装: pip install .")
        return False

def main():
    """主验证流程"""
    print("=" * 60)
    print("pdf2pptx 安装验证")
    print("=" * 60)
    print()
    
    results = []
    
    print("1. 检查 Python 版本...")
    results.append(check_python_version())
    print()
    
    print("2. 检查 pdf2pptx 包...")
    results.append(check_package_installed())
    print()
    
    print("3. 检查 Python 依赖...")
    results.append(check_dependencies())
    print()
    
    print("4. 检查系统依赖（Poppler）...")
    results.append(check_poppler())
    print()
    
    print("5. 检查命令行工具...")
    results.append(check_command())
    print()
    
    print("=" * 60)
    if all(results):
        print("✅ 所有检查通过！pdf2pptx 已正确安装。")
        print()
        print("您现在可以使用以下命令：")
        print("  pdf2ppt -f input.pdf")
    else:
        print("❌ 有些检查未通过，请按照上述提示进行修复。")
        return 1
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())


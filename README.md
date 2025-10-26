# pdf2pptx

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/VenreyShannon/pdf2pptx.svg)](https://github.com/VenreyShannon/pdf2pptx/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/VenreyShannon/pdf2pptx.svg)](https://github.com/VenreyShannon/pdf2pptx/issues)

一个简单易用的命令行工具，可以将 PDF 文件转换为 PowerPoint 演示文稿（PPTX 格式，纯图片转换，保存在同pdf目录下）。

## ⚡ 快速开始

### 第一步：确保已安装 Python

**检查是否已安装 Python：**
```bash
python3 --version
```

如果提示找不到命令，请先安装 Python：

**macOS:**
```bash
# 使用 Homebrew 安装（推荐）
brew install python3

# 或从官网下载：https://www.python.org/downloads/
```

**Windows:**
1. 访问 [Python 官网](https://www.python.org/downloads/)
2. 下载最新版本（Python 3.7 或更高）
3. 安装时**务必勾选** "Add Python to PATH"

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 第二步：安装依赖（Poppler）

**macOS:**
```bash
brew install poppler
```

**Ubuntu/Debian:**
```bash
sudo apt-get install poppler-utils
```

**Windows:**
1. 从 [这里](https://github.com/oschwartz10612/poppler-windows/releases/) 下载 Poppler
2. 解压到某个目录（例如 `C:\Program Files\poppler`）
3. 将 `bin` 目录添加到系统 PATH 环境变量中

### 第三步：安装 pdf2pptx

```bash
# 1. 安装 pipx（如果还没有）
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# 2. 重启终端，然后安装 pdf2pptx
pipx install git+https://github.com/VenreyShannon/pdf2pptx.git
# 或使用 SSH 协议（更稳定）
pipx install git+ssh://git@github.com/VenreyShannon/pdf2pptx.git

# 3. 使用
pdf2ppt -f your_file.pdf
```

就这么简单！✨

### 常用命令

```bash
# 基本使用（默认输出到同目录）
pdf2ppt -f input.pdf

# 指定输出路径
pdf2ppt -f input.pdf -d output.pptx

# 调整质量（DPI）
pdf2ppt -f input.pdf -q 150    # 低质量（文件小）
pdf2ppt -f input.pdf -q 300    # 默认质量
pdf2ppt -f input.pdf -q 600    # 高质量（文件大）
```

---

## 📋 功能特点

- ✅ 将 PDF 的每一页转换为 PowerPoint 的一张幻灯片
- ✅ 保持原始 PDF 的画面质量
- ✅ 自动调整图片大小以适应幻灯片
- ✅ 可自定义输出质量（DPI）
- ✅ 简单的命令行界面
- ✅ 自动清理临时文件

---

## 💻 系统要求

### 1. Python（必需）
需要 Python 3.7 或更高版本。

如果您还没有安装 Python，请参考上面的"快速开始"部分获取安装指南。

### 2. Poppler（必需）
此工具依赖 Poppler 来处理 PDF 文件。安装方法请参考上面"快速开始"的第二步。

---

## 📦 安装

### 推荐方式：使用 pipx（不影响本地环境）

**pipx 会为工具创建隔离环境，完全不会影响您的 Python 环境！**

```bash
# 1. 安装 pipx
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# 2. 重启终端，然后安装 pdf2pptx
# 从 GitHub 安装
pipx install git+https://github.com/VenreyShannon/pdf2pptx.git

# 或从本地安装
cd pdf2pptx
pipx install .
```

### 传统方式：使用 pip

```bash
# 克隆仓库
git clone https://github.com/VenreyShannon/pdf2pptx.git
cd pdf2pptx

# 安装包
pip install .

# 或以开发模式安装
pip install -e .
```

---

## 🚀 使用方法

### 命令行参数

| 参数 | 简写 | 必需 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--file` | `-f` | ✅ | - | PDF 文件路径 |
| `--destination` | `-d` | ❌ | 同名.pptx | 输出 PPTX 文件路径 |
| `--quality` | `-q` | ❌ | 300 | 图片质量（DPI） |

### 使用示例

```bash
# 基本使用
pdf2ppt -f document.pdf

# 指定输出路径
pdf2ppt -f input.pdf -d ~/Desktop/output.pptx

# 调整质量
pdf2ppt -f input.pdf -q 150

# 完整示例
pdf2ppt -f ~/Documents/report.pdf -d ~/Desktop/presentation.pptx -q 300
```

### 批量转换

```bash
# 转换当前目录下所有 PDF
for pdf in *.pdf; do
    pdf2ppt -f "$pdf"
done
```

### 作为 Python 模块使用

```python
from pdf2pptx import pdf_to_ppt

# 基本使用
pdf_to_ppt('input.pdf')

# 指定输出路径和质量
pdf_to_ppt('input.pdf', output_path='output.pptx', dpi=300)
```

---

## ❓ 常见问题

### Q: 我没有安装 Python，怎么办？
**A:** 请参考上面"快速开始"的第一步，里面有详细的 Python 安装指南。Python 3.7 或更高版本都可以使用。

### Q: 提示找不到 Poppler？
**A:** 请确保已经安装了 Poppler 并添加到系统 PATH 中。参见上面"快速开始"的第二步。

### Q: 转换后的 PPTX 文件很大？
**A:** 尝试降低 DPI 值，例如使用 `-q 150` 或 `-q 200`。

### Q: 担心 pip install 影响本地环境？
**A:** 使用 pipx 安装！它会自动创建隔离环境，完全不会影响您的系统。

### Q: 如何更新到最新版本？
**A:** 
- **pipx 从 GitHub 安装的**：`pipx install --force git+https://github.com/VenreyShannon/pdf2pptx.git`
- **pipx 从本地安装的**：先 `git pull` 更新代码，然后 `pipx reinstall pdf2pptx`
- **pip 安装的**：重新运行 `pip install .` 或 `pip install -e .`

### Q: 如何卸载？
**A:** 
- pipx 安装：`pipx uninstall pdf2pptx`
- pip 安装：`pip uninstall pdf2pptx`

---

## ⚠️ 注意事项

1. **文件大小**：高 DPI 值会生成更大的 PPTX 文件
2. **转换时间**：页数多或 DPI 高的转换会需要较长时间
3. **临时文件**：转换过程中会创建临时图片文件，完成后会自动清理
4. **内存使用**：处理大型 PDF 文件时可能需要较多内存

---

如果这个工具对您有帮助，请给个 ⭐ Star！

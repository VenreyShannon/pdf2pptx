#!/usr/bin/env python3
"""
Setup script for pdf2pptx
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = ""
readme_path = this_directory / "README.md"
if readme_path.exists():
    long_description = readme_path.read_text(encoding='utf-8')

setup(
    name='pdf2pptx',
    version='1.0.0',
    author='Venrey Shannon',
    author_email='VenreyShannon@gmail.com',
    description='Convert PDF files to PowerPoint presentations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/VenreyShannon/pdf2pptx',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Office/Business :: Office Suites',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=[
        'pdf2image>=1.16.0',
        'python-pptx>=0.6.21',
        'Pillow>=9.0.0',
    ],
    entry_points={
        'console_scripts': [
            'pdf2ppt=pdf2pptx.cli:main',
        ],
    },
    keywords='pdf powerpoint pptx converter',
    project_urls={
        'Bug Reports': 'https://github.com/VenreyShannon/pdf2pptx/issues',
        'Source': 'https://github.com/VenreyShannon/pdf2pptx',
    },
)


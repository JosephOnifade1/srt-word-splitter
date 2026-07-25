#!/usr/bin/env python3
"""
Setup configuration for SRT Word Splitter
Enables installation via: pip install srt-word-splitter
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="srt-word-splitter",
    version="1.0.0",
    author="Joseph Onifade",
    author_email="josephonifade08@gmail.com",
    description="Automatically split SRT subtitles into 2-3 word chunks with perfect timing sync",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JosephOnifade1/srt-word-splitter",
    project_urls={
        "Bug Tracker": "https://github.com/JosephOnifade1/srt-word-splitter/issues",
        "Documentation": "https://github.com/JosephOnifade1/srt-word-splitter#readme",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Video :: Non-Linear Editors",
        "Topic :: Text Processing",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.6",
    py_modules=["srt_word_splitter"],
    entry_points={
        "console_scripts": [
            "srt-word-splitter=srt_word_splitter:main",
        ],
    },
    keywords=[
        "srt",
        "subtitles",
        "captions",
        "video",
        "youtube-shorts",
        "tiktok",
        "video-editing",
        "caption-formatter",
        "automation",
        "content-creation",
    ],
    zip_safe=False,
)

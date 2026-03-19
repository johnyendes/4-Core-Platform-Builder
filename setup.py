"""
X-Core Platform Setup Script
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="xcore-platform",
    version="1.0.0",
    author="X-Core Development Team",
    description="The Ultimate Modular AI Platform for Digital Blueprint Generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johnyendes/4-Core-Platform-Builder",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: Other/Proprietary",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "typing-extensions>=4.8.0",
    ],
)
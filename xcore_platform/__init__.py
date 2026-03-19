"""
X-Core Platform
The Ultimate Modular AI Platform for Digital Blueprint Generation
"""

__version__ = "1.0.0"
__author__ = "X-Core Development Team"

from .xcore import (
    BrainAPI,
    PackLoader,
    PackRunner,
    XCoreRegistry,
    LicenseManager,
)

__all__ = [
    "BrainAPI",
    "PackLoader",
    "PackRunner",
    "XCoreRegistry",
    "LicenseManager",
]
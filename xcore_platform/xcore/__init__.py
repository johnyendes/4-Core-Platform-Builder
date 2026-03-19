"""
X-Core Platform - Core Module
The Ultimate Modular AI Platform for Digital Blueprint Generation
"""

__version__ = "1.0.0"
__author__ = "X-Core Development Team"

from .brain_api import BrainAPI
from .pack_loader import PackLoader
from .pack_runner import PackRunner
from .xcore_registry import XCoreRegistry
from .license_manager import LicenseManager

__all__ = [
    "BrainAPI",
    "PackLoader",
    "PackRunner",
    "XCoreRegistry",
    "LicenseManager",
]
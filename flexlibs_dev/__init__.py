"""
FlexLibs Development Module

This module contains Pythonic wrapper methods for FLEx data model access.
Part of the Complete Data Access initiative to add ~290 methods for full CRUD access.

Author: FlexTools Development Team
Date: 2025-11-22
"""

from .text_ops import (
    TextCoreOperations,
    TextAdvancedOperations,
    ParagraphCRUDOperations,
)

__all__ = [
    'TextCoreOperations',
    'TextAdvancedOperations',
    'ParagraphCRUDOperations',
]

__version__ = "0.1.0"
__author__ = "FlexTools Development Team"

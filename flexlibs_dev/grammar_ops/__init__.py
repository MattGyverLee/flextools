"""
Grammar Operations Module

This module provides operations for working with Parts of Speech, Grammatical
Categories, and other grammar-related data in FLEx.

Submodules:
    - pos_crud: Parts of Speech CRUD operations
    - pos_advanced: Advanced POS operations

Author: FlexTools Development Team - Phase 2
Date: 2025-11-22
"""

from .pos_crud import (
    POSGetAll,
    POSCreate,
    POSDelete,
    POSExists,
    POSFind,
    POSGetName,
    POSSetName,
    POSGetAbbreviation,
    POSSetAbbreviation,
    POSGetSubcategories,
)

__all__ = [
    # POS CRUD operations
    'POSGetAll',
    'POSCreate',
    'POSDelete',
    'POSExists',
    'POSFind',
    'POSGetName',
    'POSSetName',
    'POSGetAbbreviation',
    'POSSetAbbreviation',
    'POSGetSubcategories',
]

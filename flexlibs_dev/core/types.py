"""
Core Type Definitions

This module provides common type definitions, type aliases, and protocols
used across all flexlibs modules.

Author: FlexTools Development Team
Date: 2025-11-22
"""

from typing import Any, Union, Optional, Protocol, TypeVar


# Type aliases for FLEx objects (to be replaced with actual imports when integrated)
IText = Any
IStText = Any
IStTxtPara = Any
ISegment = Any
IAnalysis = Any
IWfiWordform = Any
IWfiAnalysis = Any
IWfiGloss = Any
ICmMedia = Any
ICmFile = Any
INote = Any
ICmBaseAnnotation = Any
ICmTranslation = Any


# Generic type variable for objects or HVOs
ObjectOrHVO = TypeVar('ObjectOrHVO', bound=Union[Any, int])


# Writing system handle type - can be string (language tag) or int (ID)
WritingSystemHandle = Union[str, int]


# HVO type alias for clarity
HVO = int


class FlexObject(Protocol):
    """
    Protocol for FLEx objects.

    All FLEx objects have an HVO (Handle to Virtual Object) property
    that uniquely identifies them in the database.
    """

    @property
    def Hvo(self) -> int:
        """The object's HVO (database ID)."""
        ...


class FlexProject(Protocol):
    """
    Protocol for FLEx Project objects.

    Defines the minimal interface needed for project-level operations.
    """

    def GetObject(self, hvo: int) -> Any:
        """Get an object by its HVO."""
        ...

    @property
    def DefaultVernacularWs(self) -> int:
        """Default vernacular writing system handle."""
        ...

    @property
    def DefaultAnalysisWs(self) -> int:
        """Default analysis writing system handle."""
        ...


# Common return types
OptionalText = Optional[IText]
OptionalParagraph = Optional[IStTxtPara]
OptionalSegment = Optional[ISegment]
OptionalWordform = Optional[IWfiWordform]


__all__ = [
    # Type aliases
    'IText',
    'IStText',
    'IStTxtPara',
    'ISegment',
    'IAnalysis',
    'IWfiWordform',
    'IWfiAnalysis',
    'IWfiGloss',
    'ICmMedia',
    'ICmFile',
    'INote',
    'ICmBaseAnnotation',
    'ICmTranslation',

    # Generic types
    'ObjectOrHVO',
    'WritingSystemHandle',
    'HVO',

    # Protocols
    'FlexObject',
    'FlexProject',

    # Optional types
    'OptionalText',
    'OptionalParagraph',
    'OptionalSegment',
    'OptionalWordform',
]

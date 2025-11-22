"""
Core Resolver Functions

This module provides shared resolver functions that convert HVO references
to FLEx objects. These are used across all modules to handle parameters
that can be either objects or integer HVOs.

Author: FlexTools Development Team
Date: 2025-11-22
"""

from typing import Union, Any, Optional
from .types import HVO


def resolve_object(obj_or_hvo: Union[Any, HVO], project: Any) -> Optional[Any]:
    """
    Resolve a reference to a FLEx object.

    This is a generic resolver that works with any FLEx object type.

    Args:
        obj_or_hvo: Either a FLEx object or its HVO (integer identifier)
        project: The FLExProject instance

    Returns:
        The FLEx object, or None if not found

    Example:
        >>> obj = resolve_object(text_or_hvo, self.project)
        >>> if obj is None:
        ...     raise ValueError("Object not found")
    """
    if isinstance(obj_or_hvo, int):
        # It's an HVO, look up the object
        # TODO: Integrate with FLEx API
        # return project.GetObject(obj_or_hvo)
        raise NotImplementedError("FLEx API integration pending")
    else:
        # Assume it's already a FLEx object
        return obj_or_hvo


def resolve_text(text_or_hvo: Union[Any, HVO], project: Any) -> Optional[Any]:
    """
    Resolve a text reference to an IText object.

    Args:
        text_or_hvo: Either an IText object or its HVO (integer identifier)
        project: The FLExProject instance

    Returns:
        IText object or None if not found

    Example:
        >>> text_obj = resolve_text(text_or_hvo, self.project)
        >>> if text_obj is None:
        ...     raise ValueError(f"Text not found: {text_or_hvo}")
    """
    return resolve_object(text_or_hvo, project)


def resolve_paragraph(para_or_hvo: Union[Any, HVO], project: Any) -> Optional[Any]:
    """
    Resolve a paragraph reference to an IStTxtPara object.

    Args:
        para_or_hvo: Either an IStTxtPara object or its HVO (integer identifier)
        project: The FLExProject instance

    Returns:
        IStTxtPara object or None if not found

    Example:
        >>> para_obj = resolve_paragraph(para_or_hvo, self.project)
        >>> if para_obj is None:
        ...     raise ValueError(f"Paragraph not found: {para_or_hvo}")
    """
    return resolve_object(para_or_hvo, project)


def resolve_segment(segment_or_hvo: Union[Any, HVO], project: Any) -> Optional[Any]:
    """
    Resolve a segment reference to an ISegment object.

    Args:
        segment_or_hvo: Either an ISegment object or its HVO (integer identifier)
        project: The FLExProject instance

    Returns:
        ISegment object or None if not found

    Example:
        >>> segment_obj = resolve_segment(segment_or_hvo, self.project)
        >>> if segment_obj is None:
        ...     raise ValueError(f"Segment not found: {segment_or_hvo}")
    """
    return resolve_object(segment_or_hvo, project)


def resolve_wordform(wordform_or_hvo: Union[Any, HVO], project: Any) -> Optional[Any]:
    """
    Resolve a wordform reference to an IWfiWordform object.

    Args:
        wordform_or_hvo: Either an IWfiWordform object or its HVO (integer identifier)
        project: The FLExProject instance

    Returns:
        IWfiWordform object or None if not found

    Example:
        >>> wordform_obj = resolve_wordform(wordform_or_hvo, self.project)
        >>> if wordform_obj is None:
        ...     raise ValueError(f"Wordform not found: {wordform_or_hvo}")
    """
    return resolve_object(wordform_or_hvo, project)


def resolve_analysis(analysis_or_hvo: Union[Any, HVO], project: Any) -> Optional[Any]:
    """
    Resolve an analysis reference to an IWfiAnalysis object.

    Args:
        analysis_or_hvo: Either an IWfiAnalysis object or its HVO (integer identifier)
        project: The FLExProject instance

    Returns:
        IWfiAnalysis object or None if not found

    Example:
        >>> analysis_obj = resolve_analysis(analysis_or_hvo, self.project)
        >>> if analysis_obj is None:
        ...     raise ValueError(f"Analysis not found: {analysis_or_hvo}")
    """
    return resolve_object(analysis_or_hvo, project)


__all__ = [
    'resolve_object',
    'resolve_text',
    'resolve_paragraph',
    'resolve_segment',
    'resolve_wordform',
    'resolve_analysis',
]

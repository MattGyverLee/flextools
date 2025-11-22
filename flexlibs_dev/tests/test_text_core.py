"""
Unit tests for Core Text Operations (Cluster 1.1)

Tests for the TextCoreOperations class, covering all 8 core text methods.

Author: FlexTools Development Team
Date: 2025-11-22
"""

import pytest
from unittest.mock import Mock, MagicMock, patch
import sys
import os

# Add parent directory to path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from text_ops.text_core import TextCoreOperations


@pytest.fixture
def mock_project():
    """Create a mock FLEx project for testing."""
    project = Mock()
    project.DefaultAnalysisWs = 1  # Mock writing system handle
    project.LangProject = Mock()
    project.LangProject.TextsOC = Mock()
    return project


@pytest.fixture
def text_ops(mock_project):
    """Create a TextCoreOperations instance with mock project."""
    return TextCoreOperations(mock_project)


class TestTextCreate:
    """Tests for text_create method."""

    def test_text_create_simple(self, text_ops):
        """Test creating a text with just a name."""
        # Currently raises NotImplementedError until FLEx API is integrated
        with pytest.raises(NotImplementedError):
            text_ops.text_create("Story 1")

    def test_text_create_with_genre(self, text_ops):
        """Test creating a text with a genre."""
        with pytest.raises(NotImplementedError):
            text_ops.text_create("Story 1", genre="Narrative")

    def test_text_create_duplicate_raises_error(self, text_ops):
        """Test that creating a duplicate text raises ValueError."""
        # This will be implemented when FLEx API is integrated
        # For now, it raises NotImplementedError first
        with pytest.raises((ValueError, NotImplementedError)):
            text_ops.text_create("Duplicate")


class TestTextDelete:
    """Tests for text_delete method."""

    def test_text_delete(self, text_ops):
        """Test deleting a text."""
        mock_text = Mock()
        with pytest.raises(NotImplementedError):
            text_ops.text_delete(mock_text)

    def test_text_delete_by_hvo(self, text_ops):
        """Test deleting a text by HVO."""
        with pytest.raises(NotImplementedError):
            text_ops.text_delete(12345)

    def test_text_delete_nonexistent_raises_error(self, text_ops):
        """Test that deleting a non-existent text raises ValueError."""
        # Will be implemented when FLEx API is integrated
        with pytest.raises((ValueError, NotImplementedError)):
            text_ops.text_delete(99999)


class TestTextExists:
    """Tests for text_exists method."""

    def test_text_exists_true(self, text_ops):
        """Test checking if an existing text exists."""
        with pytest.raises(NotImplementedError):
            text_ops.text_exists("Existing Text")

    def test_text_exists_false(self, text_ops):
        """Test checking if a non-existent text exists."""
        with pytest.raises(NotImplementedError):
            text_ops.text_exists("Non-existent Text")


class TestTextGetAll:
    """Tests for text_get_all method."""

    def test_text_get_all(self, text_ops):
        """Test getting all texts."""
        # The method is a generator, so we can create it
        gen = text_ops.text_get_all()
        # But iterating over it will raise NotImplementedError
        with pytest.raises(NotImplementedError):
            list(gen)

    def test_text_get_all_empty(self, text_ops):
        """Test getting all texts when no texts exist."""
        gen = text_ops.text_get_all()
        with pytest.raises(NotImplementedError):
            list(gen)


class TestTextGetSetName:
    """Tests for text_get_name and text_set_name methods."""

    def test_text_get_name(self, text_ops):
        """Test getting the name of a text."""
        mock_text = Mock()
        with pytest.raises(NotImplementedError):
            text_ops.text_get_name(mock_text)

    def test_text_get_name_with_ws(self, text_ops):
        """Test getting the name with a specific writing system."""
        mock_text = Mock()
        with pytest.raises(NotImplementedError):
            text_ops.text_get_name(mock_text, ws_handle=2)

    def test_text_set_name(self, text_ops):
        """Test setting the name of a text."""
        mock_text = Mock()
        with pytest.raises(NotImplementedError):
            text_ops.text_set_name(mock_text, "New Name")

    def test_text_set_name_with_ws(self, text_ops):
        """Test setting the name with a specific writing system."""
        mock_text = Mock()
        with pytest.raises(NotImplementedError):
            text_ops.text_set_name(mock_text, "New Name", ws_handle=2)


class TestTextGetSetGenre:
    """Tests for text_get_genre and text_set_genre methods."""

    def test_text_get_genre(self, text_ops):
        """Test getting the genre of a text."""
        mock_text = Mock()
        with pytest.raises(NotImplementedError):
            text_ops.text_get_genre(mock_text)

    def test_text_get_genre_no_genre(self, text_ops):
        """Test getting the genre when no genre is set."""
        mock_text = Mock()
        with pytest.raises(NotImplementedError):
            text_ops.text_get_genre(mock_text)

    def test_text_set_genre(self, text_ops):
        """Test setting the genre of a text."""
        mock_text = Mock()
        with pytest.raises(NotImplementedError):
            text_ops.text_set_genre(mock_text, "Narrative")

    def test_text_set_genre_invalid(self, text_ops):
        """Test setting an invalid genre raises ValueError."""
        mock_text = Mock()
        with pytest.raises((ValueError, NotImplementedError)):
            text_ops.text_set_genre(mock_text, "NonexistentGenre")


class TestTextOperationsIntegration:
    """Integration tests for text operations."""

    def test_text_operations_integration(self, text_ops):
        """Test a complete workflow of text operations."""
        # This test demonstrates the intended workflow
        # Once FLEx API is integrated, this will test:
        # 1. Create a text
        # 2. Verify it exists
        # 3. Get its name
        # 4. Set a genre
        # 5. Get the genre
        # 6. Delete the text
        # 7. Verify it no longer exists

        # For now, we just ensure the methods exist
        assert hasattr(text_ops, 'text_create')
        assert hasattr(text_ops, 'text_exists')
        assert hasattr(text_ops, 'text_get_name')
        assert hasattr(text_ops, 'text_set_name')
        assert hasattr(text_ops, 'text_get_genre')
        assert hasattr(text_ops, 'text_set_genre')
        assert hasattr(text_ops, 'text_delete')
        assert hasattr(text_ops, 'text_get_all')

    def test_helper_methods_exist(self, text_ops):
        """Test that helper methods are defined."""
        assert hasattr(text_ops, '_resolve_text')
        assert hasattr(text_ops, '_find_genre')


class TestHelperMethods:
    """Tests for helper methods."""

    def test_resolve_text(self, text_ops):
        """Test the _resolve_text helper method."""
        mock_text = Mock()
        with pytest.raises(NotImplementedError):
            text_ops._resolve_text(mock_text)

    def test_resolve_text_by_hvo(self, text_ops):
        """Test resolving text by HVO."""
        with pytest.raises(NotImplementedError):
            text_ops._resolve_text(12345)

    def test_find_genre(self, text_ops):
        """Test the _find_genre helper method."""
        with pytest.raises(NotImplementedError):
            text_ops._find_genre("Narrative")


# TODO: Once FLEx API is integrated, add tests for:
# - Actual text creation with FLEx database
# - Text deletion verification
# - Genre list validation
# - Writing system handling
# - Error cases with real FLEx objects
# - Transaction handling
# - Concurrent access scenarios


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

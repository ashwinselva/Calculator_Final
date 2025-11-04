"""Tests for history functionality."""
import pytest
import os
import tempfile
from app.history import History


class TestHistory:
    """Test suite for history management."""
    
    @pytest.fixture
    def clean_history(self):
        """Create a clean history instance for each test."""
        # Remove the existing history.csv file
        history_file = os.path.join(os.path.dirname(__file__), '../app/history.csv')
        if os.path.exists(history_file):
            os.remove(history_file)
        yield History()
        # Cleanup
        if os.path.exists(history_file):
            os.remove(history_file)
    
    def test_history_initialization(self, clean_history):
        """Test history initialization."""
        assert hasattr(clean_history, 'df')
        assert hasattr(clean_history, 'history_file')
        assert clean_history.df.empty
    
    def test_add_entry(self, clean_history):
        """Test adding entry to history."""
        clean_history.add_entry(5.0, 3.0, 8.0)
        assert len(clean_history.df) == 1
        assert clean_history.df.iloc[0]['a'] == 5.0
        assert clean_history.df.iloc[0]['b'] == 3.0
        assert clean_history.df.iloc[0]['Result'] == 8.0
    
    def test_add_multiple_entries(self, clean_history):
        """Test adding multiple entries."""
        clean_history.add_entry(5.0, 3.0, 8.0)
        clean_history.add_entry(10.0, 2.0, 5.0)
        clean_history.add_entry(6.0, 3.0, 2.0)
        assert len(clean_history.df) == 3
    
    def test_show_history(self, clean_history, capsys):
        """Test showing history."""
        clean_history.add_entry(5.0, 3.0, 8.0)
        clean_history.show_history()
        captured = capsys.readouterr()
        assert "Calculation history" in captured.out or "5.0" in captured.out
    
    def test_show_history_empty(self, clean_history, capsys):
        """Test showing empty history."""
        clean_history.show_history()
        captured = capsys.readouterr()
        assert "No history available" in captured.out
    
    def test_clear_history(self, clean_history):
        """Test clearing history."""
        clean_history.add_entry(5.0, 3.0, 8.0)
        assert len(clean_history.df) == 1
        clean_history.clear_history()
        assert len(clean_history.df) == 0


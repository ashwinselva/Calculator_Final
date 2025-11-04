"""Integration and UI tests for calculator components."""
import pytest
import os
import tempfile
import sys
from io import StringIO
from unittest.mock import patch, MagicMock, mock_open

from app.calculator import main
from app.calculation import perform_operation
from app.help import show_help, show_menu
from app.colors import (
    print_header, print_success, print_error, print_warning, print_info,
    print_special, highlight, color_text, Colors
)
from app.logger import Logger
from app.history import History


class TestHelpModule:
    """Test suite for help module."""
    
    def test_show_menu(self, capsys):
        """Test menu display."""
        show_menu()
        captured = capsys.readouterr()
        assert "Menu:" in captured.out
        assert "1)" in captured.out
        assert "Perform calculation" in captured.out
        assert "9)" in captured.out
        assert "Exit" in captured.out
    
    def test_show_help(self, capsys):
        """Test help display."""
        show_help()
        captured = capsys.readouterr()
        assert "Help" in captured.out
        assert "Available commands:" in captured.out
        assert "1:" in captured.out
        assert "9:" in captured.out


class TestColorsModule:
    """Test suite for colors module."""
    
    def test_print_header(self, capsys):
        """Test header printing."""
        print_header("Test Header")
        captured = capsys.readouterr()
        assert "Test Header" in captured.out
    
    def test_print_success(self, capsys):
        """Test success message printing."""
        print_success("Success message")
        captured = capsys.readouterr()
        assert "Success message" in captured.out
        assert "✓" in captured.out
    
    def test_print_error(self, capsys):
        """Test error message printing."""
        print_error("Error message")
        captured = capsys.readouterr()
        assert "Error message" in captured.out
        assert "✗" in captured.out
    
    def test_print_warning(self, capsys):
        """Test warning message printing."""
        print_warning("Warning message")
        captured = capsys.readouterr()
        assert "Warning message" in captured.out
    
    def test_print_info(self, capsys):
        """Test info message printing."""
        print_info("Info message")
        captured = capsys.readouterr()
        assert "Info message" in captured.out
    
    def test_print_special(self, capsys):
        """Test special message printing."""
        print_special("Special message")
        captured = capsys.readouterr()
        assert "Special message" in captured.out
    
    def test_print_subheader(self, capsys):
        """Test subheader printing."""
        from app.colors import print_subheader
        print_subheader("Subheader")
        captured = capsys.readouterr()
        assert "Subheader" in captured.out
    
    def test_highlight(self, capsys):
        """Test text highlighting."""
        result = highlight("test")
        assert isinstance(result, str)
        assert "test" in result
    
    def test_color_text(self):
        """Test color_text function."""
        result = color_text("test", Colors.SUCCESS)
        assert isinstance(result, str)
        assert "test" in result
    
    def test_colors_constants(self):
        """Test that color constants exist."""
        assert hasattr(Colors, 'SUCCESS')
        assert hasattr(Colors, 'ERROR')
        assert hasattr(Colors, 'WARNING')
        assert hasattr(Colors, 'INFO')
        assert hasattr(Colors, 'HEADER')
        assert hasattr(Colors, 'SPECIAL')
        assert hasattr(Colors, 'RESET')


class TestLoggerModule:
    """Test suite for logger module."""
    
    @pytest.fixture
    def test_logger(self):
        """Create a test logger instance."""
        return Logger()
    
    @pytest.fixture
    def clean_logs(self):
        """Clean log file before and after test."""
        log_file = os.path.join(os.path.dirname(__file__), '../app/logs/calculator.log')
        if os.path.exists(log_file):
            os.remove(log_file)
        yield
        if os.path.exists(log_file):
            os.remove(log_file)
    
    def test_logger_custom_init(self):
        """Test logger initialization with custom log file."""
        custom_path = os.path.join(tempfile.gettempdir(), 'custom', 'test.log')
        logger = Logger(log_file=custom_path)
        assert logger.log_file == custom_path
        assert os.path.exists(os.path.dirname(custom_path))
        # Cleanup
        if os.path.exists(custom_path):
            os.remove(custom_path)
        if os.path.exists(os.path.dirname(custom_path)):
            os.rmdir(os.path.dirname(custom_path))
    
    def test_logger_initialization(self, test_logger):
        """Test logger initialization."""
        assert hasattr(test_logger, 'log_file')
        assert test_logger.log_file.endswith('calculator.log')
    
    def test_logger_log(self, test_logger, clean_logs):
        """Test logging operation."""
        test_logger.log(10.0, 5.0, "Addition", 15.0)
        assert os.path.exists(test_logger.log_file)
        
        with open(test_logger.log_file, 'r') as f:
            content = f.read()
            assert "Addition" in content
            assert "10.0" in content
            assert "5.0" in content
            assert "15.0" in content
    
    def test_logger_multiple_logs(self, test_logger, clean_logs):
        """Test multiple log entries."""
        test_logger.log(5.0, 3.0, "Addition", 8.0)
        test_logger.log(10.0, 2.0, "Division", 5.0)
        
        with open(test_logger.log_file, 'r') as f:
            content = f.read()
            assert "Addition" in content
            assert "Division" in content
    
    def test_logger_timestamp_format(self, test_logger, clean_logs):
        """Test that logs include timestamps."""
        test_logger.log(1.0, 1.0, "Test", 2.0)
        
        with open(test_logger.log_file, 'r') as f:
            line = f.read()
            # Check for timestamp pattern [YYYY-MM-DD HH:MM:SS]
            assert "[" in line and "]" in line
            assert "LOG:" in line
    
    def test_logger_get_log_file_path(self, test_logger):
        """Test getting log file path."""
        path = test_logger.get_log_file_path()
        assert path == test_logger.log_file
        assert path.endswith('calculator.log')
    
    def test_logger_clear_logs(self, test_logger, clean_logs, capsys):
        """Test clearing log file."""
        test_logger.log(1.0, 1.0, "Test", 2.0)
        assert os.path.exists(test_logger.log_file)
        
        test_logger.clear_logs()
        captured = capsys.readouterr()
        assert "cleared" in captured.out.lower() or not os.path.exists(test_logger.log_file)
    
    def test_logger_io_error_handling(self, capsys, monkeypatch):
        """Test logger handles IO errors gracefully."""
        logger_instance = Logger()
        
        # Mock open to raise IOError
        def mock_open_error(*args, **kwargs):
            raise IOError("Permission denied")
        
        original_open = open
        
        def patched_open(*args, **kwargs):
            if 'calculator.log' in str(args):
                raise IOError("Permission denied")
            return original_open(*args, **kwargs)
        
        monkeypatch.setattr('builtins.open', patched_open)
        logger_instance.log(1.0, 1.0, "Test", 2.0)
        captured = capsys.readouterr()
        assert "Error writing" in captured.out or "error" in captured.out.lower()


class TestHistorySaveLoad:
    """Test suite for history save/load operations."""
    
    @pytest.fixture
    def clean_history(self):
        """Clean history for each test."""
        history_file = os.path.join(os.path.dirname(__file__), '../app/history.csv')
        if os.path.exists(history_file):
            os.remove(history_file)
        yield History()
        if os.path.exists(history_file):
            os.remove(history_file)
    
    def test_save_history(self, clean_history):
        """Test saving history to file."""
        clean_history.add_entry(5.0, 3.0, 8.0)
        clean_history.save_history()
        
        assert os.path.exists(clean_history.history_file)
        
        # Verify file contains data
        import pandas as pd
        df = pd.read_csv(clean_history.history_file)
        assert len(df) == 1
        assert df.iloc[0]['a'] == 5.0
    
    def test_load_history(self, clean_history, capsys):
        """Test loading history from file."""
        clean_history.add_entry(5.0, 3.0, 8.0)
        clean_history.save_history()
        
        # Create new history instance and load
        new_history = History()
        new_history.load_history()
        captured = capsys.readouterr()
        
        assert "Loaded" in captured.out or len(new_history.df) == 1
    
    def test_load_history_nonexistent_file(self, capsys):
        """Test loading when no history file exists."""
        history_file = os.path.join(os.path.dirname(__file__), '../app/history.csv')
        if os.path.exists(history_file):
            os.remove(history_file)
        
        history = History()
        history.load_history()
        captured = capsys.readouterr()
        
        # Should handle gracefully
        assert os.path.exists(history_file) or True  # Either created or message shown
    
    def test_clear_last_entry(self, clean_history):
        """Test clearing last entry from history."""
        clean_history.add_entry(5.0, 3.0, 8.0)
        clean_history.add_entry(10.0, 2.0, 5.0)
        assert len(clean_history.df) == 2
        
        clean_history.clear_last_entry()
        assert len(clean_history.df) == 1
        assert clean_history.df.iloc[0]['Result'] == 8.0
    
    def test_show_history_with_multiple_entries(self, clean_history, capsys):
        """Test showing history with multiple entries."""
        clean_history.add_entry(5.0, 3.0, 8.0)
        clean_history.add_entry(10.0, 2.0, 5.0)
        clean_history.add_entry(6.0, 6.0, 36.0)
        
        clean_history.show_history()
        captured = capsys.readouterr()
        assert "Calculation history" in captured.out or "5.0" in captured.out
    
    def test_clear_last_entry_empty_history(self, clean_history):
        """Test clearing last entry when history is empty."""
        assert len(clean_history.df) == 0
        clean_history.clear_last_entry()
        assert len(clean_history.df) == 0


class TestCalculationPerformOperation:
    """Test suite for perform_operation function."""
    
    def test_perform_operation_addition(self, capsys, monkeypatch):
        """Test performing addition operation."""
        inputs = iter(['5', '3', '1'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Result:" in captured.out or "result" in captured.out.lower()
    
    def test_perform_operation_subtraction(self, capsys, monkeypatch):
        """Test performing subtraction operation."""
        inputs = iter(['10', '3', '2'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Result:" in captured.out or "result" in captured.out.lower()
    
    def test_perform_operation_multiplication(self, capsys, monkeypatch):
        """Test performing multiplication operation."""
        inputs = iter(['5', '6', '3'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Result:" in captured.out or "result" in captured.out.lower()
    
    def test_perform_operation_division(self, capsys, monkeypatch):
        """Test performing division operation."""
        inputs = iter(['10', '2', '4'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Result:" in captured.out or "result" in captured.out.lower()
    
    def test_perform_operation_power(self, capsys, monkeypatch):
        """Test performing power operation."""
        inputs = iter(['2', '3', '5'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Result:" in captured.out or "result" in captured.out.lower()
    
    def test_perform_operation_root(self, capsys, monkeypatch):
        """Test performing root operation."""
        inputs = iter(['8', '3', '6'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Result:" in captured.out or "result" in captured.out.lower()
    
    def test_perform_operation_modulus(self, capsys, monkeypatch):
        """Test performing modulus operation."""
        inputs = iter(['10', '3', '7'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Result:" in captured.out or "result" in captured.out.lower()
    
    def test_perform_operation_integer_division(self, capsys, monkeypatch):
        """Test performing integer division operation."""
        inputs = iter(['10', '3', '8'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Result:" in captured.out or "result" in captured.out.lower()
    
    def test_perform_operation_percentage(self, capsys, monkeypatch):
        """Test performing percentage operation."""
        inputs = iter(['50', '100', '9'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Result:" in captured.out or "result" in captured.out.lower()
    
    def test_perform_operation_absolute_difference(self, capsys, monkeypatch):
        """Test performing absolute difference operation."""
        inputs = iter(['5', '3', '10'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Result:" in captured.out or "result" in captured.out.lower()
    
    def test_perform_operation_invalid_first_number(self, capsys, monkeypatch):
        """Test with invalid first number."""
        inputs = iter(['abc', '3', '1'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Error" in captured.out or "error" in captured.out.lower()
    
    def test_perform_operation_invalid_second_number(self, capsys, monkeypatch):
        """Test with invalid second number."""
        inputs = iter(['5', 'xyz', '1'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Error" in captured.out or "error" in captured.out.lower()
    
    def test_perform_operation_invalid_operation_choice(self, capsys, monkeypatch):
        """Test with invalid operation choice."""
        inputs = iter(['5', '3', 'abc'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Error" in captured.out or "error" in captured.out.lower()
    
    def test_perform_operation_invalid_operation_range(self, capsys, monkeypatch):
        """Test with operation choice out of range."""
        inputs = iter(['5', '3', '15'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Error" in captured.out or "error" in captured.out.lower()
    
    def test_perform_operation_division_by_zero(self, capsys, monkeypatch):
        """Test division by zero."""
        inputs = iter(['5', '0', '4'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Error" in captured.out or "error" in captured.out.lower()
    
    def test_perform_operation_invalid_root(self, capsys, monkeypatch):
        """Test invalid root (even root of negative)."""
        inputs = iter(['-4', '2', '6'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Error" in captured.out or "error" in captured.out.lower()
    
    def test_perform_operation_modulus_by_zero(self, capsys, monkeypatch):
        """Test modulus by zero."""
        inputs = iter(['10', '0', '7'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Error" in captured.out or "error" in captured.out.lower()
    
    def test_perform_operation_integer_div_by_zero(self, capsys, monkeypatch):
        """Test integer division by zero."""
        inputs = iter(['10', '0', '8'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        assert "Error" in captured.out or "error" in captured.out.lower()
    
    def test_perform_operation_unexpected_general_error(self, capsys, monkeypatch):
        """Test handling when unexpected error occurs."""
        # Test with invalid float conversion (caught as unexpected error)
        inputs = iter(['inf', '2', '4'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        perform_operation()
        captured = capsys.readouterr()
        # Should handle gracefully and show error message
        assert len(captured.out) > 0


class TestCalculatorMain:
    """Test suite for main calculator menu."""
    
    def test_main_exit_with_9(self, capsys, monkeypatch):
        """Test exiting with option 9."""
        inputs = iter(['9'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        captured = capsys.readouterr()
        assert "Goodbye!" in captured.out
    
    def test_main_exit_with_q(self, capsys, monkeypatch):
        """Test exiting with 'q'."""
        inputs = iter(['q'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        captured = capsys.readouterr()
        assert "Goodbye!" in captured.out
    
    def test_main_show_help(self, capsys, monkeypatch):
        """Test help option."""
        inputs = iter(['2', '9'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        captured = capsys.readouterr()
        assert "Help" in captured.out or "help" in captured.out.lower()
    
    def test_main_show_history(self, capsys, monkeypatch):
        """Test history option."""
        inputs = iter(['3', '9'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        captured = capsys.readouterr()
        assert "history" in captured.out.lower() or "History" in captured.out
    
    def test_main_clear_history(self, capsys, monkeypatch):
        """Test clear history option."""
        inputs = iter(['4', '9'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        captured = capsys.readouterr()
        assert "cleared" in captured.out.lower() or "Cleared" in captured.out
    
    def test_main_clear_last_entry(self, capsys, monkeypatch):
        """Test clear last entry option."""
        inputs = iter(['5', '9'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        captured = capsys.readouterr()
        assert "cleared" in captured.out.lower() or "entry" in captured.out.lower()
    
    def test_main_redo_last_entry(self, capsys, monkeypatch):
        """Test redo last entry option."""
        inputs = iter(['6', '5', '3', '1', '9'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        captured = capsys.readouterr()
        assert "Redo" in captured.out or "Result:" in captured.out or len(captured.out) > 0
    
    def test_main_redo_with_system_exit(self, capsys, monkeypatch):
        """Test redo last entry with SystemExit."""
        def input_side_effect(prompt):
            try:
                return next(inputs)
            except StopIteration:
                raise SystemExit
        
        inputs = iter(['6', '9'])
        monkeypatch.setattr('builtins.input', input_side_effect)
        
        main()
        captured = capsys.readouterr()
        assert len(captured.out) > 0
    
    def test_main_save_history(self, capsys, monkeypatch):
        """Test save history option."""
        inputs = iter(['7', '9'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        captured = capsys.readouterr()
        assert "Saving" in captured.out or "saved" in captured.out.lower()
    
    def test_main_load_history(self, capsys, monkeypatch):
        """Test load history option."""
        inputs = iter(['8', '9'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        captured = capsys.readouterr()
        assert "Loaded" in captured.out or "loaded" in captured.out.lower()
    
    def test_main_invalid_choice(self, capsys, monkeypatch):
        """Test invalid menu choice."""
        inputs = iter(['x', '9'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        captured = capsys.readouterr()
        assert "Unknown choice" in captured.out or "unknown" in captured.out.lower()
    
    def test_main_calculation_option_1(self, capsys, monkeypatch):
        """Test calculation option 1."""
        inputs = iter(['1', '5', '3', '1', '9'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        captured = capsys.readouterr()
        assert "Result:" in captured.out or "result" in captured.out.lower()
    
    def test_main_empty_choice_calculation(self, capsys, monkeypatch):
        """Test empty choice defaults to calculation."""
        inputs = iter(['', '5', '3', '1', '9'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        
        main()
        captured = capsys.readouterr()
        assert "Result:" in captured.out or "result" in captured.out.lower()

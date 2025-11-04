import os
from datetime import datetime


class Logger:
    def __init__(self, log_file: str = None):
        """Initialize logger with optional file path."""
        if log_file is None:
            # Default to logs directory in the app folder
            log_dir = os.path.join(os.path.dirname(__file__), "logs")
            os.makedirs(log_dir, exist_ok=True)
            self.log_file = os.path.join(log_dir, "calculator.log")
        else:
            self.log_file = log_file
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    def log(self, a: float, b: float, operation: str, result: float) -> None:
        """Log a calculation to both console and file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"[{timestamp}] LOG: Performed {operation} on {a} and {b} with result {result}"
        
        # Print to console
        print(message)
        
        # Write to file
        try:
            with open(self.log_file, 'a') as f:
                f.write(message + "\n")
        except IOError as e:
            print(f"Error writing to log file: {e}")
    
    def get_log_file_path(self) -> str:
        """Return the path to the log file."""
        return self.log_file
    
    def clear_logs(self) -> None:
        """Clear all log entries."""
        try:
            if os.path.exists(self.log_file):
                os.remove(self.log_file)
                print(f"Log file cleared: {self.log_file}")
        except IOError as e:
            print(f"Error clearing log file: {e}")

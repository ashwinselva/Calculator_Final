import pandas as pd
import os
from .colors import print_info, print_warning, Colors


df = pd.DataFrame(columns=["a","b", "Result"])

class History:
    def __init__(self):
        self.history_file = os.path.join(os.path.dirname(__file__), "history.csv")
        
        if os.path.exists(self.history_file):
            try:
                self.df = pd.read_csv(self.history_file)
            except pd.errors.EmptyDataError:
                self.df = pd.DataFrame(columns=["a","b", "Result"])
        else:
            self.df = pd.DataFrame(columns=["a","b", "Result"])
            self.df.to_csv(self.history_file, index=False)

    def add_entry(self, a: float, b: float, result: float) -> None:
        new_entry = {"a": a, "b": b, "Result": result}
        self.df = pd.concat([self.df, pd.DataFrame([new_entry])], ignore_index=True)
        self.df.to_csv(self.history_file, index=False)

    def show_history(self) -> None:
        if self.df.empty:
            print_warning("\nNo history available.")
            return
        print_info("\nCalculation history:")
        # Display header with color
        header_str = f"{Colors.HEADER}  a         b         Result{Colors.RESET}"
        print(header_str)
        print(f"{Colors.INFO}" + "-" * 30 + f"{Colors.RESET}")
        # Display each row
        for idx, row in self.df.iterrows():
            print(f"{Colors.SUCCESS}{row['a']:>6.2f}    {row['b']:>6.2f}    {row['Result']:>8.2f}{Colors.RESET}")
    
    def clear_history(self) -> None:
        self.df = self.df.iloc[0:0]
        self.df.to_csv(self.history_file, index=False)

    def clear_last_entry(self) -> None:
        if not self.df.empty:
            self.df = self.df[:-1]
            self.df.to_csv(self.history_file, index=False)

    
    def save_history(self) -> None:
        self.df.to_csv(self.history_file, index=False)

    def load_history(self) -> None:
        if os.path.exists(self.history_file):
            try:
                self.df = pd.read_csv(self.history_file)
                print_info(f"✓ Loaded {len(self.df)} entries from history")
            except pd.errors.EmptyDataError:
                self.df = pd.DataFrame(columns=["a","b", "Result"])
                print_warning("History file is empty")
        else:
            self.df = pd.DataFrame(columns=["a","b", "Result"])
            self.df.to_csv(self.history_file, index=False)
            print_warning("No history file found, created new one")
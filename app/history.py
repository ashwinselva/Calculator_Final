import pandas as pd
import os



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
            print("\nNo history available.")
            return
        print("\nCalculation history:")
        print(self.df)
    
    def clear_history(self) -> None:
        self.df = self.df.iloc[0:0]



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
            except pd.errors.EmptyDataError:
                self.df = pd.DataFrame(columns=["a","b", "Result"])
        else:
            self.df = pd.DataFrame(columns=["a","b", "Result"])
            self.df.to_csv(self.history_file, index=False)
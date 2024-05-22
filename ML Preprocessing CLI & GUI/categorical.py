import tkinter as tk
from tkinter import simpledialog, messagebox
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from data_description import DataDescription

class Categorical:
    tasks = [
        'Show Categorical Columns',
        'Perform One Hot encoding',
        
    ]

    def __init__(self, data):
        self.data = data

    def show_categorical_columns(self):
        categorical_columns = self.data.select_dtypes(include="object")
        messagebox.showinfo("Categorical Columns", f"Categorical Columns:\n{', '.join(categorical_columns)}")

    def encoding(self):
        column = simpledialog.askstring("One Hot Encoding", "Enter column name to one hot encode (Press -1 to go back):")
        if column == "-1":
            return
        if column not in self.data.columns:
            messagebox.showerror("Error", "Column not found!")
            return
        if self.data[column].dtype != 'object':
            messagebox.showerror("Error", "Column is not categorical!")
            return
        
        encoded_data = pd.get_dummies(self.data[column], prefix=column)
        self.data = pd.concat([self.data, encoded_data], axis=1)
        self.data.drop(columns=[column], inplace=True)
        messagebox.showinfo("Success", "One Hot Encoding done!")

    def execute(self):
        while True:
            choice = simpledialog.askinteger("Categorical Tasks", "\n".join([
                f"{idx}. {task}" for idx, task in enumerate(self.tasks, start=1)
            ]) + "\nEnter your choice (Press -1 to exit):")

            if choice is None or choice == -1:
                break

            if choice == 1:
                self.show_categorical_columns()
            elif choice == 2:
                self.encoding()
            else:
                messagebox.showerror("Error", "Invalid choice!")

        return self.data

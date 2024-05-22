import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd
from data_description import DataDescription

class Imputation:
    def __init__(self, data):
        self.data = data

    def show_columns(self):
        columns = ", ".join(self.data.columns)
        messagebox.showinfo("Columns", f"Columns: {columns}")

    def print_null_values(self):
        null_values = {column: sum(self.data[column].isnull()) for column in self.data.columns}
        null_values_str = "\n".join(f"{column}: {count}" for column, count in null_values.items())
        messagebox.showinfo("Null Values", f"Null Values:\n{null_values_str}")

    def remove_column(self):
        column = simpledialog.askstring("Remove Column", "Enter column(s) to remove (comma-separated):")
        if column:
            columns_to_remove = [col.strip() for col in column.split(",")]
            try:
                self.data.drop(columns_to_remove, axis=1, inplace=True)
                messagebox.showinfo("Success", "Columns removed successfully!")
            except KeyError as e:
                messagebox.showerror("Error", f"Column(s) not found: {', '.join(str(e) for e in e.args)}")

    def fill_null_with_mean(self):
        column = simpledialog.askstring("Fill Null with Mean", "Enter column name:")
        if column:
            try:
                self.data[column].fillna(self.data[column].mean(), inplace=True)
                messagebox.showinfo("Success", f"Null values in column '{column}' filled with mean!")
            except KeyError:
                messagebox.showerror("Error", f"Column '{column}' not found!")

    def fill_null_with_median(self):
        column = simpledialog.askstring("Fill Null with Median", "Enter column name:")
        if column:
            try:
                self.data[column].fillna(self.data[column].median(), inplace=True)
                messagebox.showinfo("Success", f"Null values in column '{column}' filled with median!")
            except KeyError:
                messagebox.showerror("Error", f"Column '{column}' not found!")

    def fill_null_with_mode(self):
        column = simpledialog.askstring("Fill Null with Mode", "Enter column name:")
        if column:
            try:
                self.data[column].fillna(self.data[column].mode()[0], inplace=True)
                messagebox.showinfo("Success", f"Null values in column '{column}' filled with mode!")
            except KeyError:
                messagebox.showerror("Error", f"Column '{column}' not found!")

    def execute(self):
        tasks = {
            1: self.print_null_values,
            2: self.remove_column,
            3: self.fill_null_with_mean,
            4: self.fill_null_with_median,
            5: self.fill_null_with_mode,
            # Add more tasks here if needed
        }

        while True:
            choice = simpledialog.askinteger("Imputation Tasks", "\n".join([
                "1. Show number of Null Values",
                "2. Remove Columns",
                "3. Fill Null Values (with mean)",
                "4. Fill Null Values (with median)",
                "5. Fill Null Values (with mode)",
                "Enter your choice (Press -1 to exit):"
            ]))

            if choice is None or choice == -1:
                break

            task = tasks.get(choice)
            if task:
                task()
                if choice != 5:
                    DataDescription(self.data)
            else:
                messagebox.showerror("Error", "Invalid choice!")

        return self.data

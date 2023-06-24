import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
import os
import csv
from datetime import datetime


class CSVAnalyzer:
    def __init__(self):
        self.file_path = None

    def check_if_file_correct(self):
        while True:
            try:
                self.file_path = self.get_path()
                self.is_csv_file(self.file_path)
                with open(self.file_path, 'r', encoding='utf-8') as csvfile:
                    csv.reader(csvfile, delimiter=',')
                    break
            except (FileNotFoundError, TypeError) as e:
                # Error handled already
                pass

    @staticmethod
    def is_csv_file(file_path):
        file_name, file_extension = os.path.splitext(file_path)
        if not file_path:
            messagebox.showerror("Error", "No file selected")
            raise FileNotFoundError("No file selected")
        if file_extension.lower() != '.csv':
            messagebox.showerror("Error", "Wrong file type")
            raise TypeError("Wrong file type")

    @staticmethod
    def get_path():
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path

    @staticmethod
    def min_max_val(column_values):
        max_val = max(column_values)
        min_val = min(column_values)
        col_range = f"{min_val}#{max_val}"
        return col_range

    def get_column_range(self, column_values):
        column_type = self.get_column_type(column_values[0], column_values)

        if column_type == str:
            col_range = "Not applicable#Not applicable"

        elif column_type == int:
            # Just in case of such lists: ['0', '0', '0', '0,45', '0,2', '0', '0', '0,2', '0,2', '0']
            column_values = [float(value.replace(',', '.')) for value in column_values]
            column_values = list(map(int, column_values))
            col_range = self.min_max_val(column_values)

        elif column_type == float:
            column_values = [float(value.replace(',', '.')) for value in column_values]
            column_values = list(map(float, column_values))
            col_range = self.min_max_val(column_values)

        elif column_type == datetime:
            column_values = [datetime.strptime(value, "%d.%m.%Y") for value in column_values]
            if column_values:
                col_range = self.min_max_val(column_values)

        elif column_type == bool:
            col_range = self.min_max_val(column_values)

        else:
            col_range = "Not applicable#Not applicable"

        return col_range

    @staticmethod
    def get_column_type(value, column_values):
        try:
            datetime_obj = datetime.strptime(value, '%d.%m.%Y')
            return type(datetime_obj)
        except ValueError:
            pass

        if all(value.isdigit() or value.lstrip('-').isdigit() for value in column_values):
            return int
        else:
            try:
                if all(isinstance(float(value.replace(',', '.')), float) for value in column_values):
                    return float
            except ValueError:
                pass

        if value.lower() in ['true', 'false']:
            return bool

        else:
            return str

    def describe_file(self):
        self.check_if_file_correct()
        with open(self.file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            rows = list(reader)
            column_names = rows[0]
            data_rows = rows[1:]

            columns = []
            for col_index, col_name in enumerate(column_names):
                column_values = [row[col_index] for row in data_rows]
                col_type = self.get_column_type(column_values[0], column_values)
                col_example = column_values[0]
                col_range = self.get_column_range(column_values)
                col_range_from, col_range_to = col_range.split('#')
                columns.append((col_name, col_type, col_example, col_range_from, col_range_to))

            return columns

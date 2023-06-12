import tkinter as tk
from tkinter import filedialog
import os
import csv
from datetime import datetime


def is_csv_file(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    if not file_path:
        raise FileNotFoundError("No file selected")
    if file_extension.lower() != '.csv':
        raise TypeError("Wrong file type")


def check_if_file_correct():
    while True:
        try:
            file_path = get_path()
            is_csv_file(file_path)
            with open(file_path, 'r') as csvfile:
                csv.reader(csvfile, delimiter=',')
                break
        except (FileNotFoundError, TypeError) as e:
            print(f"{e}")
    return file_path


def get_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


def get_column_range(column_values):
    column_type = get_column_type(column_values[0])

    if column_type in (float, int, bool):
        max_val = max(column_values)
        min_val = min(column_values)
        col_range = f"{min_val}:{max_val}"
    else:
        col_range = "Not applicable:Not applicable"

    return col_range


def get_column_type(value):
    try:
        datetime_obj = datetime.strptime(value, '%d.%m.%Y')
        return type(datetime_obj)
    except ValueError:
        pass
    if '.' in value or ',' in value:
        try:
            float(value.replace(',', '.'))
            return float
        except ValueError:
            pass
    elif value.isdigit():
        return int
    elif value.lower() in ['true', 'false']:
        return bool
    else:
        return str


def show_file(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        rows = list(reader)
        column_names = rows[0]
        data_rows = rows[1:]

        columns = []

        for col_index, col_name in enumerate(column_names):
            column_values = [row[col_index] for row in data_rows]
            col_type = get_column_type(column_values[0])
            col_example = column_values[0]
            col_range = get_column_range(column_values)
            col_range_from, col_range_to = col_range.split(':')
            columns.append((col_name, col_type, col_example, col_range_from, col_range_to))

        print(column_names)
        print(columns)

        return columns
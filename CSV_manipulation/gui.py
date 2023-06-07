import tkinter as tk
from tkinter import ttk
import datetime


def create_gui(columns):
    root = tk.Tk()
    root.title("AnoData")
    root.geometry("400x800")

    # Ramka do przewijania
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Tworzenie ramki wewnątrz obszaru przewijania
    scrollable_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    for i, (column_name, column_type, column_example) in enumerate(columns):
        frame = ttk.LabelFrame(scrollable_frame, text=column_name)
        frame.pack(padx=15, pady=15, fill="x")

        # Example
        ttk.Label(frame, text="Example:").grid(row=1, column=0, sticky="w")
        ttk.Label(frame, text=column_example).grid(row=1, column=1, sticky="w")

        # Data Range
        ttk.Label(frame, text="Data Range:").grid(row=2, column=0, sticky="w")
        data_range_entry = ttk.Entry(frame)
        data_range_entry.grid(row=2, column=1, sticky="w")

        # Data Type
        ttk.Label(frame, text="Data Type:").grid(row=3, column=0, sticky="w")
        data_type_var = tk.StringVar(value=str(column_type))
        data_type_var.set(column_type)

        data_type_values = ["Int", "Float", "Date", "String", "Geo", "Bool"]
        if column_type == int:
            data_type_var.set("Int")
        elif column_type == float:
            data_type_var.set("Float")
        elif column_type == datetime.datetime:
            data_type_var.set("Date")
        elif column_type == str:
            data_type_var.set("String")
        elif column_type == bool:
            data_type_var.set("Bool")

        data_type_dropdown = ttk.Combobox(frame, values=data_type_values, textvariable=data_type_var, state="readonly")
        data_type_dropdown.current(data_type_values.index(data_type_var.get()))
        data_type_dropdown.grid(row=3, column=1, sticky="w")

        # Modification
        ttk.Label(frame, text="Modification:").grid(row=4, column=0, sticky="w")
        modification_entry = ttk.Entry(frame)
        modification_entry.grid(row=4, column=1, sticky="w")

    # Konfiguracja przewijania
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    root.mainloop()

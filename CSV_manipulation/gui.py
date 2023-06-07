import tkinter as tk
from tkinter import ttk
import datetime


def create_gui(columns):
    root = tk.Tk()
    root.title("AnoData")
    root.geometry("400x800")

    # Frame to scroll
    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    scrollable_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Go through list of tuples to fill in boxes
    for i, (column_name, column_type, column_example, column_range) in enumerate(columns):
        frame = ttk.LabelFrame(scrollable_frame, text=str(i+1) + ". " + column_name)
        frame.pack(padx=15, pady=15, fill="x")

        # Example section
        ttk.Label(frame, text="Example:").grid(row=1, column=0, sticky="w")
        ttk.Label(frame, text=column_example).grid(row=1, column=1, sticky="w")

        # Data Range section
        ttk.Label(frame, text="Data Range:").grid(row=2, column=0, sticky="w")
        data_range_entry = ttk.Entry(frame)
        data_range_entry.grid(row=2, column=1, sticky="w")

        # Set default value for Data Range
        data_range_entry.insert(tk.END, column_range)

        # Data Type section with pre-set value
        ttk.Label(frame, text="Data Type:").grid(row=3, column=0, sticky="w")
        data_type_var = tk.StringVar(value=str(column_type))

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

        data_type_values = ["Int", "Float", "Date", "String", "Geo", "Bool"]
        data_type_dropdown = ttk.Combobox(frame, values=data_type_values, textvariable=data_type_var, state="readonly")
        data_type_dropdown.current(data_type_values.index(data_type_var.get()))
        data_type_dropdown.grid(row=3, column=1, sticky="w")

        # Modification section
        ttk.Label(frame, text="Modification:").grid(row=4, column=0, sticky="w")
        modification_entry = ttk.Entry(frame)
        modification_entry.grid(row=4, column=1, sticky="w")

        modification_values = ["Remain as is", "Draw from existing values", "Draw from given values"]
        modification_var = tk.StringVar()
        modification_dropdown = ttk.Combobox(frame, values=modification_values, textvariable=modification_var, state="readonly")
        modification_dropdown.grid(row=4, column=1, sticky="w")

        modification_dropdown.current(modification_values.index("Remain as is"))  # Ustawienie wartości domyślnej

    # Konfiguracja przewijania
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    root.mainloop()

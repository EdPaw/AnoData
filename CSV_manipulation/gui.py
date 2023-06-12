import tkinter as tk
from tkinter import ttk
import datetime
import csv_process as csv_p


def get_user_choices(columns, entries, dropdowns):
    user_choices = []  # List storing user choices

    # Collect user choices for each column
    for i, (column_name, column_type, _, _, _) in enumerate(columns):
        data_range_from = entries[i][0].get()
        data_range_to = entries[i][1].get()
        data_type = dropdowns[i][0].get()
        modification = dropdowns[i][1].get()

        user_choices.append((column_name, data_type, data_range_from, data_range_to, modification))
        #print(user_choices)

        mod_data = csv_p.process_data(user_choices)
        csv_p.create_new_csv(mod_data)

    return user_choices


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

    entries = []  # List saving Entry fields
    dropdowns = []  # Lista saving Combobox fields

    # Go through list of tuples to fill in boxes
    for i, (column_name, column_type, column_example, column_range_from, column_range_to) in enumerate(columns):
        frame = ttk.LabelFrame(scrollable_frame, text=str(i + 1) + ". " + column_name)
        frame.pack(padx=15, pady=15, fill="x")

        # Example section
        ttk.Label(frame, text="Example:").grid(row=1, column=0, sticky="w")
        ttk.Label(frame, text=column_example).grid(row=1, column=1, sticky="w")

        # Data Range From section
        ttk.Label(frame, text="Data Range From:").grid(row=2, column=0, sticky="w")
        data_range_from_entry = ttk.Entry(frame)
        data_range_from_entry.grid(row=2, column=1, sticky="w")

        # Set default value for Data Range From
        data_range_from_entry.insert(tk.END, column_range_from)

        # Data Range To section
        ttk.Label(frame, text="Data Range To:").grid(row=3, column=0, sticky="w")
        data_range_to_entry = ttk.Entry(frame)
        data_range_to_entry.grid(row=3, column=1, sticky="w")

        # Set default value for Data Range To
        data_range_to_entry.insert(tk.END, column_range_to)

        # Data Type section with pre-set value
        ttk.Label(frame, text="Data Type:").grid(row=4, column=0, sticky="w")
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
        data_type_dropdown.grid(row=4, column=1, sticky="w")

        # Modification section
        ttk.Label(frame, text="Modification:").grid(row=5, column=0, sticky="w")
        modification_entry = ttk.Entry(frame)
        modification_entry.grid(row=5, column=1, sticky="w")

        modification_values = ["Remain as is", "Draw from data range"]
        modification_var = tk.StringVar()
        modification_dropdown = ttk.Combobox(frame, values=modification_values, textvariable=modification_var,
                                             state="readonly")
        modification_dropdown.grid(row=5, column=1, sticky="w")

        modification_dropdown.current(modification_values.index("Remain as is"))  # Set default value

        entries.append((data_range_from_entry, data_range_to_entry))
        dropdowns.append((data_type_dropdown, modification_dropdown))

    # Generate Button
    generate_button = ttk.Button(scrollable_frame, text="Generate",
                                 command=lambda: get_user_choices(columns, entries, dropdowns))
    generate_button.pack(pady=15)

    # Result
    result_label = ttk.Label(root, text="")
    result_label.pack()

    root.mainloop()



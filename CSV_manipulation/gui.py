import tkinter as tk
from tkinter import ttk
import datetime
import csv_process as csv_p
import csv_entry as csv_e


class StartScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AnoData")
        self.root.geometry("400x300")

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        image = tk.PhotoImage(file="background.png", master=self.canvas)
        self.canvas.create_image(0, 0, anchor="nw", image=image)

        # Calculate the center coordinates of the canvas
        canvas_center_x = 400 // 2
        canvas_center_y = 300 // 2

        # Add "Select CSV" button
        select_csv_button = ttk.Button(self.root, text="Select CSV", command=self.handle_select_csv)
        select_csv_button.place(x=canvas_center_x, y=canvas_center_y, anchor="center")

        self.analyzer = None
        self.columns = None
        self.path = None

        self.root.mainloop()

    def handle_select_csv(self):
        self.analyzer = csv_e.CSVAnalyzer()
        self.columns = self.analyzer.describe_file()
        self.path = self.analyzer.file_path

        self.root.destroy()
        GUI(self.columns, self.path)


class GUI:
    def __init__(self, columns, path):
        self.root = tk.Tk()
        self.root.title("AnoData")
        self.root.geometry("400x800")

        # Frame to scroll
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.scrollable_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # List saving Entry fields
        self.entries = []
        # List saving Combobox fields
        self.dropdowns = []

        # Go through list of tuples to fill in boxes
        for i, (column_name, column_type, column_example, column_range_from, column_range_to) in enumerate(columns):
            frame = ttk.LabelFrame(self.scrollable_frame, text=str(i + 1) + ". " + column_name)
            frame.pack(padx=15, pady=15, fill="x")

            # 1) Example section
            ttk.Label(frame, text="Example:").grid(row=1, column=0, sticky="w")
            ttk.Label(frame, text=column_example).grid(row=1, column=1, sticky="w")

            # 2) Data Range From section
            ttk.Label(frame, text="Data Range From:").grid(row=2, column=0, sticky="w")
            data_range_from_entry = ttk.Entry(frame, state="normal")
            data_range_from_entry.grid(row=2, column=1, sticky="w")

            # Set default value for Data Range From
            data_range_from_entry.insert(tk.END, column_range_from)

            # 3) Data Range To section
            ttk.Label(frame, text="Data Range To:").grid(row=3, column=0, sticky="w")
            data_range_to_entry = ttk.Entry(frame, state="normal")
            data_range_to_entry.grid(row=3, column=1, sticky="w")

            # Set default value for Data Range To
            data_range_to_entry.insert(tk.END, column_range_to)

            # 4) String range section
            ttk.Label(frame, text="String range:").grid(row=4, column=0, sticky="w")
            string_range_to_entry = ttk.Entry(frame, state="normal")
            string_range_to_entry.grid(row=4, column=1, sticky="w")

            # 5) Data Type section
            ttk.Label(frame, text="Data Type:").grid(row=5, column=0, sticky="w")
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
            data_type_dropdown = ttk.Combobox(frame, values=data_type_values)
            data_type_dropdown.grid(row=5, column=1, sticky="w")

            # Set default value for Data Type section
            data_type_dropdown.current(data_type_values.index(data_type_var.get()))

            # 6) Modification section
            ttk.Label(frame, text="Modification:").grid(row=6, column=0, sticky="w")
            modification_entry = ttk.Entry(frame)
            modification_entry.grid(row=6, column=1, sticky="w")

            modification_values = ["Remain as is", "Draw from data range"]
            modification_dropdown = ttk.Combobox(frame, values=modification_values, state="readonly")
            modification_dropdown.grid(row=6, column=1, sticky="w")

            # Set default value for Modification section
            modification_dropdown.current(modification_values.index("Remain as is"))

            self.entries.append((data_range_from_entry, data_range_to_entry, string_range_to_entry))
            self.dropdowns.append((data_type_dropdown, modification_dropdown))

        # Generate Button
        generate_button = ttk.Button(self.scrollable_frame, text="Generate",
                                     command=lambda: self.get_user_choices(columns, path))
        generate_button.pack(pady=15)

        # Result
        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack()

        self.root.mainloop()

    def get_user_choices(self, columns, path):
        user_choices = []  # List storing user choices

        # Collect user choices for each column
        for i, (column_name, column_type, _, _, _) in enumerate(columns):
            data_range_from = self.entries[i][0].get()
            data_range_to = self.entries[i][1].get()
            string_range_to = self.entries[i][2].get()
            data_type = self.dropdowns[i][0].get()
            modification = self.dropdowns[i][1].get()

            user_choices.append((column_name, data_type, data_range_from, data_range_to, string_range_to, modification))

        print(user_choices)

        processor = csv_p.CSVProcessor(path)

        modified_data = processor.process_data(user_choices)
        processor.create_new_csv(modified_data)

        return user_choices

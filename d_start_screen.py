import tkinter.messagebox as messagebox
import sys
import b_csv_entry as csv_e
import tkinter as tk
from tkinter import ttk
import e_gui as g


def exit_program():
    if messagebox.askokcancel("Exit", "Do you want to close the program?"):
        sys.exit()


class StartScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AnoData")
        self.root.geometry("400x300")
        self.root.iconbitmap("x_letter-a.ico")

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        image = tk.PhotoImage(file="x_background.png", master=self.canvas)
        self.canvas.create_image(0, 0, anchor="nw", image=image)

        # Calculate the center coordinates of the canvas
        canvas_center_x = 400 // 2
        canvas_center_y = 300 // 2

        # Add label above the button
        label = tk.Label(self.root, text="Program to anonymize your data. \nSelect CSV and input parameters.",
                         background="#FFE1ED", font=("Calibri", 12), relief="sunken", width=30, height=3)
        label.place(x=canvas_center_x, y=canvas_center_y-80, anchor="center")

        # Add "Select CSV" button
        select_csv_button = ttk.Button(self.root, text="Select CSV", command=self.handle_select_csv, width=20)
        select_csv_button.place(x=canvas_center_x, y=canvas_center_y, anchor="center")

        self.analyzer = None
        self.columns = None
        self.path = None
        self.root.protocol("WM_DELETE_WINDOW", exit_program)
        self.root.mainloop()

    def handle_select_csv(self):
        self.analyzer = csv_e.CSVAnalyzer()
        self.columns = self.analyzer.describe_file()
        self.path = self.analyzer.file_path

        self.root.destroy()
        g.GUI(self.columns, self.path)

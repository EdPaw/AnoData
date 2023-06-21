import csv
import random
from datetime import datetime, timedelta
import tkinter.messagebox as messagebox


class CSVProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def calculate_rows(self):
        rows = -1
        with open(self.file_path, "r", encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                rows += 1

        return rows

    def original_file_content(self):
        with open(self.file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            rows = list(reader)

        return rows

    def process_data(self, column_choices):
        modified_data = []
        column_names = [column[0] for column in column_choices]
        num_rows = self.calculate_rows()
        original = self.original_file_content()

        for i in range(num_rows):
            row_data = []
            for column in column_choices:
                column_type = column[1]
                data_range_from = column[2]
                data_range_to = column[3]
                string_range_to = column[4]
                string_range_to = string_range_to.split(',')
                modification = column[5]

                if modification == "Remain as is" or column_type == "Geo":
                    row_data.append(original[i + 1][column_names.index(column[0])])

                elif modification == "Draw from data range":
                    if column_type == "Int":
                        random_value = random.randint(int(float(data_range_from.replace(',', '.'))),
                                                      int(float(data_range_to.replace(',', '.'))))
                        row_data.append(str(random_value))

                    elif column_type == "Float":
                        random_value = random.uniform(float(data_range_from.replace(',', '.')),
                                                      float(data_range_to.replace(',', '.')))
                        row_data.append(str(random_value))

                    elif column_type == "Date":
                        data_range_from = datetime.strptime(data_range_from, "%Y-%m-%d %H:%M:%S")
                        data_range_to = datetime.strptime(data_range_to, "%Y-%m-%d %H:%M:%S")

                        random_value = data_range_from + timedelta(seconds=random.randint(0, int((data_range_to - data_range_from).total_seconds())))
                        row_data.append(random_value)

                    elif column_type == "Bool":
                        random_value = str(random.choice([True, False]))
                        row_data.append(random_value)

                    elif column_type == "String":
                        random_value = str(random.choice(string_range_to))
                        row_data.append(random_value)

            modified_data.append(row_data)

        return [column_names] + modified_data

    @staticmethod
    def create_new_csv(modified_data):
        try:
            with open("modified_data.csv", "w", newline="", encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                writer.writerows(modified_data)
                messagebox.showinfo("Success", "File generated")
        except PermissionError:
            messagebox.showinfo("Fail", "No permissions to save or file opened")

        return "modified_data.csv"

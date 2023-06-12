import csv
import random


def calculate_rows():
    pass


def process_data(choices):
    modified_data = []

    for column in choices:
        modified_value = None
        column_name, data_type, data_range_from, data_range_to, modification = column
        modified_data = [column_name]

        if data_type == 'Int':
            if modification == "Remain as is":
                modified_value = 2
            elif modification == "Draw from data range":
                modified_value = random.randint(int(data_range_from), int(data_range_to))

        elif data_type == 'Float':
            if modification == "Remain as is":
                modified_value = 1.0
            elif modification == "Draw from data range":
                modified_value = random.uniform(float(data_range_from), float(data_range_to))

        elif data_type == 'String':
            if modification == "Remain as is":
                modified_value = "abc"
            elif modification == "Draw from data range":
                modified_value = 2

        modified_data.append(modified_value)

    print(modified_data)
    return modified_data


def create_new_csv(modified_data):
    # Creating new CSV file with modified data
    with open("modified_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for row in modified_data:
            writer.writerow([row])

    return "modified_data.csv"

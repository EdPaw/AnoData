import csv_entry as c
import csv


path = c.get_path()
new = []
with open(path, 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    rows = list(reader)
    for i in range(5):
        print(rows[i])
        new.append(rows[i])

with open("test.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(new)

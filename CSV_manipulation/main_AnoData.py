import csv_mod as c
import gui as g


def main():
    c_path = c.check_if_file_correct()
    columns = c.show_file(c_path)
    g.create_gui(columns)


if __name__ == '__main__':
    main()

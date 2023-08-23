import pandas as pd


def read(filename):
    return pd.read_excel(filename, engine='openpyxl')


def write(table):
    table.to_csv('output_file_name.csv', index=False)


def convert(filename):
    write(read(filename))


if __name__ == "__main__":
    convert('first_project.xlsx')

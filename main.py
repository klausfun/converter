import pandas as pd


def read():
    return pd.read_excel(io='first_project.xlsx', engine='openpyxl')


def write(table):
    table.to_csv('output_file_name.csv', index=False)


if __name__ == "__main__":
    write(read())

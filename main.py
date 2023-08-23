import pandas as pd
import openpyxl
import csv


def read():
    x = pd.read_excel(io='first_project.xlsx', engine='openpyxl')
    return x


def write(y):
    y.to_csv('output_file_name.csv', index=False)  # index=False prevents pandas from writing a row index to the CSV.


if __name__ == "__main__":
    t = read()
    write(t)
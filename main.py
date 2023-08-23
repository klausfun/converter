import pandas as pd


def read(filename: str) -> pd.DataFrame:
    return pd.read_excel(filename, engine='openpyxl')


def write(table: pd.DataFrame) -> None:
    print(table)
    table.to_csv('output_file_name.csv', index=False)


def convert(filename: str) -> None:
    write(read(filename))


if __name__ == "__main__":
    filename = input()
    if not filename:
        filename = 'first_project.xlsx'

    try:
        convert(filename)
    except Exception as e:
        print(e)

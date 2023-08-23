import pandas as pd


def read(filename: str) -> pd.DataFrame:
    return pd.read_excel(filename, engine='openpyxl')


def write(table: pd.DataFrame, output_filename: str) -> None:
    print(table)
    table.to_csv(output_filename, index=False)


def convert(filename: str, output_filename: str = 'output_file_name.csv') -> None:
    write(read(filename), output_filename=output_filename)


def test() -> None:
    # TODO вынести эту функцию в отдельный файл (посмотри библиотеку pytest)
    convert('test_data/test.xlsx', 'test_data/test.csv')

    with open('test_data/test.csv', 'rb') as output_file:
        result = output_file.readlines()

    with open('test_data/expected_result.csv', 'rb') as expected_result_file:
        expected_result = expected_result_file.readlines()

    if expected_result != result:
        raise ZeroDivisionError  # TODO измени ошибку, которая вызывается
    else:
        pass


if __name__ == "__main__":
    filename = input()
    if not filename:
        filename = 'first_project.xlsx'

    try:
        convert(filename)
    except Exception as e:
        print(e)

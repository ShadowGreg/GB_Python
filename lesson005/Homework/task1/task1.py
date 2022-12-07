# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
from pathlib import Path


def get_line_from(input_path: str) -> str:
    with Path(input_path, 'task1.txt').open("r", encoding="utf-8") as f:
        output_text = f.read()
    return output_text


def clean_line(input_line: str) -> str:
    DELETE_TEXT = 'абв'
    return (' ').join([i for i in input_line.split() if DELETE_TEXT not in i])


def write_line_to(input_folder: str, input_line: str) -> str:
    OUT_NAME = 'out.txt'
    with Path(input_folder, OUT_NAME).open("w", encoding="utf-8") as f:
        f.write(input_line)
    return f'Результат записан в файл по пути > {Path(input_folder, OUT_NAME)}'


def main():
    path = 'files'
    print(get_line_from(path))
    print(clean_line(get_line_from(path)))
    print(write_line_to(path, clean_line(get_line_from(path))))


main()

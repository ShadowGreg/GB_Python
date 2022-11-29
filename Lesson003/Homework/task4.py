# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
import random


def get_num() -> int:
    start = 1
    end = 1000
    return random.randrange(start, end)


def binary_number(in_num: int) -> str:
    count = 0
    out_str = ''
    while in_num > 0:
        count += 1
        out_str = str(in_num % 2) + out_str
        in_num = in_num // 2
        if count == 4:
            out_str = ' ' + out_str
            count = 0
    return out_str


def main_program():
    temp_num = get_num()
    print(f'{temp_num} -> {binary_number(temp_num)}')


main_program()

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from GenerateArray import generate_float as gf


def get_decimal(in_num: float):
    return float('0.'+str(in_num).split('.')[1])


def get_decimal_array(in_array: list):
    output_array = []
    for i in in_array:
        output_array.append(get_decimal(i))
    return output_array


def find_different(in_array: list):
    temp_array = get_decimal_array(in_array).copy()
    return max(temp_array) - min(temp_array)


def main_program():
    temp_array = gf(1, 10, 10).copy()
    print(f'{temp_array} => {find_different(temp_array)}')


main_program()

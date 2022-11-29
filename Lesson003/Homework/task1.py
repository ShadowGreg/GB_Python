# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётных индексах.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных индексах элементы 3 и 9, ответ: 12

from GenerateArray import generate_list


def find_elements_and_count(in_list: list):
    count = 0
    out_msg = ''
    for i in range(1, len(in_list), 2):
        count += i
        if i < len(in_list) - 2:
            sign = ' и '
        else:
            sign = ' '
        out_msg = out_msg + str(in_list[i]) + sign
    return out_msg, count


def main_program():
    start_rnd = 2
    end_rnd = 10
    temp_array = generate_list(start_rnd, end_rnd).copy()
    print(f'Исходный массив элементов {temp_array} ', end='')
    print(
        f' -> на нечётных индексах элементы {find_elements_and_count(temp_array)[0]}, ответ: {find_elements_and_count(temp_array)[1]}')


main_program()

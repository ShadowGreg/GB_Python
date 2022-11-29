# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from GenerateArray import generate_list as gl


def find_composition(first_num: int, second_num: int):
    return first_num * second_num


def create_array(in_array: list):
    start_index: int = 0
    end_index = int(len(in_array) - 1)
    temp_array = []
    while (start_index != end_index) and (start_index < end_index):
        temp_array.append(find_composition(in_array[start_index], in_array[end_index]))
        start_index += 1
        end_index -= 1
        # if start_index == end_index:  почему эта конструкция не работает?
        #     continue
    return temp_array


def main_program():
    local_array = gl(2, 10, 5)
    print(f'{local_array} => {create_array(local_array)}')


main_program()

# Реализуйте алгоритм перемешивания списка.
import random as rnd


def generate_list() -> list:
    quantity = rnd.randrange(2,10)
    output_data = []
    for _ in range(quantity + 1):
        output_data.append(rnd.randrange(100))
    return output_data


def compare(in_firs_list: list, in_second_list: list):
    for i in range(0, len(in_firs_list) - 1):
        if in_firs_list[i] == in_second_list[i]:
            return True
    return False


def deep_mix(in_list: list):
    output_data = in_list.copy()
    while compare(in_list, output_data):
        rnd.shuffle(output_data)
    return output_data


output_list = generate_list().copy()
print(f'Случайный массив >\t\t {output_list}')
print(f'Перемешанный массив >\t {deep_mix(output_list)}')

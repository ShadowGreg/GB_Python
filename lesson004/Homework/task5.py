# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях). Пример того, что будет в итогвом
# файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

import re
from pathlib import Path

END_DICTIONARY = 9999999


def read_file(input_folder: str, input_name: str):
    with Path(input_folder, input_name).open("r", encoding="utf-8") as f:
        output_text = f.read()
    return output_text


def line_separate(input_str: str, input_sep: str = ' ') -> list:
    out_list = input_str.partition(input_sep)
    while out_list[-1] != '0':
        temp = out_list[-1]
        out_list = out_list[:-1]
        out_list = out_list + temp.partition(input_sep)
    return out_list


def find_stem_multiplier(input_str: str) -> list:
    nums = re.findall(r'\d+', input_str)
    nums = [int(i) for i in nums]
    return nums


def get_line_array(input_str: str) -> list:
    separate_line = line_separate(input_str)
    output_list = []
    for i in range(0, len(separate_line)):
        output_list.append(find_stem_multiplier(separate_line[i]))
    return [x for x in output_list if x != []]


def get_dictionary(input_array: list) -> dict:
    count = 0
    out_dic = {}
    for i in range(0, len(input_array)):
        if len(input_array[i]) == 1:
            count += 1
        if len(input_array[i]) == 2:
            out_dic[input_array[i][1]] = input_array[i][0]
    if count == 3:
        out_dic[1] = input_array[len(input_array) - 3][0]
        out_dic[0] = input_array[len(input_array) - 2][0]
        out_dic[END_DICTIONARY] = 0
    if count == 2:
        out_dic[0] = input_array[len(input_array) - 2][0]
        out_dic[END_DICTIONARY] = 0
    if count == 1:
        out_dic[END_DICTIONARY] = 0
    return out_dic


def summarize_dictionaries(in_first_dict: dict, in_second_dict: dict) -> dict:
    out_dictionary = {k: in_first_dict.get(k, 0) + in_second_dict.get(k, 0) for k in
                      set(in_first_dict) | set(in_second_dict)}
    return out_dictionary


def get_string_line(input_dict: dict) -> str:
    output_line = ''
    for key, value in sorted(input_dict.items(), key=lambda x: x[0]):
        if key != END_DICTIONARY and key != 0 and key != 1:
            output_line = f'{value}*(x**{key}) + ' + output_line
        if key == 0:
            output_line = f'{value} + ' + output_line
        if key == 1:
            output_line = f'{value}*x + ' + output_line
        output_line = f'{output_line[:-3]}= 0'
    return output_line


def write_file(input_folder: str, input_name: str, input_text: str):
    with Path(input_folder, input_name).open("w", encoding="utf-8") as f:
        f.write(input_text)
    return Path(input_folder, input_name)


folder = 'task'
first_file = 'polynomial01.txt'
second_file = 'polynomial02.txt'
output_file = 'output.txt'


def main():
    first_list = get_line_array(read_file(folder, first_file))
    second_list = get_line_array(read_file(folder, second_file))
    output_line = get_string_line(summarize_dictionaries(get_dictionary(first_list), get_dictionary(second_list)))
    print(f'файл записан по пути > {write_file(folder, output_file, output_line)}')


main()

# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +, -, /, *.приоритет операций стандартный.
# *Пример: *
# 2 + 2 = > 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 * 3 = > -5;
#
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#
# *Пример: *
#
# 1 + 2 * 3 = > 7;
#
# (1 + 2) * 3 = > 9;

import re


# print(eval(input("Введите вычмсляемое выражение: ")))


def parse_symbols(full_string):
    res_list = []
    for i in full_string:
        if i in "+-/*":
            res_list.append(i)
    return res_list


# def calc(num_list: list, op_list: list):
#     while len(num_list) > 1:
#         if ('*' in op_list) and ('/' in op_list):
#             if op_list.index('*') < op_list.index('/'):
#                 i = op_list.index('*')
#                 sc = '*'
#             else:
#                 i = op_list.index('/')
#                 sc = '/'
#         elif '*' in op_list:
#             i = op_list.index('*')
#             sc = '*'
#         elif '/' in op_list:
#             i = op_list.index('/')
#             sc = '/'
#         elif ('+' in op_list) and ('-' in op_list):
#
#
#         tmp = list(num_list[i] * num_list[i + 1])
#         num_list = num_list[:i] + tmp + num_list[i + 2:]
#         op_list.remove(sc)
#
# expression = input("Введите вычисляемое выражение: ")
expression = "23+54-47*895/1452+65"
symbs = parse_symbols(expression)
expression = (re.findall(r'-|/|\+|\*|[\d]+', expression))
print(expression)
print(symbs)


# lambda x: (x:=x+1)

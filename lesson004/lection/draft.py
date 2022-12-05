# # import re
# #
# # first_line = '67*(x**4) + 9*(x**3) + 37*(x**2) + 46*x + 18 = 0'
# # second_line = '76*(x**8) + 74*(x**7) + 67*(x**6) + 55*(x**5) + 86*(x**4) + 37*(x**3) + 81*(x**2) + 12*x + 13 = 0'
# #
# #
# # def find_longest(f_line: str, s_line: str) -> str:
# #     first_length = len(f_line)
# #     second_length = len(s_line)
# #     if first_length > second_length:
# #         return first_length
# #     if first_length < second_length:
# #         return second_length
# #     if first_length == second_length:
# #         return second_length
# #
# #
# # # def get_key(in_str: str) -> list:
# # #     # отделить степени х
# # #     temp_list = str.split()
# # #     return temp_list
# #
# #
# # # first_sep = first_line.partition(' ')
# # # print(first_sep)  # находит индекс первого вхождения
# # # second_step = []
# # # for item in first_sep:
# # #     second_step.append(item.rsplit(sep='*('))
# # # print(second_step)
# #
# #
# # def separate_by_str(in_str: str, in_sep: str) -> list:
# #     out_list = in_str.partition(in_sep)
# #     while out_list[-1] != '0':
# #         temp = out_list[-1]
# #         out_list = out_list[:-1]
# #         out_list = out_list + temp.partition(in_sep)
# #     return out_list
# #
# #
# # print(separate_by_str(first_line, ' '))
#
#
# # case_list = {}
# # for entry in entries_list:
# #     case = {'key1': value, 'key2': value, 'key3':value }
# #     case_list[entryname] = case
#
#
# # # вычленение чисел
# import re
#
# match = re.match(r"([a-z]+)([0-9]+)", 'foofo21', re.I)
# if match:
#     items = match.groups()
# print(items)
# print()
# items= []
# nums = re.findall(r'\d+', '67*(x**4) + 9*(x**3) + 37*(x**2) + 46*x + 18 = 0')
# nums = [int(i) for i in nums]
# print(nums)
#
# # sorted_tuple = sorted(out_dictionary.items(), key=lambda x: x[0], reverse=True)
#     # return dict(sorted_tuple)

# 2. Задайте список. Напишите программу, которая определит, присутствует ли в
# заданном списке строк некое число.
# ['213213', 'dsf653', 'dsf', 'fdh76']
# num = 3
# Вывод: '213213', 'dsf653'

def filter_contain(string_to_check):
    num = 3
    if str(num) in string_to_check:
        return True
    else:
        return False


array_to_filter = ['213213', 'dsf653', 'dsf', 'fdh76']

out_filter = list(filter(filter_contain, array_to_filter))
print(out_filter)

# 'r' - чтение
# 'w' - перезапись (если файла нет, его создаст)
# 'a' - до запись
# 'r+' - чтение + запись

# file_path = r'file.txt'

# О том, как правильно оформлять путь к файлу (базовый вариант): https://pythonworld.ru/moduli/modul-os-path.html
# Но лучше сразу так: https://www.digitalocean.com/community/tutorials/how-to-use-the-pathlib-module-to-manipulate-filesystem-paths-in-python-3-ru
# *По просьбе аналитиков: https://stepik.org/course/76/syllabus

# with open('file_Task1.txt', 'r') as f:
#     string = f.read() - читает всё readline в цикле
# print(string)


# 1. Считать строку набора чисел из файла. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел. Результат запишите в исодный файл (minn maxx).

# from pathlib import Path

# path = 'task1.txt'
# text_path = Path('task1.txt')

# with open('task1.txt', 'r') as f:
#     string_line = f.read()

# int_array = int(string_line.split(' '))


# print(Max(int_array))
# print(Min(int_array))

f_path = 'test.txt'

with open(f_path, 'r') as f_nums:
    list_nums = f_nums.read().split(' ')
# print(list_nums)
for i in range(len(list_nums)):
    list_nums[i] = int(list_nums[i])

minmax_list = [min(list_nums), max(list_nums)]

# with open(f_path, 'a') as min_max:
#     min_max.writelines(f"\n {minmax_list} ")

print(minmax_list)

# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом
# другого.

#  *Примеры:*

#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет


a = print('Введите первое число: > ', int(input()))
b = print('Введите второе число: > ', int(input()))

if (a == b**2) or (b == a**2): #
    print(f'{a},{b} -> да')
else:
    print(f'{a},{b} -> нет')

a = 50 if True else 70 # тернарный оператор в c# a? = 


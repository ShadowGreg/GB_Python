# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

from random import randint
col = [int(el) for el in input('Введите 5 чисел: ').split()]
print(f'Максимальное число = {max(col)}')


list_to_find_max = list(map(int, input('Введите несколько чисел ').split()))
maximal = list_to_find_max[0]
for i in range(len(list_to_find_max) - 1):
    if list_to_find_max[i] >= maximal:
        maximal = list_to_find_max[i]
print(maximal)


num = 0
maximum = int(input("Введите число: "))
# range(5) -> 0 1 2 3 4
# range(1,5) -> 1 2 3 4
# range(1,5,2) -> 1 3
for _ in range(4):  # _ если переменная итератора не требуется её можно хаменить _`
    num = int(input("Введите число: "))
    if num > maximum:
        maximum = num
print(maximum)


numbers = []  # списки
for i in range(5):
    numbers.append(randint(-10, 10))
max_count = max(numbers)
print(numbers)
print(max_count)

# .pop() -индекс элемента
# .remuve() -значение элемента
# a = [42,67,12,87,112]
# a[1:3] -> [67, 12]
# a[2:] -> [12, 87, 112]
# a[::2] -> [42, 12, 112]

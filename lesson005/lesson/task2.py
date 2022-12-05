# 2. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 4 5 7 8 9

# string_ = '1 2 3 4 5 6 8 9'
# li = set(map(int, string_.split()))
# li_1 = set(i for i in range(1, len(li)+1))
# dif = li_1-li
# print(*dif) #* распаковка на лету

# int_ = [1, 2, 3, 4, 5, 6, 8, 9]
#
#
# def find(input_array):
#     for i in range(1, len(int_)):
#         if (int_[i] - 1) != (int_[i - 1]):
#             return int_[i-1]+1
#
#
# print(find(int_))

# 3.Дан список чисел.Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок
# элементов менять нельзя.
#
# *Пример: *
# [1, 5, 2, 3, 4, 6, 1, 7] = > [1, 5, 6, 7] и т.д.


li = [-1, 0, 8, 5, 4, 8, 0, 12]
my_li = [li[0]]

# for i in range(1, len(li)):
#     if my_li[-1] < li[i]:
#         my_li.append(li[i])
# print(my_li)

# [my_li.append(li[i]) for i in range(1, len(li)) if my_li[-1] < li[i]]
# print(my_li)


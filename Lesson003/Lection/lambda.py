# sum = lambda x: x + 10
# mult = lambda x: x ** 2
#
#
# def h(x, y, z): return x(y(z))
#
#
# h = lambda x, y, z: x(y(z))
#
# h(sum, mult, 5)

# # Анонимные, lambda функции
# f = open('f.txt', 'r')
# data = f.read() + ' '
# f.close()
# numbers = []
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)

# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()
data = select(int, data)
data = where(lambda e: not e % 2, data) # 0 - True 1 - False
print(data)
data = list(select(lambda e: (e, e ** 2), data))


def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()
data = select(int, data)
data = where(lambda e: not e % 2, data)
data = list(select(lambda e: (e, e ** 2), data))

data = '1 2 3 5 8 15 23 38'.split()
data = list(map(int, data))
data = list(filter(lambda e: not e % 2, data))
data = list(map(lambda e: (e, e**2), data))
print(data)

# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.
# f(x) ⇒ x + 10
# map(f, [ 1, 2, 3, 4, 5])
#  ↓ ↓ ↓ ↓ ↓
#  [ 11, 12, 13, 14, 15]
# Нельзя пройтись дважды

# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4,5])
#  ↓
#  [ 2, 4 ]
# Нельзя пройтись дважды


# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
#  ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды


# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#  ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды

#
# List Comprehension
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# List comprehension — это упрощенный подход к созданию списка, который задействует цикл for,
# а также инструкции if-else для определения того, что в итоге окажется в финальном списке.

# >>> nums = [1, 2, 3, 4, 5]
# >>> squares = [n*n for n in nums]
# >>> print(squares)
# [1, 4, 9, 16, 25]
#
# >>> nums = [1, 2, 3, 4, 5]
# >>> odd_squares = [n*n for n in nums if n%2 == 1]
# >>> print(odd_squares)
# [1, 9, 25]
#
# >>> matrix = [[x for x in range(1, 4)] for y in range(1, 4)]
# >>> print(matrix)
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
#
# people = [{
#   "first_name": "Василий",
#   "last_name": "Марков",
#   "birthday": "9/25/1984"
# }, {
#   "first_name": "Регина",
#   "last_name": "Павленко",
#   "birthday": "8/21/1995"
# }]
#
# birthdays = [
#   person[term]
#   for person in people
#   for term in person
#   if term == "birthday"
# ]
#
# print(birthdays)
#
# В этом примере мы сперва перебираем people, присваивая каждый словарь person. После этого перебираем каждый идентификатор в словаре, присваивая ключи term. Если значение term равно birthday, то значение person[term] добавляет в list comprehension.
#
# ['9/25/1984', '8/21/1995']

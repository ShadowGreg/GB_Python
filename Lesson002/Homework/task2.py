# Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.

# Пример:

# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def composition(in_num: int):
    count: int = 1
    string_count = ''
    for i in range(1, in_num + 1):
        count = count * i
        if i <= 1:
            sign = ''
        else:
            sign = '*'
        string_count = string_count + sign + str(i)
    return count, string_count


def list_composition(in_num: int):
    list1 = []
    list2 = []
    for i in range(1, in_num + 1):
        list1.append(composition(i)[0])
        list2.append(composition(i)[1])
    return list1, list2


n = int(input('введите n > '))
print(f'N = {n}, тогда {list_composition(n)[0]} {list_composition(n)[1]}')

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0
def create_list(in_num: int) -> list:
    output = []
    for i in range(-in_num, in_num + 1):
        output.append(i)
    return output


def input_index(in_msg: str) -> list:
    output = []
    for i in in_msg.split(' '):
        output.append(int(i))
    return output


def multiplication(in_list: list, in_index: list):
    mult = 1
    output_str = ''
    for i in in_index:
        mult = mult * in_list[i]
        if i is len(in_index):
            sign = ''
        else:
            sign = ' * '
        output_str = output_str + str(in_list[i]) + sign
    return mult, output_str


def main_program():
    n = int(input('Введите число n= '))
    create_numbers = create_list(n)
    print('получился массив: ')
    print(create_numbers)
    print('введите индексы элементов через пробел:')
    indexes = input('--> ')
    print('произведение имеет вид: ')
    print(
        f'{multiplication(create_numbers, input_index(indexes))[1]} = {multiplication(create_numbers, input_index(indexes))[0]}')
    print(f'Вывод: {multiplication(create_numbers, input_index(indexes))[0]}')


main_program()

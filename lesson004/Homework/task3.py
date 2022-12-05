# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]


def delete_duplicates(in_list):
    output_array = in_list.copy()
    temp_dictionary = {}
    for item in output_array:
        if item in temp_dictionary:
            temp_dictionary[item] += 1
        else:
            temp_dictionary[item] = 1
    clean_dictionary = {key: val for key, val in temp_dictionary.items() if val == 1}
    return list(clean_dictionary.keys())


in_array = [1, 1, 2, 3, 4, 4, 4]
print(delete_duplicates(in_array))

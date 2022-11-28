# Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр.
# Пример:
# 0,56 -> 11

def accepts(in_string: str) -> int:
    count = 0
    for item in in_string:
        if item.isdigit():
            count += int(item)
    return count


number = input('> ')
print(f'{number} -> {accepts(number)}')

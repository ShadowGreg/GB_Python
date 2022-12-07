# вариант человек против бота c "интеллектом":
from entities.RegularExpressions import *


def get_bot_amount(input_amount):
    k = randint(1, 29)
    while input_amount - k <= 28 and input_amount > 29:
        k = randint(1, 29)
    return k


player2 = "Bot"
priority = randint(0, 2)
if priority:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while amount > 28:
    if priority:
        k = input_dat(player1)
        counter1 += k
        amount -= k
        priority = False
        p_print(player1, k, counter1, amount)
    else:
        k = get_bot_amount(amount)
        counter2 += k
        amount -= k
        priority = True
        p_print(player2, k, counter2, amount)

if priority:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

# вариант человек против бота:
from entities.RegularExpressions import *

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
        k = randint(1, 29)
        counter2 += k
        amount -= k
        priority = True
        p_print(player2, k, counter2, amount)

if priority:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

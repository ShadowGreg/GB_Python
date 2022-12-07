# 3. Создайте программу для игры в ""Крестики-нолики"".
from entities.PlayingField import *


def main():
    game_over = False
    human = True
    while not game_over:
        print_field()
        if human:
            symbol = "X"
            step = int(input("Ваш ход: "))
        else:
            print("Ход компьютера: ")
            symbol = "O"
            step = find_motion_line()
        if step != '':
            get_move(step, symbol)
            win = get_current_state()
            if win != '':
                game_over = True
            else:
                game_over = False
        else:
            print('Ничья!')
            game_over = True
        human = not human
    print_field()
    print(f'\033[30m\033[43m Победил! {win}')


main()

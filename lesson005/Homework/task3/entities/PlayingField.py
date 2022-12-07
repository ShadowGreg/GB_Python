FIELD = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

VICTORY_LINES = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [0, 4, 8],
                 [2, 4, 6]]


def color_print(item, end=''):
    if item == 'X' and 'Х':
        print(f'\033[31m{item} ', end=end)
    if item == 'O' and 'О':
        print(f'\033[34m{item} ', end=end)
    if item != 'X' and item != 'O':
        print(f'\033[37m{item} ', end=end)


def print_field():
    count = 0
    END_STR = [2, 5, 8]
    for item in FIELD:
        if count in END_STR:
            color_print(item, '\n')
        else:
            color_print(item)
        count += 1


def get_move(step, symbol):
    ind = FIELD.index(step)
    FIELD[ind] = symbol


def get_current_state():
    win = ''

    for i in VICTORY_LINES:
        if FIELD[i[0]] == 'X' and FIELD[i[1]] == 'X' and FIELD[i[2]] == 'X':
            win = 'Игрок'
        if FIELD[i[0]] == 'O' and FIELD[i[1]] == 'O' and FIELD[i[2]] == 'O':
            win = 'Компьютер'

    return win


def find_place(sum_o, sum_x):
    move_place = ''
    for line in VICTORY_LINES:
        o = 0
        x = 0
        for j in range(0, 3):
            if FIELD[line[j]] == 'O':
                o = o + 1
            if FIELD[line[j]] == 'X':
                x = x + 1
        if o == sum_o and x == sum_x:
            for j in range(0, 3):
                if FIELD[line[j]] != 'O' and FIELD[line[j]] != 'X':
                    move_place = FIELD[line[j]]
    return move_place


def find_motion_line():
    motion_line = ''
    motion_line = find_place(2, 0)
    if motion_line == '':
        motion_line = find_place(0, 2)
    if motion_line == '':
        motion_line = find_place(1, 0)
    if motion_line == '':
        if FIELD[4] != 'X' and FIELD[4] != 'O':
            motion_line = 5
    if motion_line == '':
        if FIELD[0] != 'X' and FIELD[0] != 'O':
            motion_line = 1
    return motion_line

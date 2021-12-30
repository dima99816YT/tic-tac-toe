board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


def printBoard():
    r = '+-----+-----+-----+'
    c = '|'
    s = '  '

    for i in range(0, 3):

        print(r)
        print(*[c + s + board[i][j] + ' ' for j in range(0, 3)] + ['|'])

    print(r)


turns = 0


def player_turn(turn_chr):
    while True:
        global turns  # Hate it
        row = input(f'{turn_chr}, Enter row: ')
        column = input(f'{turn_chr}, Enter column: ')
        try:
            row = int(row)
            column = int(column)
        except ValueError:
            print('Ввод некорректных данных!')
            break

        row = int(row)-1
        column = int(column)-1

        if row <= 3 and column <= 3:
            if board[row][column] != ' ':
                printBoard()
                print('Нельзя!')
            board[row][column] = turn_chr
            printBoard()

            turns += 1
            if turns > 4:
                check_win()
            break
        else:
            print('Ввод неправильного столба или строки')
            break


def check_win():  # Переделать с проверкой на X и O (all(X), all(O))
    if all([True if board[i][i] == 'X' else False for i in range(3)]):
        win('Игрок X победил!')

    elif all([True if board[i][2-i] == 'X' else False for i in range(3)]):
        win('Игрок X победил!')

    elif any([True if all([True if board[i][j] == 'X' else False for j in range(3)]) else False for i in range(3)]):
        win('Игрок X победил!')

    elif any([True if all([True if board[j][i] == 'X' else False for j in range(3)]) else False for i in range(3)]):
        win('Игрок X победил!')

    # ----------------------------------

    elif all([True if board[i][i] == 'O' else False for i in range(3)]):
        win('Игрок O победил!')

    elif all([True if board[i][2-i] == 'O' else False for i in range(3)]):
        win('Игрок O победил!')

    elif any([True if all([True if board[i][j] == 'O' else False for j in range(3)]) else False for i in range(3)]):
        win('Игрок O победил!')

    elif any([True if all([True if board[j][i] == 'O' else False for j in range(3)]) else False for i in range(3)]):
        win('Игрок O победил!')


def win(plr):
    restart = input(f'{plr} Сыграем еще раз?(y/n)\n')
    if restart == 'y' or restart == 'Y':
        start()
    else:
        exit()


def start():
    printBoard()
    for i in range(10):
        if i % 2 == 0:
            player_turn('X')
        else:
            player_turn('O')


start()

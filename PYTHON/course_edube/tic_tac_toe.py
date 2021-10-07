from random import randrange

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    board[1][1] = 'X'
    sign = ''
    while sign != 'n':
        print(f"""                  +-------+-------+-------+
                  |       |       |       |
                  |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
                  |       |       |       |
                  +-------+-------+-------+
                  |       |       |       |
                  |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
                  |       |       |       |
                  +-------+-------+-------+
                  |       |       |       |
                  |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
                  |       |       |       |
                  +-------+-------+-------+
        """)
        enter_move(board)
        draw_move(board)
        make_list_of_free_fields(board)
        sign = victory_for(board, sign)


def enter_move(board):  # JA ESTA NO PRINCIPAL
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    move = int(input('Enter your move: '))
    while move not in check:
        print('Please, type a number that has been in the board.')
        move = int(input('Enter your move: '))
    if 1 <= move <= 3:
        index = 0
    elif 4 <= move <= 6:
        index = 1
    else:
        index = 2
    board[index][board[index].index(move)] = 'O'
    return board


def make_list_of_free_fields(board):  # JA ESTA NO PRINCIPAL
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    empty_spaces = []
    for row in range(3):
        for column in range(3):
            if board[row][column] != 'X' and board[row][column] != 'O':
                empty_spaces.append((row, column))
    return empty_spaces


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    empty_spaces = make_list_of_free_fields(board)
    if (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') \
            or (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') \
            or (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O') \
            or (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):
        print('YOU WIN! :)')
        sign = input("Would you like play again? Type 'y' for yes or 'n' for not.")
        return sign
    elif (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') \
            or (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') \
            or (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X') \
            or (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X') \
            or (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X') \
            or (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') \
            or (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X') \
            or (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
        print('THE COMPUTER WINS! :(')
        sign = input("Would you like play again? Type 'y' for yes or 'n' for not.")
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        return sign
    elif not empty_spaces:
        print("THE GAME HAS TIED! :/")
        sign = input("Would you like play again? Type 'y' for yes or 'n' for not.")
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        return sign

    if sign == 'y':
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        display_board(board)
    elif sign == 'n':
        quit()


def draw_move(board):  # JA ESTA NO PRINCIPAL
    # The function draws the computer's move and updates the board.
    empty_space = make_list_of_free_fields(board)
    computer_move = empty_space[randrange(len(empty_space))]
    board[computer_move[0]][computer_move[1]] = 'X'


display_board(board)
print(board)

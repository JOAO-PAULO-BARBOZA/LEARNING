"""Verifica se as linhas do sudoku(board) são válidas. Para serem válidas a soma dos números da linha
 tem que ser exatamente igual a 45.
"""
board = [[["X" for i in range(3)] for j in range(3)] for k in range(9)]
total = 0
while total != 81:
    for i in range(9):
        cont = 0
        number = input("Type a number: ")
        for j in range(3):
            for k in range(3):
                board[i][j][k] = int(number[cont])
                cont += 1
                total += 1


def is_valid(board):
    total = 0
    lst = [45]
    while total != 405:
        for i in range(9):
            if sum(lst) == 45:
                lst = []
            elif sum(lst) != 45:
                return False
            for j in range(3):
                lst += board[i][j]
            total += sum(lst)
    return True


for i in board:
    print(i)
if is_valid(board):
    print("Yes, the sudoku is valid!")
else:
    print("No, the sudoku isn't valid!")

board = []

for i in range(8):

    row = [0 for i in range(8)]
    board.append(row)
    print(row)
# list comprehension
board2 = [[0 for i in range(8)] for j in range(8)]

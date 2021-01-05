'''
This program takes in an unsolved Sudoku board and returns the solved version of that board.
'''

# save unsolved board as list of lists
board = [
            [0,0,2,0,0,0,4,0,0],
            [0,0,0,4,0,2,8,0,0],
            [0,9,0,0,7,0,0,0,2],
            [6,8,0,1,9,0,0,0,0],
            [0,2,0,0,0,0,0,4,0],
            [0,0,0,0,6,3,0,8,7],
            [1,0,0,0,5,0,0,2,0],
            [0,0,3,9,0,6,0,0,0],
            [0,0,8,0,0,0,6,0,0],
        ]

# print unsolved board
for i in range(len(board)):

    if (i % 3 == 0) and (i != 0):

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    for j in range(len(board[0])):

        if (j % 3 == 0) and (j != 0):

            print(" | ", end = "")

        if j == 8:

            print(board[i][j], end ="")

        else:

            print(str(board[i][j]) + ' ', end = "")



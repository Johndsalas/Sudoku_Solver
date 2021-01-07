'''
This program takes in an unsolved Sudoku board and returns the solved version of that board.
'''

# save unsolved board as list of lists
sudoku = [
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

def print_board(board):
    '''
    Prints unsolved Sedoku board from list of list of numbers
    '''
    
    # itterate through each row number
    for i in range(len(board)):

        # for each row number if it is divisable by three and is not zero print dividing line
        if (i % 3 == 0) and (i != 0):

            # print dividing line
            print("- - - - - - - - - -")

        # itterate through each column number
        for j in range(len(board[0])):

            # for each row number if it is divisable by three and is not zero
            if (j % 3 == 0) and (j != 0):

                # print 'pipe' and stay on the same line
                print("|", end = "")

            # if the cloumn number is the last number in the row
            if j == 8:

                # print the number located at borard[row_number][column_number]
                print(board[i][j])

            # other wise print the number located at borard[row_number][column_number] stay on the current line
            else:

                print(str(board[i][j]) + ' ', end = "")

def get_empty(board):
    '''
    Get next empty space on the board
    '''

    # itterate through each row number and each column number
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):

            # if the position of the row and column has a value of 0 (an empty space on the board)
            # return a tuple with the row and column number
            if board[i][j] == 0:
                return (i,j) # (row,column)

def valid(board, number, pos):
    '''
    Verifies if a given number is a valid entry for a given position on the current sudoku board
    '''

    # check row
    # examines a (row, column) pair.
    # itterates through each row in the named column
    # checks if the value in each row matches the value in the named row
    # returns False if any of the values match
    for j in range(len(board[0])):

        if board[j][pos[0]] == number and pos[0] != j:

            return False

    # check column
    # examines a (row, column) pair.
    # itterates through each column in the named row
    # checks if the value in each column matches the value in the named column
    # returns False if any of the values match
    for i in range(len(board)):

        if board[pos[0]][i] == number and pos[1] != i:

            return False

    # check box
    # gets x and y coordinate for box a (row, column) position is in 
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # itterates through values in the box and returns false if and of the values match a specified value 
    for i in range(box_y * 3, (box_y * 3) + 3):

        for j in range(box_x * 3, (box_x * 3) + 3):

            if board[i][j] == number and (i,j) != pos:

                return False

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

# print board
def print_board(bo):
    '''
    Prints Sedoku board from list of list of numbers
    '''
    
    # itterate through each row number
    for i in range(len(bo)):

        # for each row number if it is divisable by three and is not zero print dividing line
        if (i % 3 == 0) and (i != 0):

            # print dividing line
            print("- - - - - - - - - -")

        # itterate through each column number
        for j in range(len(bo[0])):

            # for each row number if it is divisable by three and is not zero
            if (j % 3 == 0) and (j != 0):

                # print 'pipe' and stay on the same line
                print("|", end = "")

            # if the cloumn number is the last number in the row
            if j == 8:

                # print the number located at borard[row_number][column_number]
                print(bo[i][j])

            # other wise print the number located at borard[row_number][column_number] stay on the current line
            else:

                print(str(bo[i][j]) + ' ', end = "")

def find_empty(bo):
    '''
    Get next empty space on the board
    '''

    # itterate through each row number and each column number
    for i in range(len(bo)):
        for j in range(len(bo[0])):

            # if the position of the row and column has a value of 0 (an empty space on the board)
            # return a tuple with the row and column number
            if bo[i][j] == 0:
                return (i,j) # (row,column)

    return False

def valid(bo, num, pos):
    '''
    Verifies if a given number is a valid entry for a given position on the current sudoku board
    '''

    # check row
    # itterates through each other position in the row
    # returns false if there are any matches
    for i in range(len(bo[0])):

        if bo[pos[0]][i] == num and pos[1] != i:

            return False
    
    # check column
    # itterates through each other position in the column
    # returns false if there are any matches
    for i in range(len(bo)):

        if bo[i][pos[1]] == num and pos[0] != i:

            return False

    # check box
    # gets x and y coordinate for box a (row, column) position is in
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # itterates through values in the box and returns false if and of the values match a specified value
    for i in range(box_y * 3, (box_y * 3) + 3):

        for j in range(box_x * 3, (box_x * 3) + 3):

            if board[i][j] == num and (i,j) != pos:

                return False

    return True

def solve(bo):
    '''
    Solve a sudoku board
    '''

    # get position of the first empty place on the board
    # or return True if there are no empty places remaining
    find = find_empty(bo)
    if not find:

        return True

    else:

        row, col = find

    # itterate through all possible values for position (1-9)
    for i in range(1,10):

        # if a value can be legally placed at the given position do so
        # otherwise move to the next value
        if valid(bo, i, (row, col)):

            bo[row][col] = i

            # if calling solve again results no correct values
            # set the current position to a value to zero
            # continue itterating through i values untill a new legal value is found
            # put that value in the current position
            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def make_it_happen(bo):
    '''
    Prints out unsolved and solved vertion of sudoku board
    '''
    print_board(bo)
    solve(bo)
    print('')
    print('')
    print_board(bo)

make_it_happen(board)

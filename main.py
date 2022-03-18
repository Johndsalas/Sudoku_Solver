'''
program for solving a sudoku board
'''

# input unsolved Sedoku board as a list containing a list of numbers for each row in the board
# use 0 for blank spaces
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
def print_board(board):
    '''
    Takes in a list of nine lists of nine numbers each 
    Outputs the numbers as a human readable Sedoku board
    '''
    
    # for each list of numbers in board
    for i in range(len(board)):

        # if it is divisable by three and is not zero print dividing line
        if (i % 3 == 0) and (i != 0):

            # print dividing line
            print("- - - - - - - - - -")

        # Then for each number in the list of numbers
        for j in range(len(board[0])):

            # if it is divisable by three and is not zero
            if (j % 3 == 0) and (j != 0):

                # print 'pipe' and stay on the same line
                print("|", end = "")

            # if it is the last nuber in the row
            if j == 8:

                # print the number and go to the next line
                print(board[i][j])

            # other wise print the number located at borard[row_number][column_number] stay on the current line
            else:

                print(str(board[i][j]) + ' ', end = "")

def find_empty(board):
    '''
    Takes in a computer readable Sedoku board
    returns the coordenents of the first blank space on that board (represented by a 0)
    '''
    # for each list of numbers
    for i in range(len(board)):

        # look through the numbers in each position in the list
        for j in range(len(board[0])):

            # if the number in the number is 0 
            if board[i][j] == 0:

                # return it's coordinates
                return (i,j)

    # if no 0' are found return false
    return False

def valid(board, number, position):
    '''
    Takes in a computer readable Sedoku board, a number, and a position on the Sedoku board expressed as a tuple (row, column)
    return true if the number can legally be placed on the board (no matching number in the same square, row, or column)
    return false otherwise
    '''

    # check's position's row to see if there is a number that matches the input number
   
    # for each position 
    for i in range(len(board[0])):


        # in the same row of numbers as the input number if the number in that position is equal to the input number and is not in the input position
        if board[position[0]][i] == number and position[1] != i:

            # return false
            return False
    
    # check's position's column to see if there is a number that matches the input number

    # for each position
    for i in range(len(board)):

        # in the same column of numbers as the input number if the number in that position is equal to the input number and is not in the input position
        if board[i][position[1]] == number and position[0] != i:

            #return false
            return False


    # check position's square to see if there is a number that matches the input number 

    # find the correct square to check

    # intiger divide both input coordinants by three to get the position of the sqare on a human readable sedoku board

    # 00 01 02
    # 10 11 12
    # 20 21 22

    box_x = position[0] // 3 
    box_y = position[1] // 3

    # multiply those position numbers by 3 to get the coordanents of the upper right position of that square in the machine readable sedoku board
    # 00 03 06
    # 30 33 36
    # 60 63 66

    ur_x = box_x * 3
    ur_y = box_y * 3


    # for each row in the box
    for i in range(ur_x, ur_x + 3):

        # look through the numbers in each position in the box
        for j in range(ur_y, ur_y + 3):

            # if the number in that position is equal to the input number and is not in the input position
            if board[i][j] == number and (i,j) != position:

                # return false
                return False

    return True

def solve(board):
    '''
    Takes in a machine readable Sudoku board and modifies the global variables of that board to create a solved vertion of that board
    '''

    # get position of the first empty place on the board
    find = find_empty(board)

    # if there are no empty spaces return true to close recursion loop
    if not find:

        return True

    # otherwise begin/continue recursion loop
    else:

        row, col = find

    # beginning at one, itterate through all possible numbers that can be placed in a Sudoku board, for each number
    for i in range(1,10):

        # if that number can be legally placed in the open position
        if valid(board, i, (row, col)):

            # place that number in the open position
            board[row][col] = i

            # if calling solve again results no correct values
            # set the current position to a value to zero
            # continue itterating through i values untill a new legal value is found
            # put that value in the current position

            # call solve on board to find the next empty space and place a new number 
            if solve(board):

                # if there are no empty spaces remaining return True
                return True

            # if the next call of solve loops through all 10 possible numbers and does not find a legal placement
            # reset the number placed in this call of solve to 0
            board[row][col] = 0

    # if no number can be legally placed return false
    return False

def make_it_happen(board):
    '''
    takes in a global object that is a machine readable sudoku board 
    prints a human readable copy of the board
    modifies that object to create a solved version of the machine readable board
    then prints a human readable copy of the solved version
    '''

    print()
    print_board(board)
    solve(board)
    print()
    print()
    print_board(board)
    print()

if __name__ == "__main__":  

    make_it_happen(board)

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


print_board(sudoku)
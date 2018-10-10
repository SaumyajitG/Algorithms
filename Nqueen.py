global Size
print "Enter size of board(N) - "
Size= input();


def printSolution(board):
    for i in range(Size):
        for j in range(Size):
            print board[i][j],
        print


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, Size, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveSizeQUtil(board, col):
    if col >= Size:
        return True

    for i in range(Size):

        if isSafe(board, i, col):
            board[i][col] = 1

            if solveSizeQUtil(board, col + 1) == True:
                return True

            board[i][col] = 0


    return False



def solveSizeQ():
    board = [[0 for x in range(Size)] for y in range(Size)]

    if solveSizeQUtil(board, 0) == False:
        print "Solution does not exist"
        return False

    printSolution(board)
    return True


solveSizeQ()
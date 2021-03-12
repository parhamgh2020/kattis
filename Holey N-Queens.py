
def solve(n):
    board = [[0 for x in range(n)] for x in range(n)]
    place_queen(board, 0, 0)

def place_queen(board, row, column):
    """place a queen that satisfies all the conditions"""
    if row > len(board)-1:
        print(board)
    while column < len(board):
        if is_safe(board, row, column):
            board[row][column] = 1
            return place_queen(board, row+1, 0)
        else:
            column += 1
    for c in range(len(board)):
        if board[row-1][c] == 1:
            board[row-1][c] = 0
            return place_queen(board, row-1, c+1)

def is_safe(board, row, column):
    """ if no other queens threaten a queen at (row, queen) return True """
    queens = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 1:
                queen = (r,c)
                queens.append(queen)
    for queen in queens:
        qr, qc = queen
        if row == qr or column == qc:
            return False
        if (row + column) == (qr+qc) or (column-row) == (qc-qr):
            return False
    return True

solve(4)
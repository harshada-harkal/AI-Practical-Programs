N = 8

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))


def is_safe(board, row, col):

    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, N),
                    range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve(board, col):

    if col >= N:
        return True

    for row in range(N):

        if is_safe(board, row, col):

            board[row][col] = 1

            if solve(board, col + 1):
                return True

            board[row][col] = 0

    return False


# Main Program
board = [[0] * N for _ in range(N)]

if solve(board, 0):
    print("Solution Found:\n")
    print_board(board)
else:
    print("No Solution")
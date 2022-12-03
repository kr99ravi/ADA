# Global variables
possible_boards = 0
result = []

# Function to print board


def print_board(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print()
    print()


def is_valid(board, n, row, col):
    # Row
    for i in range(n):
        if board[row][i] == 'Q':
            return False
    # Column
    for j in range(n):
        if board[j][col] == 'Q':
            return False

    # / diagonal
    i, j = row, col

    while (i >= 0 and j >= 0):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # \ diagonal
    i, j = row, col

    while (i < n and j >= 0):
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def n_queens(board, n, result, col=0):

    if col == n:
        global possible_boards
        possible_boards += 1
        ans = [[col for col in row] for row in board]
        result.append(ans)
        return

    for row in range(n):
        if is_valid(board, n, row, col):
            board[row][col] = 'Q'
            n_queens(board, n, result, col+1)
            board[row][col] = '.'


if __name__ == "__main__":
    n = int(input("Enter number of queens: "))
    board = [["." for i in range(n)] for j in range(n)]

    n_queens(board, n, result)
    for board in result:
        print_board(board)

print(f"Total Possible Boards are {possible_boards}")

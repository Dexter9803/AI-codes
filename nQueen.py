

def is_safe(board, row, col, n):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True




def solve_n_queens_util(board, col, n):
    if col == n:
        return True  # All queens are placed successfully

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1  # Place the queen

            if solve_n_queens_util(board, col + 1, n):
                return True  # If placing queen in the current position leads to a solution

            board[i][col] = 0  # If placing queen doesn't lead to a solution, backtrack

    return False  # If no position is found to place the queen in this column





def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return
 
    print_board(board)

def print_board(board):
    for row in board:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))



        

# Example usage:
n = 4  # Change this to the desired board size
solve_n_queens(n)
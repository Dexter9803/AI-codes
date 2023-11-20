INFINITY, NEG_INFINITY = 1000, -1000

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = NEG_INFINITY
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        return best
    else:
        best = INFINITY
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best

if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    print("The optimal value is:", minimax(0, 0, True, values, NEG_INFINITY, INFINITY))


#2 code with solved sudoku


def print_sudoku(puzzle):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(puzzle[i][j], end=" ")
        print()

# Rest of the code remains the same...


def is_valid(puzzle, row, col, num):
    # Check if the number can be placed in the given row and column
    for i in range(9):
        if puzzle[row][i] == num or puzzle[i][col] == num or puzzle[row - row % 3 + i // 3][col - col % 3 + i % 3] == num:
            return False
    return True



def find_empty_location(puzzle):
    # Find an empty cell in the puzzle
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None



def solve_sudoku(puzzle):
    empty_loc = find_empty_location(puzzle)

    if not empty_loc:
        # If no empty cell is found, the puzzle is solved
        return True

    row, col = empty_loc

    for num in range(1, 10):
        if is_valid(puzzle, row, col, num):
            # Try placing the number in the empty cell
            puzzle[row][col] = num

            # Recursively attempt to solve the remaining puzzle
            if solve_sudoku(puzzle):
                return True

            # If placing the number leads to an invalid solution, backtrack
            puzzle[row][col] = 0

    # If no number can be placed in the current cell, backtrack
    return False

# Driver Code
if __name__ == "__main__":
    puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 0, 0]
              ]

    if solve_sudoku(puzzle):
        print("Sudoku puzzle solved:")
        print_sudoku(puzzle)
    else:
        print("No solution exists.")
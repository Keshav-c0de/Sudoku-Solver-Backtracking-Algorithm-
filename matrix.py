
def get_matrix():

    input_board = [[None for _ in range(9)] for _ in range(9)]
    print("Enter your Sudoku puzzle (use -1 for empty spaces):")
    for r in range (9):
        for c in range (9):
            value= int(input(f"enter the value for {r}:{c}-> "))
            input_board[r][c] = value
    return input_board

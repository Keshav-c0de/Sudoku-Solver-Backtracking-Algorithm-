def get_empty_space(puzzle):
    for r in range (9):
        for c in range (9):
            if puzzle[r][c] == -1:
                return r,c
    return None, None


def is_valid(puzzle,guess,row,col):
    row_valid = puzzle[row]
    if guess in row_valid:
        return False
    
    col_valid = []
    for i in range(9):
        col_valid.append(puzzle[i][col])
        if guess in col_valid:
            return False

    row_start = (row//3)*3
    col_start = (col//3)*3
    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if guess == puzzle[r][c]:
                return False

    return True



def solve_puzzle(puzzle):

    row, col = get_empty_space(puzzle)
    if row == None:
        return True

    for guess in range(1,10):
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col]= guess      

            if solve_puzzle(puzzle):   #recursion
                return True

        puzzle[row][col] = -1 

    return False


if __name__ =="__main__":
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_puzzle(example_board))
    print(example_board)



    
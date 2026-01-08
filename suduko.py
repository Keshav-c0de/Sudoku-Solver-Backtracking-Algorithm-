import webscraping


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



def solve_puzzle_steps(puzzle):

    row, col = get_empty_space(puzzle)
    if row == None:
        return True

    for guess in range(1,10):
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col] = guess 
            yield puzzle     

            if (yield from solve_puzzle_steps(puzzle)):                                                           #recursion
                return True

            puzzle[row][col] = -1          # backtracking (pops the previous guess      value and loop move on) 
            yield puzzle

    return False  




if __name__ =="__main__":

    input_board =  webscraping.main()

    if solve_puzzle(input_board):
        print("--------Solution--------")
        for row in input_board:
            print(row)
    else:
        print("No Solution exists") 
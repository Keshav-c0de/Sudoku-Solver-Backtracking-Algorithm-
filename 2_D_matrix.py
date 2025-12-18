puzzle = [[None for _ in range(3)] for _ in range(3)]

for r in range (3):
    for c in range (3):
        guess= input(f"enter the value for {r}:{c}")
        puzzle[r][c] = guess


row = 2
print (f"all the elements in 3rd row is {puzzle[row]}")
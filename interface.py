import pygame
import sys
import webscraping
import suduko
import copy

input_board=webscraping.main()
original_board = copy.deepcopy(input_board)
W = 800
H = 600
pygame.init()
window = pygame.display.set_mode((W,H))
pygame.display.set_caption("suduko")
clock = pygame.time.Clock()

black = (0,0,0)
font = pygame.font.SysFont("comicsans", 40)

cell_size = 50
grid_size = 450

grid_rect = pygame.Rect(0,0,grid_size,grid_size)
grid_rect.center =(W//2,H//2)

solver_generator = []
selected = None

def draw_grid():
    # --- drawning the grid ---
    
    for i in range(10):
        if i % 3 == 0:
            width = 4
        else:
            width = 1

        offset = i* cell_size

        pygame.draw.line(window, black, (grid_rect.left+offset,grid_rect.top), (grid_rect.left+offset,grid_rect.bottom), width)
        pygame.draw.line(window, black, (grid_rect.left,grid_rect.top+offset), (grid_rect.right,grid_rect.top+offset), width)


def draw_input_board():
    for i in range(9):
        for j in range(9):
            num  = input_board[i][j]
            if num != -1:

                if input_board[i][j] == original_board[i][j]:
                    text=font.render(str(num),True,(0,0,0))
                else:
                    temp_val = input_board[i][j]
                    input_board[i][j] = 0
                    if suduko.is_valid(input_board,num,i,j):
                        text=font.render(str(num),True,(128,128,128))
                    else:
                        text=font.render(str(num),True,(128,0,0))
                    input_board[i][j] = temp_val

                x_pos = grid_rect.left+ (j*cell_size)+ (cell_size // 2 - text.get_width() // 2)
                y_pos = grid_rect.top+ (i*cell_size)+  (cell_size // 2 - text.get_height() // 2)
                window.blit(text,(x_pos,y_pos))



running = True

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mou_pos = pygame.mouse.get_pos()
                if grid_rect.collidepoint(mou_pos):
                    col= (mou_pos[0]-grid_rect.left)//cell_size
                    row= (mou_pos[1]-grid_rect.top)//cell_size
                    selected = (row,col)
                else:
                    selected = None

            if selected:
                r , c = selected
                if event.type == pygame.KEYDOWN:
                    if original_board[r][c] != -1:
                        pass
                    else:
                        if event.key == pygame.K_1:input_board[r][c] = 1
                        if event.key == pygame.K_2:input_board[r][c] = 2
                        if event.key == pygame.K_3:input_board[r][c] = 3
                        if event.key == pygame.K_4:input_board[r][c] = 4
                        if event.key == pygame.K_5:input_board[r][c] = 5
                        if event.key == pygame.K_6:input_board[r][c] = 6
                        if event.key == pygame.K_7:input_board[r][c] = 7
                        if event.key == pygame.K_8:input_board[r][c] = 8
                        if event.key == pygame.K_9:input_board[r][c] = 9
                        if event.key == pygame.K_BACKSPACE:input_board[r][c] = -1
                        if event.key == pygame.K_SPACE:solver_generator=suduko.solve_puzzle_steps(input_board)
                        if event.key == pygame.K_LSHIFT:
                            input_board=webscraping.main()
                            original_board = copy.deepcopy(input_board)

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:solver_generator=suduko.solve_puzzle_steps(input_board)
                    if event.key == pygame.K_LSHIFT:
                        input_board=webscraping.main()
                        original_board = copy.deepcopy(input_board)


    
    
    if solver_generator:
        try:
            input_board=next(solver_generator)
            pygame.time.delay(50)
        except StopIteration:
            # This error means the solver finished completely
            solver_generator = None
            print("Finished solving!")

                        

    window.fill((225,225,225))
    draw_grid()
    draw_input_board()
    
    if selected:
        r , c = selected
        x_pos = c*cell_size + grid_rect.left
        y_pos = r*cell_size + grid_rect.top
        selected_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
        pygame.draw.rect(window,(173, 216, 230),selected_rect,2)

   
    pygame.display.update()
    clock.tick(60)




        
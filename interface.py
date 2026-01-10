import pygame
import sys
import webscraping
import suduko
import copy
import os 
import time

def get_asset_path(relative_path):
    try:
        # If running as an app (PyInstaller)
        base_path = sys._MEIPASS
    except Exception:
        # If running in VS Code, use the directory of the script
        base_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(base_path, relative_path)

# ---- getting option image ----
solution_button = pygame.image.load(get_asset_path(os.path.join("Assets","interrogation.png")))
pause_button = pygame.image.load(get_asset_path(os.path.join("Assets","pause.png")))
play_button = pygame.image.load(get_asset_path(os.path.join("Assets","play.png")))
next_button = pygame.image.load(get_asset_path(os.path.join("Assets","right.png")))
reset_button = pygame.image.load(get_asset_path(os.path.join("Assets","refresh.png")))


input_board=webscraping.main()
original_board = copy.deepcopy(input_board)

W = 600
H = 660
pygame.init()
window = pygame.display.set_mode((W,H))
pygame.display.set_caption("suduko")
clock = pygame.time.Clock()

BLACK = (0,0,0)
COLOR_BG = (250, 248, 239)      # Warm off-white background
COLOR_GRID = (187, 173, 160)    # Soft brownish-grey for lines
COLOR_CELL_BG = (255, 255, 255) # White for the cells themselves
COLOR_TEXT_LOCKED = (119, 110, 101)  # Dark Grey for original numbers
COLOR_TEXT_USER = (0, 100, 200)      # Nice Blue for user input
COLOR_SELECTED = (180, 210, 255)     # Light Blue highlight
COLOR_ERROR = (255, 100, 100)        # Soft Red for errors

grid_size = 540
cell_size = grid_size//9

font_1 = pygame.font.SysFont("comicsans", cell_size)
font_2 = pygame.font.SysFont("helvetica", cell_size//2)
font_3 = pygame.font.SysFont("helvetica", 39)

grid_rect = pygame.Rect(0,0,grid_size,grid_size)
grid_rect.center =(W//2,H//2)

solver_generator = []
selected = None

game_won = False
final_time_str = None
start_time = time.time() 


def draw_grid():
    text = "SUDOKU:"
    title = font_2.render(text,1,BLACK)
    window.blit(title,(grid_rect.left,grid_rect.top-5- (cell_size//2)))
    # --- drawning the grid ---
    pygame.draw.rect(window, COLOR_CELL_BG, grid_rect)
    for i in range(10):
        if i % 3 == 0:
            width = 4
        else:
            width = 1

        offset = i* cell_size
        pygame.draw.line(window, COLOR_GRID, (grid_rect.left+offset,grid_rect.top), (grid_rect.left+offset,grid_rect.bottom), width)
        pygame.draw.line(window, COLOR_GRID, (grid_rect.left,grid_rect.top+offset), (grid_rect.right,grid_rect.top+offset), width)


def draw_input_board():
    for i in range(9):
        for j in range(9):
            num  = input_board[i][j]
            if num != -1:

                if input_board[i][j] == original_board[i][j]:
                    text=font_1.render(str(num),True,COLOR_TEXT_LOCKED)
                else:
                    temp_val = input_board[i][j]
                    input_board[i][j] = 0
                    if suduko.is_valid(input_board,num,i,j):
                        text=font_1.render(str(num),True,COLOR_TEXT_USER)
                    else:
                        text=font_1.render(str(num),True,(COLOR_ERROR))
                    input_board[i][j] = temp_val

                x_pos = grid_rect.left+ (j*cell_size)+ (cell_size // 2 - text.get_width() // 2)
                y_pos = grid_rect.top+ (i*cell_size)+  (cell_size // 2 - text.get_height() // 2)
                window.blit(text,(x_pos,y_pos))



class Button:
    def __init__(self,image, x,y ,height,width,command = None):
        self.image = pygame.transform.scale(image, (width, height))
        self.x = x
        self.y = y
        self.height =height
        self.width =width
        self.rect = self.image.get_rect(topleft=(x, y))
        self.command = command


    def display(self,window):
        window.blit(self.image,self.rect)
    
    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if self.command:
                self.command()

def reset():
    global input_board, original_board, game_won, start_time
    input_board = original_board
    original_board = copy.deepcopy(input_board)
    game_won = False
    start_time = time.time()

def solve():
    global solver_generator
    reset()
    solver_generator=suduko.solve_puzzle_steps(input_board)
    

def next_game():
    global input_board, original_board, solver_generator, game_won, start_time
    input_board= webscraping.main()
    original_board = copy.deepcopy(input_board)
    solver_generator= None
    game_won = False
    start_time = time.time()

def check_solution(input_board):
    for i in range(9):
        for j in range(9):
            if input_board[i][j] == -1:
                return False
    for i in range(9):
        for j in range(9):
            current_val = input_board[i][j]
            input_board[i][j] = 0
            if not suduko.is_valid(input_board, current_val, i, j):
                input_board[i][j] =current_val
                return False
            input_board[i][j] =current_val
    return True

btn_solve = Button(solution_button, 40, grid_rect.bottom+10, 32, 32, command= solve)
btn_reset = Button(reset_button, 100,  grid_rect.bottom+10, 32, 32, command= reset)
btn_next = Button(next_button, 160,  grid_rect.bottom+10, 32, 32, command= next_game) 

running = True

while running:

    # --- Getting Input ----

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

                btn_solve.is_clicked(mou_pos)
                btn_reset.is_clicked(mou_pos)
                btn_next.is_clicked(mou_pos)

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

    # --- solver live solving ---

    if solver_generator:
        try:
            next(solver_generator) # Take one step
            pygame.time.delay(20) 
        except StopIteration:
            solver_generator = None
            print("Puzzle Solved Successfully!") # Stop when finished

    window.fill(COLOR_BG)

    # --- Drawing grid and buttons ----

    btn_solve.display(window)
    btn_reset.display(window) 
    btn_next.display(window)
    draw_grid()
    draw_input_board()
    
    # --- Drawing input box ----
    if selected:
        r , c = selected
        x_pos = c*cell_size + grid_rect.left
        y_pos = r*cell_size + grid_rect.top
        selected_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
        pygame.draw.rect(window,(173, 216, 230),selected_rect,2)
    
    # --- time display ---
    if not game_won:
        # Game is running: Calculate live time
        play_time_secs = round(time.time() - start_time)
        minutes = play_time_secs // 60
        seconds = play_time_secs % 60
        time_text = (f"Time- {minutes:02}:{seconds:02}")
        
    # --- Check for Win ---
    if check_solution(input_board) and not game_won:
        final_time_str = time_text # Freeze the time
        pygame.time.delay(20)
        game_won = True 
        print("Winner!")

    else:
    # --- Game is won: Use the frozen time ---
        final_time_str = time_text
    
    text_surface = font_2.render(time_text, True, (0,0,0))
    text_surface_rect = text_surface.get_rect()
    window.blit(text_surface, (grid_rect.right -text_surface.get_width(), grid_rect.top-5- (cell_size//2)))
   
     # --- pop up when solved --- 
    if game_won:
        s = pygame.Surface((390,190))
        s.set_alpha(150)                
        s.fill((255, 255, 255))  
        s_rect =s.get_rect(center=(W//2, H//2))  
     
        window.blit(s, s_rect)
        pygame.draw.rect(window, (0, 0, 0), s_rect, 3)

        # Draw Big Victory Text
        
        win_text = font_3.render("PUZZLE SOLVED!", True, (0, 128, 0)) 
        time_msg = font_2.render(f"{final_time_str}", True, (0, 0, 0))
        next_msg = font_3.render(f"Press    To Next", True, (0, 0, 0))
        
        # Center the text
        win_rect = win_text.get_rect(center=(W//2, H//2 - 50))
        time_rect = time_msg.get_rect(center=(W//2, H//2))
        next_rect = next_msg.get_rect(center=(W//2, H//2 + 50))

        next_img=pygame.transform.scale(next_button, (32, 32))
        

        window.blit(win_text, win_rect)
        window.blit(time_msg, time_rect)
        window.blit(next_msg, next_rect)
        window.blit(next_img, (W//2-28,H//2 +32))


    pygame.display.update()
    clock.tick(60)




        
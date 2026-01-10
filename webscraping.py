import requests
from bs4 import BeautifulSoup


def extart_value():

    start_url = 'https://www.websudoku.com'


    r_1 = requests.get(start_url)
    soup_1 = BeautifulSoup(r_1.text,"html.parser")


    frame_tag= soup_1.find("frame")
    if frame_tag:
        game_link = frame_tag.get("src")
        r_2 = requests.get(game_link)
        soup_2 = BeautifulSoup(r_2.text,"html.parser")
        cheat_input = soup_2.find("input", {'id': 'cheat'})
        edit_mask_input = soup_2.find("input", {'id': 'editmask'}) 
        if cheat_input and  edit_mask_input:
            print(cheat_input)
            print(edit_mask_input)
            value = cheat_input.get("value")
            hidden_value = edit_mask_input.get("value")
            return value, hidden_value

    return None,None


def make_grid(value,hidden_value):

    grid = [int(x) for x in list(value)]
    hidden_grid = [int(x) for x in list(hidden_value)]
   
    for i in range(len(hidden_grid)):
        if hidden_grid[i]==1:
            solution_value= grid[i]
            grid[i]= -1

    input_board=[grid[i : i+9] for i in range(0,81,9)]
    return input_board


def main():
    val, hid_val = extart_value()

    if val and hid_val:
        my_grid = make_grid(val, hid_val)
        
        print("\n--- Matrix Received! ---")
        for row in my_grid:
            print(row)
        return my_grid
    else:
        print("Something went wrong")
        return None
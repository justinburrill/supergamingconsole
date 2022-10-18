# justin burrill 14 10 22

# RUN THIS FILE WITH THE BASH SCRIPT

from tkinter import *
from os import listdir


root = Tk()  # put me at the top

WINRES = [1280, 1024]
winwidth = WINRES[0]
winheight = WINRES[1]
root.geometry(f"{winwidth}x{winheight}")
root.title("Home Screen")


path = "./pyfiles"  # dir to look for games
game_list = []

try:
    game_list = [f for f in listdir(path)]  # get list of games
    print(game_list)
except FileNotFoundError:
    print("path not found")


for game in game_list:
    game_name = Label(root, text=game)
    game_name.pack()
    img = PhotoImage(file=f"ico/{game}.png")
    canvas = Canvas(root, width=300, height=300)
    canvas.pack()
    canvas.create_image(20, 20, anchor=NW, image=img)


root.mainloop()

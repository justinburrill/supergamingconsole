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
    # print(game_list)
except FileNotFoundError:
    print("path not found")

canvas_dict = {}
canvas_list = []

for game in game_list:
    game_name = Label(root, text=game)
    game_name.pack()
    # print(f"ico/{game[0:-3]}.png")
    canvas = Canvas(root, width=300, height=300)
    canvas_dict[game[0:-3]] = canvas
    # print(f"canvas added to dict with name {game}")

# # display
# for key in canvas_dict.keys():
#     imgname = f"ico/{key}.png"
#     img = PhotoImage(file=imgname)

#     canvas_dict[key].pack()
#     canvas_dict[key].create_image(0, 0, anchor=NW, image=img)

# display
for itm in canvas_list:
    imgname = f"ico/{}.png"
    img = PhotoImage(file=imgname)

    itm.pack()
    itm.create_image(0, 0, anchor=NW, image=img)

root.mainloop()

# justin burrill 14 10 22

# RUN THIS FILE WITH THE BASH SCRIPT

from functools import partial
from tkinter import *
from os import listdir
import os

import sys
sys.path.insert(0, '/util_package/')
from util_package import getres

root = Tk()  # put me at the top

WINRES = getres()
winwidth = WINRES[0]
winheight = WINRES[1]
root.geometry(f"{winwidth}x{winheight}")
root.title("Home Screen")

path = "py/"

game_list = [f for f in listdir(path)]  # get list of games
# print(game_list)

def rmpy(inp):
    return inp[0, -3]

def rungame(game):
    print(f"running {game}")
    os.system(f"python3 py/{game}")

for i in range(len(game_list)):
    game = game_list[i]

    f = Frame(root)
    print(f"game: {game}")
    button = Button(f, text=game, command = partial(rungame, game))
    button.pack()


    padx = winwidth/len(game_list)/2 - len(game) * 5
    pady = winheight / 2 # this won't work for more than like 4 games (not an issue right now)
    f.grid( row = 1, column = i, padx = padx , pady = pady)




# for itm in canvas_list:
#     imgname = f"ico/{itm}.png"
#     img = PhotoImage(file=imgname)

#     itm.pack()
#     itm.create_image(0, 0, anchor=NW, image=img)

# working
# frame = Frame(root)
# l = Label(frame, text="hey")
# l.pack()
# frame.pack()

# for f in frames:
#     f.pack()

# old
# for game in game_list:
#     game_name = Label(root, text=game)
#     game_name.pack()
#     img = PhotoImage(file=f"ico/{game}.png")
#     canvas = Canvas(root, width=300, height=300)
#     canvas.pack()
#     canvas.create_image(20, 20, anchor=NW, image=img)



# # display
# for key in canvas_dict.keys():
#     imgname = f"ico/{key}.png"
#     img = PhotoImage(file=imgname)

#     canvas_dict[key].pack()
#     canvas_dict[key].create_image(0, 0, anchor=NW, image=img)

# display



root.mainloop()

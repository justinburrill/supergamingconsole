# justin burrill 14 10 22

from tkinter import *
from os import listdir


root = Tk()  # put me at the top

WINRES = [1280, 1024]
winwidth = WINRES[0]
winheight = WINRES[1]
root.geometry(f"{winwidth}x{winheight}")
root.title("Home Screen")

path = "./py"  # dir to look for games

game_list = [f for f in listdir(path)]  # get list of games
print(game_list)

def rmpy(inp):
    return inp[0, -3]

for i in range(len(game_list)):
    game = game_list[i]

    f = Frame(root)
    button = Button(f, text=game)
    button.pack()


    padx = winwidth/len(game_list)/2 - len(game) * 5
    pady = winheight / 2 # this won't work for more than like 4 games (not an issue right now)
    f.grid( row = 1, column = i, padx = padx , pady = pady)


def rungame(game):
    print(f"running {game}")



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




root.mainloop()

from tkinter import *
from tkinter import ttk
#from backend import *

# apparently time.sleep() doesn't work with tkinter stuff, use this one
def tk_sleep(time_s):
    time_ms = int(time_s*1000)
    variable = IntVar(root)
    root.after(time_ms, lambda: variable.set(1))
    root.wait_variable(variable)


root = Tk()
root.title("Springarvandring")
root.geometry("1000x800+0+0")
root.resizable(0,0)

# constants
SQUARE_SIZE = 75
PAD = 20
BOARD_DIM = 2*PAD+8*SQUARE_SIZE
LIGHT_COLOUR = "#edce93"
DARK_COLOUR = "#a8720a"
# the image has the same dimensions as a square: 75x75
knightImg = PhotoImage(file="yes.png")

# frame that contains the board and the buttons below to step forward or backward
leftframe = Frame(root,highlightbackground="black",highlightthickness=2)
leftframe.pack(side="left")

boardcanvas = Canvas(leftframe,width=BOARD_DIM,height=BOARD_DIM)
boardcanvas.pack(padx=(PAD,PAD),pady=(PAD,PAD))

for i in range(8):
    boardcanvas.create_text((PAD/2,SQUARE_SIZE*(i+0.5)+PAD),text=str(8-i),anchor=CENTER)
    boardcanvas.create_text((SQUARE_SIZE*(i+0.5)+PAD,BOARD_DIM-PAD/2),text=chr(97+i),anchor=CENTER)

for i in range(8):
    for j in range(8):
        x1 = PAD+SQUARE_SIZE*i
        y1 = PAD+SQUARE_SIZE*j
        x2 = x1+SQUARE_SIZE
        y2 = y1+SQUARE_SIZE
        if (i+j) % 2 == 0:
            boardcanvas.create_rectangle(x1,y1,x2,y2,fill=LIGHT_COLOUR)
        else:
            boardcanvas.create_rectangle(x1,y1,x2,y2,fill=DARK_COLOUR)

bottomframe = Frame(leftframe,highlightbackground="blue",highlightthickness=2)
bottomframe.pack(side="bottom")

prevMoveButton = Button(bottomframe, text="<-").pack(side="left")
nextMoveButton = Button(bottomframe, text="->").pack(side="left")


menuframe = Frame(root,highlightbackground="blue",highlightthickness=2)
menuframe.pack(side="left")

movelistframe = Frame(menuframe,highlightbackground="green",highlightthickness=2)
movelistframe.pack(side="top")

movelabels = []
for i in range(4):
    for j in range(16):
        movelabels.append(Label(movelistframe,text=f"{16*i+j}",highlightbackground="red",highlightthickness=2))
        movelabels[16*i+j].grid(row=j,column=i)

def updateMoveListText(movenumber,labellist,knightwalk):
    for i in range(1,65):
        if i <= movenumber:
            labellist[i-1].config(text=f"{i}. a4")
        else:
            labellist[i-1].config(text="")


def placeKnight(square):
    # only used when placing the knight on the starting square
    x = SQUARE_SIZE*square[0]+PAD
    y = SQUARE_SIZE*(7-square[1])+PAD
    Icon = boardcanvas.create_image(x,y,anchor=NW,image=knightImg)
    return Icon

def updateKnightPos(oldIcon,square,movenumber):
    # this is a bit scuffed ig, have to save new knight as the output
    # this function.
    x = SQUARE_SIZE*square[0]+PAD
    y = SQUARE_SIZE*(7-square[1])+PAD
    boardcanvas.delete(oldIcon)
    newIcon = boardcanvas.create_image(x,y,anchor=NW,image=knightImg)
    return newIcon

def displayMoveNumber(knightwalk,movenumber):
    # displays the board after move moves of the knightwalk
    # maybe wipe?
    for i in range(movenumber-1):
        xcoord,ycoord = knightwalk[i]
        x = SQUARE_SIZE*xcoord+PAD
        y = SQUARE_SIZE*ycoord+PAD
        

def displayWalk(knightWalk):
    # read in the knightwalk and do everything graphics-related with it
    startingSquare = knightWalk[0]
    
    knightIcon = placeKnight(startingSquare)
    for move in range(1,len(knightWalk)):
        tk_sleep(0.2)
        knightIcon = updateKnightPos(knightIcon,knightWalk[move],move)


# test to see if anything works
knightWalk = [(0,0),(1,2),(2,4),(4,5),(5,3),(3,4)]
#displayWalk(knightWalk)

updateMoveListText(4,movelabels,knightWalk)

root.mainloop()

from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Springarvandring")
root.geometry("1000x800+0+0")
root.resizable(0,0)
#root.rowconfigure(0, weight=1)
#root.columnconfigure(0, weight=1)

# apparently time.sleep() doesn't work with tkinter stuff, use this one
def tk_sleep(time_s):
    time_ms = int(time_s*1000)
    variable = IntVar(root)
    root.after(time_ms, lambda: variable.set(1))
    root.wait_variable(variable)



leftframe = Frame(root,highlightbackground="black",highlightthickness=2)
leftframe.pack(side="left")


boardcanvas = Canvas(leftframe,highlightbackground="blue",highlightthickness=2,width=640,height=640)
boardcanvas.pack(padx=(20,20),pady=(20,20))

for i in range(8):
    boardcanvas.create_text((10,75*i+57.5),text=str(8-i),anchor=CENTER)
    boardcanvas.create_text((57.5+75*i,630),text=chr(97+i),anchor=CENTER)

xoffset = 20
yoffset = 20
for i in range(8):
    for j in range(8):
        x1 = xoffset+75*i
        y1 = yoffset+75*j
        x2 = x1+75
        y2 = y1+75
        if (i+j) % 2 == 0:
            boardcanvas.create_rectangle(x1,y1,x2,y2,fill="#edce93")
        else:
            boardcanvas.create_rectangle(x1,y1,x2,y2,fill="#a8720a")

bottomframe = Frame(leftframe,highlightbackground="blue",highlightthickness=2)
bottomframe.pack(side="bottom")
prevMoveButton = Button(bottomframe, text="<-").pack(side="left")
nextMoveButton = Button(bottomframe, text="->").pack(side="left")

menuframe = Frame(root,highlightbackground="blue",highlightthickness=2)
menuframe.pack(side="left")

randomWalkButton = Button(menuframe, text="Generera slumpad vandring")
inputWalkButton = Button(menuframe, text="Skriv in din egen vandring")
completeWalkButton = Button(menuframe, text="Besök alla rutor")
randomWalkButton.pack()
inputWalkButton.pack()
completeWalkButton.pack()



# test to see if anything works
knightWalk = [(0,0),(1,2),(2,4),(4,5),(5,3),(3,4)]

# the image has the same dimensions as a square: 75x75
knightImg = PhotoImage(file="yes.png")


def placeKnight(square):
    # change the square to include the picture of the knight
    # instead of nothing
    x = 75*square[0]+xoffset
    y = 75*(7-square[1])+yoffset
    Icon = boardcanvas.create_image(x,y,anchor=NW,image=knightImg)
    return Icon

def updateKnightPos(oldIcon,square,movenumber):
    x = 75*square[0]+xoffset
    y = 75*(7-square[1])+yoffset   
    boardcanvas.delete(oldIcon)
    newIcon = boardcanvas.create_image(x,y,anchor=NW,image=knightImg)
    return newIcon

def displayWalk(knightWalk):
    # read in the knightwalk and do everything graphics-related with it
    
    startingSquare = knightWalk[0]
    
    knightIcon = placeKnight(startingSquare)
    for move in range(1,len(knightWalk)):
        tk_sleep(0.5)
        knightIcon = updateKnightPos(knightIcon,knightWalk[move],move)


displayWalk(knightWalk)

root.mainloop()


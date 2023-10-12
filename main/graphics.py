from tkinter import *
from tkinter import ttk

# apparently time.sleep() doesn't work with tkinter stuff, use this one
def tk_sleep(time_s):
    time_ms = int(time_s*1000)
    variable = IntVar(root)
    root.after(time_ms, lambda: variable.set(1))
    root.wait_variable(variable)

# i think this class is pretty nice
class Knightwalk:
    def __init__(self,walk,board):
        self.movenumber = 1 # this one is 1-indexed ig
        self.walk = walk
        x = SQUARE_SIZE*walk[0][0]+PAD
        y = SQUARE_SIZE*(7-walk[0][1])+PAD
        self.canvas = board 
        self.knightIcon = self.canvas.create_image(x,y,anchor=NW,image=knightImg)
    
    def CurrSquare(self):
        return self.walk[self.movenumber-1]

    def moveForward(self):
        oldSquare = self.CurrSquare()
        self.movenumber += 1
        newSquare = self.CurrSquare()
        x = SQUARE_SIZE*newSquare[0]+PAD
        y = SQUARE_SIZE*(7-newSquare[1])+PAD
        
        self.canvas.delete(self.knightIcon)
        self.knightIcon = self.canvas.create_image(x,y,anchor=NW,image=knightImg)

    def moveBackward(self):
        oldSquare = self.CurrSquare()
        self.movenumber -= 1
        newSquare = self.CurrSquare()
        x = SQUARE_SIZE*newSquare[0]+PAD
        y = SQUARE_SIZE*(7-newSquare[1])+PAD
        
        self.canvas.delete(self.knightIcon)
        self.knightIcon = self.canvas.create_image(x,y,anchor=NW,image=knightImg)


# initialise basic window
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
knightImg = PhotoImage(file="yes.png") #image has same dim as a square


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

menuframe = Frame(root,highlightbackground="blue",highlightthickness=2)
menuframe.pack(side="left")

movelistframe = Frame(menuframe,highlightbackground="green",highlightthickness=2)
movelistframe.pack(side="top")

movelabels = []
for i in range(4):
    for j in range(16):
        movelabels.append(Label(movelistframe,text=""))
        movelabels[16*i+j].grid(row=j,column=i)


knightWalk = Knightwalk([(0,0),(1,2),(2,4),(4,5),(5,3),(3,4)], boardcanvas)

def moveBackwardButtonFn(knightwalk):
    knightwalk.moveBackward()

def moveForwardButtonFn(knightwalk):
    knightwalk.moveForward()

bottomframe = Frame(leftframe)
bottomframe.pack(side="bottom")
prevMoveButton = Button(bottomframe, text="<-", command=lambda: moveBackwardButtonFn(knightWalk))
prevMoveButton.pack(side="left")
nextMoveButton = Button(bottomframe, text="->", command=lambda: moveForwardButtonFn(knightWalk))
nextMoveButton.pack(side="left")


def coordsToSquare(coords):
    reverseMap = list('abcdefgh')
    return reverseMap[coords[0]]+str(coords[1]+1)

def displayMoveList(labellist,walk):
    for i in range(len(walk)):
        coords = walk[i]
        labellist[i].config(text=f"{i+1}. {coordsToSquare(coords)}")

def showCurrentMove(labellist,movenumber): #movenumber is 1-indexed ig
    labellist[movenumber-1].config(highlightbackground="red",highlightthickness=2)
    # also make sure the other ones don't have a red box


def displayWalk(knightWalk):
    # change this entirely
    startingSquare = knightWalk[0]
    
    knightIcon = placeKnight(startingSquare)
    for move in range(1,len(knightWalk)):
        tk_sleep(0.2)
        knightIcon = updateKnightPos(knightIcon,knightWalk[move],move)


# test to see if anything works

#displayMoveList(movelabels,knightWalk.walk)
#showCurrentMove(movelabels,knightWalk.movenumber)




root.mainloop()


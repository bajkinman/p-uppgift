from tkinter import *
from tkinter import ttk
from idk import *

#TESTWALK = [(0, 0), (2, 1), (0, 2), (1, 0), (3, 1), (5, 0), (7, 1), (6, 3), (7, 5), (6, 7), (4, 6), (2, 7), (0, 6), (1, 4), (2, 6), (0, 7), (1, 5), (0, 3), (1, 1), (3, 0), (4, 2), (6, 1), (4, 0), (5, 2), (7, 3), (5, 4), (6, 6), (4, 7), (3, 5), (2, 3), (0, 4), (1, 6), (3, 7), (5, 6), (7, 7), (6, 5), (4, 4), (2, 5), (1, 7), (0, 5), (1, 3), (0, 1), (2, 0), (1, 2), (3, 3), (4, 1), (6, 0), (7, 2), (5, 1), (7, 0), (6, 2), (7, 4), (5, 3), (3, 2), (2, 4), (3, 6), (5, 7), (4, 5), (6, 4), (7, 6), (5, 5), (4, 3), (2, 2), (3, 4)]

TESTWALK = menu()


# function that makes screen sleep for a while, might not need this
def tk_sleep(time_s):
    time_ms = int(time_s*1000)
    variable = IntVar(root)
    root.after(time_ms, lambda: variable.set(1))
    root.wait_variable(variable)

# square conversion, this is already in idk.py so won't need this one
def coordsToSquare(coords):
    reverseMap = list('abcdefgh')
    return reverseMap[coords[0]]+str(coords[1]+1)

# i think this class is pretty nice
class Knightwalk:
    def __init__(self,walk,board):
        self.movenumber = 1 # this one is 1-indexed ig
        self.walk = walk
        x = SQUARE_SIZE*(0.5+walk[0][0])+PAD
        y = SQUARE_SIZE*(7.5-walk[0][1])+PAD
        self.canvas = board
        self.knightIcon = self.canvas.create_image(x,y,anchor=CENTER,image=knightImg)
        self.numberIcons = []

    def CurrSquare(self):
        return self.walk[self.movenumber-1]

    def moveForward(self):
        if self.movenumber == len(self.walk):
            # we should not be allowed to move forward
            return

        oldSquare = self.CurrSquare()
        self.movenumber += 1
        newSquare = self.CurrSquare()
        oldx = SQUARE_SIZE*(0.5+oldSquare[0])+PAD
        oldy = SQUARE_SIZE*(7.5-oldSquare[1])+PAD
        newx = SQUARE_SIZE*(0.5+newSquare[0])+PAD
        newy = SQUARE_SIZE*(7.5-newSquare[1])+PAD
        
        self.canvas.delete(self.knightIcon)
        self.knightIcon = self.canvas.create_image(newx,newy,anchor=CENTER,image=knightImg)
        textIcon = self.canvas.create_text(oldx,oldy,anchor=CENTER,text=f"{self.movenumber-1}",font=("Helvetica 20 bold"))
        self.numberIcons.append(textIcon)

    def moveBackward(self):
        if self.movenumber == 1:
            # we should not be allowed to move backward
            return

        oldSquare = self.CurrSquare()
        self.movenumber -= 1
        newSquare = self.CurrSquare()
        newx = SQUARE_SIZE*(0.5+newSquare[0])+PAD
        newy = SQUARE_SIZE*(7.5-newSquare[1])+PAD
        
        self.canvas.delete(self.knightIcon)
        self.knightIcon = self.canvas.create_image(newx,newy,anchor=CENTER,image=knightImg)
        self.canvas.delete(self.numberIcons[-1])
        self.numberIcons.pop()


class Movelist:
    def __init__(self,knightwalk):
        self.knightwalk = knightwalk
        self.movelabels = []
        for i in range(4):
            for j in range(16):
                self.movelabels.append(Label(movelistframe,text="     "))
                self.movelabels[16*i+j].grid(row=j,column=i,padx=2)
        for i in range(len(knightwalk.walk)):
            coords = self.knightwalk.walk[i]
            self.movelabels[i].config(text=f"{i+1}. {coordsToSquare(coords)}")
            self.movelabels[i].config(highlightbackground=BG_COLOUR,highlightthickness=1.5)
        self.movelabels[self.knightwalk.movenumber-1].config(highlightbackground="red",highlightthickness=1.5)
    
    def showCurrMove(self): #movenumber is 1-indexed ig
        for i in range(64):
            if i == self.knightwalk.movenumber-1:
                colour="red"
            else:
                colour = BG_COLOUR
            self.movelabels[i].config(highlightbackground=colour,highlightthickness=1.5)


def moveBackwardButtonFn(knightwalk,movelist):
    knightwalk.moveBackward()
    movelist.showCurrMove()

def moveForwardButtonFn(knightwalk,movelist):
    knightwalk.moveForward()
    movelist.showCurrMove()

# initialise basic window
root = Tk()
root.title("Springarvandring")
root.geometry("1000x800+0+0")
#root.configure(bg="#d0d1d6")
root.resizable(0,0)

# constants
SQUARE_SIZE = 75
PAD = 20
BOARD_DIM = 2*PAD+8*SQUARE_SIZE
BG_COLOUR = root.cget("bg") #apparently this colour varies across operating systems
LIGHT_COLOUR = "#edce93"
DARK_COLOUR = "#a8720a"
knightImg = PhotoImage(file="yes.png") #image has same dimensions as a square

# frame that contains the board and the buttons below to step forward or backward
leftframe = Frame(root)
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

menuframe = Frame(root)
menuframe.pack(side="left")
text1="Tryck på höger- och vänsterpilen på \n"
text2="tangentbordet för att stega fram respektive \n"
text3="bak, alternativt använd knapparna under brädet."
menutext = Label(menuframe,text=text1+text2+text3)
menutext.pack(side="top")

movelistframe = Frame(menuframe,highlightbackground="grey",highlightthickness=2)
movelistframe.pack(side="top",pady=10)

# these are very important
knightWalk = Knightwalk(TESTWALK, boardcanvas)
moveList = Movelist(knightWalk)


bottomframe = Frame(leftframe)
bottomframe.pack(side="bottom")
prevMoveButton = Button(bottomframe, text="<-", command=lambda: moveBackwardButtonFn(knightWalk,moveList))
prevMoveButton.pack(side="left")
nextMoveButton = Button(bottomframe, text="->", command=lambda: moveForwardButtonFn(knightWalk,moveList))
nextMoveButton.pack(side="left")

root.bind("<Left>", lambda event: moveBackwardButtonFn(knightWalk,moveList))
root.bind("<Right>", lambda event: moveForwardButtonFn(knightWalk,moveList))


root.mainloop()


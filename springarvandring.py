import os
from random import choice, shuffle
from tkinter import *

# konstanter
SQUARE_SIZE = 75
PAD = 20
BOARD_DIM = 2*PAD+8*SQUARE_SIZE
BG_COLOUR = "#d9d9d9"
LIGHT_COLOUR = "#edce93"
DARK_COLOUR = "#a8720a"
imgPath = os.path.join("pictures","icon.png") # springarens ikon, den har samma dimensioner som en ruta

#TESTWALK = [(0, 0), (2, 1), (0, 2), (1, 0), (3, 1), (5, 0), (7, 1), (6, 3), (7, 5), (6, 7), (4, 6), (2, 7), (0, 6), (1, 4), (2, 6), (0, 7), (1, 5), (0, 3), (1, 1), (3, 0), (4, 2), (6, 1), (4, 0), (5, 2), (7, 3), (5, 4), (6, 6), (4, 7), (3, 5), (2, 3), (0, 4), (1, 6), (3, 7), (5, 6), (7, 7), (6, 5), (4, 4), (2, 5), (1, 7), (0, 5), (1, 3), (0, 1), (2, 0), (1, 2), (3, 3), (4, 1), (6, 0), (7, 2), (5, 1), (7, 0), (6, 2), (7, 4), (5, 3), (3, 2), (2, 4), (3, 6), (5, 7), (4, 5), (6, 4), (7, 6), (5, 5), (4, 3), (2, 2), (3, 4)]

# Board-klassen ska hålla koll på allt som sker medan springarvandringen genereras,
# det är alltså inget bräde som kommer visas grafiskt utan finns endast för att kunna
# hålla koll på springarens position under generering av vandring
class Board:
    def __init__(self):
        self.xpos = -1
        self.ypos = -1
        self.visited = [[False for _ in range(8)] for _ in range(8)]
        self.knightWalk = []

    def setKnightPos(self,square):
        self.xpos = square[0]
        self.ypos = square[1]
        self.knightWalk.append((self.xpos,self.ypos))
        self.visited[self.ypos][self.xpos] = True

    def wipe(self):
        self.visited = [[False for _ in range(8)] for _ in range(8)]
        self.xpos = -1
        self.ypos = -1
        self.knightWalk = []

    def legalMoves(self):
        legal = [] 
        moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        for x,y in moves:
            if 0 <= self.xpos+x <= 7 and 0 <= self.ypos+y <= 7:
                legal.append((self.xpos+x,self.ypos+y))
        return legal

    def notVisitedMoves(self):
        available = []
        for x,y in self.legalMoves():
            if not self.visited[y][x]:
                available.append((x,y))
        return available
    
    def moveKnight(self,square):
        if square not in self.legalMoves():
            print("Ej tillåtet drag, försök igen")
            return False

        if self.visited[square[1]][square[0]]:
            print("Redan besökt, försök igen")
            return False

        self.xpos = square[0]
        self.ypos = square[1]
        self.visited[self.ypos][self.xpos] = True
        self.knightWalk.append((self.xpos,self.ypos))
        return True

    def undoLastMove(self):
        xremove,yremove = self.knightWalk.pop()
        self.visited[yremove][xremove] = False
        self.xpos,self.ypos = self.knightWalk[-1]


# denna klass innehåller de funktioner för att grafiskt visa
# vandringen på schackbrädet
# ett Knightwalk-objekt skapas i __init__ av Graphics-klassen
class Knightwalk:
    def __init__(self,walk,board):
        self.movenumber = 1 # notera 1-indexering
        self.walk = walk
        x = SQUARE_SIZE*(0.5+walk[0][0])+PAD
        y = SQUARE_SIZE*(7.5-walk[0][1])+PAD
        self.canvas = board
        self.knightImg = PhotoImage(file=imgPath)
        self.knightIcon = self.canvas.create_image(x,y,anchor=CENTER,image=self.knightImg)
        self.numberIcons = []

    def CurrSquare(self):
        return self.walk[self.movenumber-1]

    def moveForward(self):
        if self.movenumber == len(self.walk):
            return # vi ska inte få gå framåt

        oldSquare = self.CurrSquare()
        self.movenumber += 1
        # efter att movenumber har ändrats ändras även det som
        # CurrSquare() returnerar
        newSquare = self.CurrSquare()
        oldx = SQUARE_SIZE*(0.5+oldSquare[0])+PAD
        oldy = SQUARE_SIZE*(7.5-oldSquare[1])+PAD
        newx = SQUARE_SIZE*(0.5+newSquare[0])+PAD
        newy = SQUARE_SIZE*(7.5-newSquare[1])+PAD
       
        # ta bort gamla springarikonen, skapa en ny på den nya rutan, sätt på gamla rutan istället en siffra
        self.canvas.delete(self.knightIcon)
        self.knightIcon = self.canvas.create_image(newx,newy,anchor=CENTER,image=self.knightImg)
        textIcon = self.canvas.create_text(oldx,oldy,anchor=CENTER,text=f"{self.movenumber-1}",font=("Helvetica 20 bold"))
        self.numberIcons.append(textIcon)

    def moveBackward(self):
        if self.movenumber == 1:
            return # vi ska inte få gå bakåt

        oldSquare = self.CurrSquare()
        self.movenumber -= 1
        newSquare = self.CurrSquare()
        newx = SQUARE_SIZE*(0.5+newSquare[0])+PAD
        newy = SQUARE_SIZE*(7.5-newSquare[1])+PAD
       
        # ta bort gamla springarikonen, skapa en ny på den nya rutan, ta bort en siffra
        self.canvas.delete(self.knightIcon)
        self.knightIcon = self.canvas.create_image(newx,newy,anchor=CENTER,image=self.knightImg)
        self.canvas.delete(self.numberIcons[-1])
        self.numberIcons.pop()


# denna klass uppdaterar listan till höger i det grafiska fönstret, som visar de drag som
# vandringen består av. Ett Movelist-objekt skapas i __init__ av Graphics-klassen
class Movelist:
    def __init__(self,knightwalk,frame):
        self.knightwalk = knightwalk
        self.movelabels = []
        self.movelistframe = frame
        for i in range(4):
            for j in range(16):
                self.movelabels.append(Label(self.movelistframe,text="     "))
                self.movelabels[16*i+j].grid(row=j,column=i,padx=2)
        for i in range(len(knightwalk.walk)):
            coords = self.knightwalk.walk[i]
            self.movelabels[i].config(text=f"{i+1}. {coordsToSquare(coords)}")
            self.movelabels[i].config(highlightbackground=BG_COLOUR,highlightthickness=1.5)
        self.movelabels[self.knightwalk.movenumber-1].config(highlightbackground="red",highlightthickness=1.5)
    
    def showCurrMove(self):
        for i in range(64):
            if i == self.knightwalk.movenumber-1:
                colour="red"
            else:
                colour = BG_COLOUR
            self.movelabels[i].config(highlightbackground=colour,highlightthickness=1.5)


# en klass för grafikfönstret
class Graphics:
    def __init__(self, Walk):
        self.root = Tk()
        self.root.title("Springarens vandring på schackbrädet")
        self.root.geometry("1000x800+0+0")
        self.root.resizable(0,0)
        self.walk = Walk

        # ram som innehåller brädet samt de två knapparna under brädet för att flytta springaren
        self.leftframe = Frame(self.root)
        self.leftframe.pack(side="left")
        
        # boardcanvas är där brädets rutor och springaren visas och uppdateras
        self.boardcanvas = Canvas(self.leftframe,width=BOARD_DIM,height=BOARD_DIM)
        self.boardcanvas.pack(padx=(PAD,PAD),pady=(PAD,PAD))
        for i in range(8):
            self.boardcanvas.create_text((PAD/2,SQUARE_SIZE*(i+0.5)+PAD),text=str(8-i),anchor=CENTER)
            self.boardcanvas.create_text((SQUARE_SIZE*(i+0.5)+PAD,BOARD_DIM-PAD/2),text=chr(97+i),anchor=CENTER)

        for i in range(8):
            for j in range(8):
                x1 = PAD+SQUARE_SIZE*i
                y1 = PAD+SQUARE_SIZE*j
                x2 = x1+SQUARE_SIZE
                y2 = y1+SQUARE_SIZE
                if (i+j) % 2 == 0:
                    self.boardcanvas.create_rectangle(x1,y1,x2,y2,fill=LIGHT_COLOUR)
                else:
                    self.boardcanvas.create_rectangle(x1,y1,x2,y2,fill=DARK_COLOUR)

        # menuframe innehåller en label med text samt movelistframe
        self.menuframe = Frame(self.root)
        self.menuframe.pack(side="left")
        text1="Tryck på höger- och vänsterpilen på \n"
        text2="tangentbordet för att stega fram respektive \n"
        text3="bak, alternativt använd knapparna under brädet."
        self.menutext = Label(self.menuframe,text=text1+text2+text3)
        self.menutext.pack(side="top")
        
        # movelistframe innehåller listan med rutorna som ingår i vandringen
        self.movelistframe = Frame(self.menuframe,highlightbackground="grey",highlightthickness=2)
        self.movelistframe.pack(side="top",pady=10)

        # skapa objekt av klasserna Knightwalk och Movelist
        self.knightWalk = Knightwalk(self.walk, self.boardcanvas)
        self.moveList = Movelist(self.knightWalk, self.movelistframe)
        
        # ramen som innehåller de två knapparna
        self.bottomframe = Frame(self.leftframe)
        self.bottomframe.pack(side="bottom")
        self.prevMoveButton = Button(self.bottomframe, text="<-", command=lambda: self.moveBackwardFn())
        self.prevMoveButton.pack(side="left")
        self.nextMoveButton = Button(self.bottomframe, text="->", command=lambda: self.moveForwardFn())
        self.nextMoveButton.pack(side="left")
        
        # vänster- och högerpilen binds till samma funktion som de två knapparna
        self.root.bind("<Left>", lambda event: self.moveBackwardFn())
        self.root.bind("<Right>", lambda event: self.moveForwardFn())

        self.root.mainloop()

    def moveBackwardFn(self):
        self.knightWalk.moveBackward()
        self.moveList.showCurrMove()

    def moveForwardFn(self):
        self.knightWalk.moveForward()
        self.moveList.showCurrMove()


#några simpla funktioner som underlättar behandling av indata
def squareToCoords(square):
    columnMap = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7 }
    return (columnMap[square[0]],int(square[1])-1)

def coordsToSquare(coords):
    reverseMap = list('abcdefgh')
    return reverseMap[coords[0]]+str(coords[1]+1)

def validSquareInput(square):
    if len(square) != 2 or square[0] not in list('abcdefgh') or square[1] not in ['1','2','3','4','5','6','7','8']:
        print("Inte en schackruta, försök igen")
        return False
    return True

def getStartingSquare(board):
    validInput = False
    while not validInput:
        startSquare = input("Skriv in rutan som vandringen börjar på: ")
        validInput = validSquareInput(startSquare)
    return squareToCoords(startSquare)


#huvudmenyn, här sker läsning av indata från användaren
def menu():
    print()
    print("Välkommen till \"Springarens vandring på schackbrädet\"")
    print("Programmet kommer gå ut på att generera en springarvandring på ett")
    print("schackbräde, som sedan kommer visas grafiskt där du kan stega fram")
    print("och tillbaka i vandringen")
    print("-"*15+"Menyval"+"-"*15)
    print("Skriv in 1 för att generera en slumpmässig vandring")
    print("Skriv in 2 för att skriva in din egna vandring")
    print("Skriv in 3 för att generera en vandring som besöker varje ruta")
    print("Skriv in q för att avsluta programmet")
    validChoice = False
    while not validChoice:
        choice = input("Ditt val: ")
        if choice in ["1","2","3","q"]:
            break
        else:
            print("Ej tillåtet val, försök igen")
    
    board = Board()
    walk = []
    if choice == "1":
        print("-"*40)
        print("Datorn kommer slumpmässigt generera en vandring, låt oss se hur långt den kommer")
        startingSquare = getStartingSquare(board)
        walk = randomWalk(board,startingSquare)

    elif choice == "2":
        print("-"*40)
        print("Skriv in din egna vandring och få den visad på brädet")
        print("Skriv in rutorna som springaren besöker i vandringen, i den ordning de besöks")
        print("Vandringen ska bestå av tillåtna springardrag, och ingen ruta får besökas mer än en gång")

        wanthelp = input("Ska datorn visa tillåtna drag när du skriver in vandringen (y/n)? ")
        walk = inputWalk(board,wanthelp)

    elif choice == "3":
        print("-"*40)
        print("Datorn kommer generera en vandring som börjar i vilken ruta du vill")
        print("och sedan besöker varje ruta exakt en gång")
        
        startingSquare = getStartingSquare(board)
        walk = completeWalk(board,startingSquare)
    
    elif choice == "q":
        print("-"*7+"Avslutar programmet"+"-"*7)
    
    return walk

# nu följer de tre valen: slumpmässig vandring, egeninmatad vandring, och komplett vandring

# generera nästa drag genom att slumpmässigt välja bland de tillåtna samt ej besökta rutorna
# vandringen slutar när ingen obesökt tillåten ruta finns
def randomWalk(board,start): 
    board.setKnightPos(start)
    while True:
        moveCandidates = board.notVisitedMoves()
        if len(moveCandidates) == 0:
            break
        nextmove = choice(moveCandidates)
        board.moveKnight(nextmove)
    return board.knightWalk


def inputWalk(board,showValidMoves = 'n'):
    # kontrollera att antalet rutor är rimligt för en springarvandring
    validInput = False
    while not validInput:
        numberOfSquares = input("Ange antalet rutor i din vandring: ")
        try:
            numberOfSquares = int(numberOfSquares)
        except Exception:
            numberOfSquares = -1
           
        if 1 <= int(numberOfSquares) <= 64:
                validInput = True
        else:
            print("Ogiltig indata, försök igen")
   
    board.setKnightPos(getStartingSquare(board))

    # for-slinga för att läsa in ett drag i taget
    for squareNumber in range(2,numberOfSquares+1):
        if showValidMoves == 'y':
            print("Tillgängliga rutor:",*[coordsToSquare(square) for square in board.notVisitedMoves()])
        validInput = False
        while not validInput:
            nextSquare = input(f"Ange ruta nummer {squareNumber} av din vandring: ")
            validInput = validSquareInput(nextSquare)
            validInput = board.moveKnight(squareToCoords(nextSquare))
    
    return board.knightWalk

# denna algoritm heter Warnsdorffs algoritm, och den är
# egentligen endast en heuristik som ofta fungerar.
# därför kör vi algoritmen och om den inte genererar en komplett vandring
# kör vi om den. Genereringen av nästa drag innehåller ett slumpelement,
# så till slut kommer en komplett vandring hittas.
def completeWalk(board,start):
    foundWalk = False
    while not foundWalk:
        board.wipe()
        board.setKnightPos(start)
        for i in range(63):
            moves = board.notVisitedMoves()
            if len(moves) == 0:
                break
             
            topcandidate = -1
            minimumMoves = 9
            shuffle(moves)
            # loopa igenom tillåtna drag, flytta springaren till varje "kandidatruta" och se därifrån
            # hur många rutor den kan gå till. Warnsdorffs algoritms säger att välja den
            # kandidatrutan som tillåter minst antal olika drag
            for move in moves:
                board.moveKnight(move)
                childMoves = len(board.notVisitedMoves())-1
                board.undoLastMove()
                if childMoves < minimumMoves:
                    minimumMoves = childMoves
                    topCandidate = move
            board.moveKnight(topCandidate)

        cond = True
        # kolla om alla rutor är besökta, om ja sätts foundWalk=True,
        # vilket avslutar while-slingan och returnerar vandringen board.knightWalk
        for row in board.visited:
            if sum(row) < 8:
                cond = False
                break
        if cond:
            foundWalk = True

    return board.knightWalk

# huvudprogrammet
knightwalk = menu()
if knightwalk:
    g = Graphics(knightwalk)


from random import choice

class Board:
    def __init__(self):
        self.squares = [["." for _ in range(8)] for _ in range(8)]
        self.knightx = -1
        self.knighty = -1
        self.visited = [[False for _ in range(8)] for _ in range(8)]
        self.movenumber = 0
        self.xpos = initialpos[0]
        self.ypos = initialpos[1]

    def setKnightPos(self,square):
        self.knightx = square[0]
        self.knighty = square[1]
        self.squares[y][x] = "N"
        self.visited[y][x] = True

    def wipe(self):
        self.squares = [["." for _ in range(8)] for _ in range(8)]
        self.visited = [[False for _ in range(8)] for _ in range(8)]

    def legalmoves(self):
        legal = set()
        moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        for x,y in moves:
            if 0 <= self.xpos+x <= 7 and 0 <= self.ypos+y <= 7:
                legal.add((self.xpos+x,self.ypos+y))
        return legal

    def notVisitedMoves(self):
        available = set()
        for x,y in self.legalmoves():
            if not self.visited[y][x]:
                available.add((x,y))
        return available
    
    def moveKnight(self,square):
        if square not in self.legalmoves():
            print("not a legal move, try again")
            return

        if board.visited[square[1]][square[0]]:
            print("already visited, try again")
            return

        self.movenumber += 1
        self.xpos = square[0]
        self.ypos = square[1]
        self.squares[self.ypos][self.xpos] = str(movenumber)
        self.squares[self.ypos][self.xpos] = "N"
        self.visited[self.ypos][self.xpos] = True

    def printBoard(self):
        print("-"*41)
        print("|   "+"-"*33+"   |")
        for i in range(7,-1,-1):
            print(f"|{i+1}  ",end="")
            for j in range(8):
                print("|"+" "*(2-len(self.squares[i][j]))+self.squares[i][j]+" ",end="")
            print("|   |")
            print("|   "+"-"*33+"   |")
        print("|     A   B   C   D   E   F   G   H     |")
        print("-"*41)


def menu():
    print("hello blablabla")
    print("Enter 1 to compute a random walk")
    print("Enter 2 to input your own walk")
    print("Enter 3 to compute a walk that visits every square")
    print("Enter q to quit")
    validChoice = False
    while not validChoice:
        choice = input("Your choice: ")
        if choice in ["1","2","3"]:
            break
        elif choice == "q":
            print("-"*7+"Exiting out of the program"+"-"*7)
            exit()
        else:
            print("Invalid input, try again")
    if choice == "1":
        print("-"*40)
        print("The computer will generate a random walk, let's see how far it gets (probably not very far)")
        randomWalk()
    elif choice == "2":
        print("-"*40)
        print("Input your own walk and have it shown on the board.")
        print("Enter the walk in the format of the squares in the order that the knight visits them.")
        wanthelp = input("Do you want the computer to show the valid moves when you enter the walk (y/n)? ")
        inputWalk(wanthelp)
    elif choice == "3":
        completeWalk()


def squareToCoords(square):
    columnMap = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7 }
    return columnmap[square[0]],int(square[1])-1


def validSquareInput(square):
    if len(square) != 2 or square[0] not in list('abcdefgh') or square[1] not in list(*range(8)):
        print("Invalid input square, try again")
        return False
    return True


def randomWalk(): 
    # generate next move randomly by choosing uniformly from the not visited legal moves
    board = Board()
    validInput = False
    while not validInput:
        startSquare = input("Enter the square that the computer starts the path from: ")
        validInput = validSquareInput(startSquare)
    
    board.setKnightPos(startSquare)

    while True:
        moveCandidates = board.notVisitedMoves()
        if len(moveCandidates) == 0:
            break
        nextmove = choice(tuple(moveCandidates))
        board.moveKnight(nextmove,numberofmoves)
    print("Resulting path:")
    board.printBoard()
    input("Enter anything to return back to the menu")


def inputWalk(showValidMoves = 'n'):
    # change so that they start by specifying the starting square
    # and then the number of moves (0 <= moves <= 63)
    validInput = False
    while not validInput:
        numberOfSquares = input("Enter the number of squares in your walk (or q to quit to menu): ")
        try:
            int(numberOfSquares)
        except ValueError:
            numberOfSquares = -1
            
        if 1 <= int(numberofsquares) <= 64:
                validinput = True
        else:
            print("Invalid input, try again")
    
    for movenumber in range(1,numberOfSquares):
        validInput = False
        while not validInput:
            nextSquare = input(f"Enter square number {movenumber} of your walk: ")
            validInput = validSquareInput(nextSquare)


# this algorithm is called Warnsdorff's algorithm and it's actually just a heuristic
# that often works. 
# it doesn't work if you start at g6: solution, just slightly change some choice if you die
# i have to fix this
def completeWalk(startx,starty,board,knight):
    for i in range(63):
        moves = knight.availableMoves(board.visited)
        minimumMoves = 9
        topCandidate = -1
        for candidateMove in moves:
            child = Knight(candidateMove)
            childMoves = len(child.availableMoves(board.visited))-1
            if childMoves < minimumMoves:
                minimumMoves = childMoves
                topCandidate = candidateMove
        knight.move(topCandidate, i+1)

    for row in board.visited:
        if sum(row) < 8:
            board.printBoard()
            break

menu()



"""
for initx in range(8):
    for inity in range(8):
        print(initx,inity)
        board.wipe()
        knight = Knight((initx,inity))
        board.setInitialKnightPos(initx,inity)

        completeWalk(knight.xpos,knight.ypos,board,knight)
"""


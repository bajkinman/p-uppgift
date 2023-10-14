from random import choice, shuffle

class Board:
    def __init__(self):
        self.squares = [["." for _ in range(8)] for _ in range(8)]
        self.visited = [[False for _ in range(8)] for _ in range(8)]
        self.moveNumber = 0
        self.xpos = -1
        self.ypos = -1
        self.knightWalk = []

    def setKnightPos(self,square):
        self.xpos = square[0]
        self.ypos = square[1]
        self.knightWalk.append((self.xpos,self.ypos))
        self.squares[self.ypos][self.xpos] = "N"
        self.visited[self.ypos][self.xpos] = True

    def wipe(self):
        self.squares = [["." for _ in range(8)] for _ in range(8)]
        self.visited = [[False for _ in range(8)] for _ in range(8)]
        self.moveNumber = 0
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
            print("not a legal move, try again")
            return False

        if self.visited[square[1]][square[0]]:
            print("already visited, try again")
            return False

        self.moveNumber += 1
        self.squares[self.ypos][self.xpos] = str(self.moveNumber)
        self.xpos = square[0]
        self.ypos = square[1]
        self.squares[self.ypos][self.xpos] = "N"
        self.visited[self.ypos][self.xpos] = True
        self.knightWalk.append((self.xpos,self.ypos))
        return True

    def undoLastMove(self):
        xremove,yremove = self.knightWalk.pop()
        self.visited[yremove][xremove] = False
        self.squares[yremove][xremove] = "."
        self.xpos,self.ypos = self.knightWalk[-1]
        self.squares[self.ypos][self.xpos] = "N"
        self.moveNumber -= 1

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
        

def squareToCoords(square):
    columnMap = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7 }
    return (columnMap[square[0]],int(square[1])-1)

def coordsToSquare(coords):
    reverseMap = list('abcdefgh')
    return reverseMap[coords[0]]+str(coords[1]+1)

def validSquareInput(square):
    if len(square) != 2 or square[0] not in list('abcdefgh') or square[1] not in ['1','2','3','4','5','6','7','8']:
        print("Invalid square, try again")
        return False
    return True

def getStartingSquare(board):
    validInput = False
    while not validInput:
        startSquare = input("Enter the starting square of the path: ")
        validInput = validSquareInput(startSquare)
    return squareToCoords(startSquare)

def menu():
    print("Enter 1 to compute a random walk")
    print("Enter 2 to input your own walk")
    print("Enter 3 to compute a walk that visits every square")
    print("Enter q to quit")
    validChoice = False
    while not validChoice:
        choice = input("Your choice: ")
        if choice in ["1","2","3","q"]:
            break
        else:
            print("Invalid input, try again")
    
    board = Board()
    if choice == "1":
        print("-"*40)
        print("The computer will generate a random walk, let's see how far it gets (probably not very far)")

        startingSquare = getStartingSquare(board)
        walk = randomWalk(board,startingSquare)

    elif choice == "2":
        print("-"*40)
        print("Input your own walk and have it shown on the board.")
        print("Enter the walk in the format of the squares in the order that the knight visits them.")
        print("The walk has to consist of legal moves for the knight, and no square may be visited")
        print("more than once.")

        wanthelp = input("Do you want the computer to show the valid moves when you enter the walk (y/n)? ")
        walk = inputWalk(board,wanthelp)

    elif choice == "3":
        print("-"*40)
        print("The computer will generete a walk that visits every square exactly once,")
        print("starting from any square you specify.")
        
        startingSquare = getStartingSquare(board)
        walk = completeWalk(board,startingSquare)
        print(walk)
    
    elif choice == "q":
        print("-"*7+"Exiting out of the program"+"-"*7)

def randomWalk(board,start): 
    # generate next move randomly by choosing uniformly from the not visited legal moves
    # it stops when it gets cornered
    board.setKnightPos(start)
    while True:
        moveCandidates = board.notVisitedMoves()
        if len(moveCandidates) == 0:
            break
        nextmove = choice(moveCandidates)
        board.moveKnight(nextmove)
    return board.knightWalk

# have to fix so that it actually checks if it's a valid knight path, it's pretty ez
def inputWalk(board,showValidMoves = 'n'):
    # change so that they start by specifying the starting square
    # and then the number of moves (0 <= moves <= 63)
    validInput = False
    while not validInput:
        numberOfSquares = input("Enter the number of squares in your walk (or q to quit to menu): ")
        if numberOfSquares == "q":
            return
        try:
            numberOfSquares = int(numberOfSquares)
        except Exception:
            numberOfSquares = -1
           
        if 1 <= int(numberOfSquares) <= 64:
                validInput = True
        else:
            print("Invalid input, try again")
   
    getStartingSquare(board)

    # loop through to get the rest of the squares
    for squareNumber in range(2,numberOfSquares+1):
        if showValidMoves == 'y':
            print("Available squares:",*[coordsToSquare(square) for square in board.notVisitedMoves()])
        validInput = False
        while not validInput:
            nextSquare = input(f"Enter square number {squareNumber} of your walk: ")
            validInput = validSquareInput(nextSquare)
            
            validInput = board.moveKnight(squareToCoords(nextSquare))
    
    return board.knightWalk


# this algorithm is called Warnsdorff's algorithm and it's actually just a heuristic
# that often works.
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
            # loop through moves, move knight to candidate square, check how many 
            # options it has there, store that number, then move back and proceed to next move.
            for move in moves:
                board.moveKnight(move)
                childMoves = len(board.notVisitedMoves())-1
                board.undoLastMove()
                if childMoves < minimumMoves:
                    minimumMoves = childMoves
                    topCandidate = move
            board.moveKnight(topCandidate)

        cond = True
        
        for row in board.visited:
            if sum(row) < 8:
                cond = False
                break
        if cond:
            foundWalk = True

    return board.knightWalk

menu()


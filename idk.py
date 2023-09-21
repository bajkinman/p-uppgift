import random 

class Knight:
    def __init__(self,initialpos):
        self.xpos = initialpos[0]
        self.ypos = initialpos[1]

    def legalmoves(self):
        legal = set()
        moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        for x,y in moves:
            if 0 <= self.xpos+x <= 7 and 0 <= self.ypos+y <= 7:
                legal.add((self.xpos+x,self.ypos+y))
        return legal

    def availableMoves(self, visitedList):
        available = set()
        for x,y in self.legalmoves():
            if not visitedList[y][x]:
                available.add((x,y))
        return available

    def move(self,square,movenumber):
        if square not in self.legalmoves():
            print("you are bad")
            return

        if board.visited[square[1]][square[0]]:
            print("already visited, try again")
            return
        self.xpos = square[0]
        self.ypos = square[1]
        board.updateKnightPos(self.xpos,self.ypos,movenumber)


class Board:
    def __init__(self):
        self.squares = [["." for _ in range(8)] for _ in range(8)]
        self.knightx = -1
        self.knighty = -1
        self.visited = [[False for _ in range(8)] for _ in range(8)]

    def setInitialKnightPos(self,x,y):
        self.knightx = x
        self.knighty = y
        self.squares[y][x] = "N"
        self.visited[y][x] = True

    def wipe(self):
        for row in self.squares:
            row = [0]*8

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

    def updateKnightPos(self, newx, newy, movenumber):
        self.squares[self.knighty][self.knightx] = str(movenumber)
        self.knightx = newx
        self.knighty = newy
        self.squares[self.knighty][self.knightx] = "N"
        self.visited[self.knighty][self.knightx] = True

# generate matrix to store the board.

board = Board()

column_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7 }
valid_inp = False
while not valid_inp:
    inp = input("Place the knight on some square (eg. a1): ")
    if len(inp) != 2 or inp[0] not in ['a','b','c','d','e','f','g','h'] or inp[1] not in ['1','2','3','4','5','6','7','8']:
        q = input("invalid input, press q to quit or any other key to try again")
        if q == 'q':
            exit()
    else:
        valid_inp = True

initx = column_map[inp[0]]
inity = int(inp[1])-1

knight = Knight((initx,inity))
board.setInitialKnightPos(initx,inity)

print("starting pos:",knight.xpos,knight.ypos)
"""
while True:
    print("legal moves:", knight.legalmoves())
    inp = input("Choose a direction for a move ")
    if inp == "quit":
        break
    inp = int(inp)
    knight.move(inp)
    print("new position:",knight.xpos,knight.ypos)
"""


def randomwalk(startx,starty,board,knight):
    numberofmoves = 0
    for i in range(100):
        legalmoves = knight.legalmoves()
        nextmove = random.choice(tuple(legalmoves))
        if not board.visited[nextmove[1]][nextmove[0]]:
            numberofmoves += 1
            knight.move(nextmove,numberofmoves)
    
    board.printBoard()


# a friend told me that this works, apparently the algorithm also has a name
# the alg is just that at each point, you look at all possible moves, and for those resulting
# squaers, the number of available moves. If you choose to move to the square with the minimum
# number of next moves available, then you will never corner yourself apparently
def knightPath(startx,starty,board,knight):
    for i in range(63):
        moves = knight.availableMoves(board.visited)
        minimumMoves = 9
        topCandidate = -1
        for candidateMove in moves:
            child = Knight(candidateMove)
            childMoves = len(child.availableMoves(board.visited))-1
            #don't want to count the square we're currently on, although it actually doesn't matter in this case
            if childMoves < minimumMoves:
                minimumMoves = childMoves
                topCandidate = candidateMove
        knight.move(topCandidate, i+1)

    board.printBoard()

knightPath(knight.xpos,knight.ypos,board,knight)


#randomwalk(knight.xpos,knight.ypos,board,knight)


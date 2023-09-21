# idk how classes work

import random 


class Knight:
    def __init__(self, initial_x,initial_y):
        self.xpos = initial_x
        self.ypos = initial_y

    def legalmoves(self):
        legal = set()
        for i in range(8):
            ex = ey = e = 0
            if i in {2,3,4,5}:
                ex = 1
            if i in {4,5,6,7}:
                ey = 1
            if i in {1,2,5,6}:
                e = 1

            x,y = int(2**(1-e)*(-1)**ex),int(2**e*(-1)**ey)
            
            if 0 <= self.xpos+x <= 7 and 0 <= self.ypos+y <= 7:
                legal.add(i)
        return legal

    def move(self,direction):
        if direction not in self.legalmoves():
            print("you are bad")
            return
        
        ex = ey = e = 0
        if direction in {2,3,4,5}:
            ex = 1
        if direction in {4,5,6,7}:
            ey = 1
        if direction in {1,2,5,6}:
            e = 1

        x,y = int(2**(1-e)*(-1)**ex),int(2**e*(-1)**ey)
        if board.visited[self.xpos+x][self.ypos+y]:
            print("already visited, try again")
            return
        self.xpos += x
        self.ypos += y
        board.updateKnightPos(self.xpos,self.ypos)


# maybe have a method named validmoves that returns the directions to which the knight legally can jump.
# think that might be quite nice actually, then i don't have to check all of this bs in the move method

class Board:
    def __init__(self):
        self.squares = [["0" for _ in range(8)] for _ in range(8)]
        self.knightx = -1
        self.knighty = -1
        self.visited = [[False for _ in range(8)] for _ in range(8)]

    def setInitialKnightPos(self,x,y):
        self.knightx = x
        self.knighty = y
        self.visited[x][y] = True

    def wipe(self):
        for row in self.squares:
            row = [0]*8

    def printBoard(self):
        print("-"*41)
        print("|   "+"-"*33+"   |")
        for i in range(8):
            print("|{}  ".format(i)+"| "+" | ".join(self.squares[i])+" |   |")
            print("|   "+"-"*33+"   |")
        print("|     A   B   C   D   E   F   G   H     |")
        print("-"*41)

    def updateKnightPos(self,newx, newy):
        self.squares[self.knightx][self.knighty] = "."
        self.knightx = newx
        self.knighty = newy
        self.squares[self.knightx][self.knighty] = "N"
        self.visited[self.knightx][self.knighty] = True

# generate matrix to store the board.

board = Board()

# testing move stuff
initx,inity = map(int,input("Place a knight: ").split())
knight = Knight(initx,inity)
board.setInitialKnightPos(initx,inity)
print("starting pos:",knight.xpos,knight.ypos)
while True:
    print("legal moves:", knight.legalmoves())
    inp = input("Choose a direction for a move ")
    if inp == "quit":
        break
    inp = int(inp)
    knight.move(inp)
    print("new position:",knight.xpos,knight.ypos)


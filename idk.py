# want a class: knight that has a method move(dir) which updates the pos of the
# knight which i guess is another method that just returns the current position of the knight.
# idk how classes work


import random #ig, idk why really


class Knight:
    def __init__(self, initialpos):
        self.pos = initialpos

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
            
            if 0 <= self.pos[0]+x <= 7 and 0 <= self.pos[1]+y <= 7:
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
        print("x,y",x,y)
        self.pos[0] += x
        self.pos[1] += y


# maybe have a method named validmoves that returns the directions to which the knight legally can jump.
# think that might be quite nice actually, then i don't have to check all of this bs in the move method

class Board:
    def __init__(self):
        self.rows = [["0" for i in range(8)] for i in range(8)]
        

    def wipe(self):
        for row in self.rows:
            row = [0]*8

    def printBoard(self):
        print("-"*41)
        print("|   "+"-"*33+"   |")
        for i in range(8):
            print("|{}  ".format(i)+"| "+" | ".join(self.rows[i])+" |   |")
            print("|   "+"-"*33+"   |")
        print("|     A   B   C   D   E   F   G   H     |")
        print("-"*41)

# generate matrix to store the board. Will record the visited positions later.

board = Board()

# testing move stuff
knight = Knight([0,0])
print("starting pos",knight.pos)
while True:
    print("legal moves:", knight.legalmoves())
    inp = input("Choose a direction for a move ")
    if inp == "quit":
        break
    inp = int(inp)
    knight.move(inp)
    print("new position:",knight.pos)


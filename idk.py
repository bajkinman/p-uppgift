# want a class: knight that has a method move(dir) which updates the pos of the
# knight which i guess is another method that just returns the current position of the knight.
# idk how classes work


import random #ig, idk why really


class Knight:
    def __init__(self, initialpos):
        self.pos = initialpos

    def move(self,direction): #direction should be an integer between 0 and 7
        
        if direction == 0: # >>^
            if self.pos[0]+2 >= 8 or self.pos[1]+1 >= 8:
                # invalid
                pass
            else:
                self.pos = (self.pos[0]+2,self.pos[1]+1)
        
        elif direction == 1: # ^^>
            if self.pos[0]+1 >= 8 or self.pos[1]+2 >= 8:
                # invalid
                pass
            else:
                self.pos = (self.pos[0]+1,self.pos[1]+2)
        
        elif direction == 2: # ^^<
            if self.pos[0]-1 < 0 or self.pos[1]+2 >= 8:
                # invalid
                pass
            else:
                self.pos = (self.pos[0]-1,self.pos[1]+2)
        
        elif direction == 3: # <<^
            if self.pos[0]-2 < 0 or self.pos[1]+1 >= 8:
                # invalid
                pass
            else:
                self.pos = (self.pos[0]-2,self.pos[1]+1)
        
        elif direction == 4: # <<v
            if self.pos[0]-2 < 0 or self.pos[1]-1 < 0:
                # invalid
                pass
            else:
                self.pos = (self.pos[0]-2,self.pos[1]-1)
        
        elif direction == 5: # vv<
            if self.pos[0]-1 < 0 or self.pos[1]-2 < 0:
                # invalid
                pass
            else:
                self.pos = (self.pos[0]-1,self.pos[1]-2)
        
        elif direction == 6: # vv>
            if self.pos[0]+1 >= 8 or self.pos[1]-2 < 0:
                # invalid
                pass
            else:
                self.pos = (self.pos[0]+1,self.pos[1]-2)
        
        elif direction == 7: # >>v
            if self.pos[0]+2 >= 8 or self.pos[1] < 0:
                # invalid
                pass
            else:
                self.pos = (self.pos[0]+2,self.pos[1]-1)
        else:
            # do something, say you are bad
            # return something
            pass

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

#board.printBoard()

"""
# testing move stuff

knight = Knight((0,0))
print(knight.pos)

knight.move(0)
knight.move(1)
print(knight.pos)
"""


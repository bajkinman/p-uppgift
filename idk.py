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


# generate matrix to store the board. Will record the visited positions later.

board = [[-1 for _ in range(8)] for _ in range(8)]

"""
# testing move stuff

knight = Knight((0,0))
print(knight.pos)

knight.move(0)
knight.move(1)
print(knight.pos)
"""


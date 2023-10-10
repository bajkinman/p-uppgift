from random import choice, shuffle
#import tkinter

class Board:
    def __init__(self):
        self.squares = [["." for _ in range(8)] for _ in range(8)]
        self.visited = [[False for _ in range(8)] for _ in range(8)]
        self.moveNumber = 0
        self.xpos = -1
        self.ypos = -1
        self.knightWalk = []

        # squares is a value stored for each square, it will be
        # a dot if the square has nnot been visited, a N if the
        # knight is currently placed there and a number if it has
        # been visited: the number will be the move number on
        # which the knight was placed there
        # visited is an array keeping track of which squares have
        # been visited, moveNumber is the current number of moves
        # that have been made, xpos and ypos are the knight's
        # current coordinates, and knightWalk is an array containing
        # all coordinates of the squares that so far have been visited
        # in the knightwalk.

    def setKnightPos(self,square):
        pass
        # sets the initial knight position on the board

    def wipe(self):
        pass
        # wipes the board back to an initial state, note
        # that there will be no knight placed anywhere
        # doesn't return  anything
    def legalMoves(self):
        pass
        # using the current position of the knight, generate
        # all legal moves and return them as a list.
        # return legalmoves

    def notVisitedMoves(self):
        pass
        # returns only those legal moves that jump to
        # squares that have not yet been visited in the
        # walk
    
    def moveKnight(self,square):
        pass
        # update the position of the knight, make
        # the new square visited, update the move counter
        # and add new square to self.knightWalk
        # doesn't return anything

    def undoLastMove(self):
        pass
        # undo the last knight move: update the position of
        # the knight using the list self.knightWalk, remove
        # the last entry of that list and set that square
        # to not visited, decrease self.moveNumber by 1.

    def printBoard(self):
        pass
        # print the board to the screen
        # once gui has been implemented, this will probably
        # not be needed as the board will always be shown
        # or if i decide to only print the result, then
        # i will still have this, and this is where a lot 
        # of the graphics will be (or probably outside the
        # board class actually idk).


def validSquareInput(square):
    pass
    # check if user submitted a valid chess coordinate for
    # the next move.
    # returns a boolean

def menu(): #returns a bool: true if user wants to quit the program
    # first reads an input into a variable choice that should be 1,2
    # or 3. Generates a board.
    choice = 1
    board = Board()
    if choice == "1":
        pass
        # run the function randomWalk()

    elif choice == "2":
        pass
        # run the function inputWalk()

    elif choice == "3":
        pass
        # run the function completeWalk()


def randomWalk(start,board): 
    # generate next move randomly by choosing uniformly from the not visited legal moves
    # it stops when it gets cornered
    
    # generate all not visited legal moves using board.notVisitedMoves() and pick one
    # move to make using random.choice()

def inputWalk():
    pass
    # change so that they start by specifying the starting square
    # and then the number of moves (0 <= moves <= 63)
    
    # user specifies starting square and number of moves, then
    # one move at a time writes in the next move as a chess coordinate
    # the moves are made on the board, and at the end, board.printBoard()
    # is called
   
# this algorithm is called Warnsdorff's algorithm and it's actually just a heuristic
# that often works. 
# if you have a fixed adjacency list, then on some starting squares the algorithm
# will not find a complete path: the solution is to randomly shuffle the order in
# which moves will be considered, and if by the end of the algorithm, no path has
# been found, just run it again.
def completeWalk(start,board): # start is the starting square of the complete walk
    # do the following until we have found a complete walk
    foundWalk = False
    while not foundWalk:
        # wipe the board and set the starting position.
        board.wipe()
        board.setKnightPos(start)
        
        # now run Warnsdorff's algorithm: generate the next move 63 times
        # by looking at all possible next moves, and taking the one that has the
        # least number of different available squares that we can move to after
        # that
        
        # check if the algorithm succeded and if so break, otherwise try running
        # the algorithm again. There is randomness in how the path is being
        # generated, so we will eventually find a path.

def main():
    user_quit = False
    while not user_quit:
        user_quit = menu()
        # run menu() function while the user wants to continue running the program.

# run main



# this algorithm is called Warnsdorff's algorithm and it's actually just a heuristic
# that often works. 
# if you have a fixed "adjacency list", then on some starting squares the algorithm
# will not find a complete path: the solution is to randomly shuffle the order in
# which moves will be considered, and if by the end of the algorithm, no path has
# been found, just run it again.
def completeWalk(start,board):
    foundWalk = False
    success = True
    while not foundWalk:
        board.wipe()
        board.setKnightPos(start)
        #board.printBoard()
        for i in range(63):
            moves = board.notVisitedMoves()
            if len(moves) == 0:
                # alg failed, no worries tho, try again
                #print("something")
                #board.printBoard()
                success = False
                break

            minimumMoves = 9
            topCandidate = -1
            #board.printBoard()
            #print(moves)

            shuffle(moves)
            # loop through moves, move knight to candidate square, check how many 
            # options it has there, store that number, then move back and proceed to next move.
            for candidateMove in moves:
                board.moveKnight(candidateMove)
                childMoves = len(board.notVisitedMoves())-1
                board.undoLastMove()
                if childMoves < minimumMoves:
                    minimumMoves = childMoves
                    topCandidate = candidateMove
            board.moveKnight(topCandidate)
        
        if success:
            foundWalk = True
            board.printBoard()
    input("Enter anything to return back to the menu ")

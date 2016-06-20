from cubeUtils import *
import copy
import pdb

def findBest(aCube, maxLength):
	bestSolution = []
	for move in allTurns:
		print "Trying solutions that start with", move, "solution cutoff is", maxLength
		innerCube=myCube()
		innerCube=copy.deepcopy(cube)
		solutions = solveCube(innerCube, [], move, maxLength)
		if solutions: # solutions have been found!
			for solu in solutions:
				qArrPrint("Found a solution:", solu)
				if len(solu) < maxLength:
					maxLength = len(solu)
					bestSolution = solu
				else:
					bestSolution = solu
		else:
			pass
	return bestSolution

cube = myCube()
printCube(cube)
print "The score of a cube with a completed cross is:", scoreCube(cube)
scramble = randTurns(8)
qArrPrint("Here is a short turn sequence:", scramble)
for turn in scramble:
	cube = makeTurn(cube, turn)
print "Here's the scrambled cube..."
printCube(cube)
maxSolnLen = 5 # Any cross can be solved in 8 turns or less. Usually 6.
for i in range(2, maxSolnLen+1):
	print "Testing with max solution length =", i
	result = findBest(cube, i)
	if (result):
		qArrPrint("Here's the best solution", result)
		qArrPrint("The scramble was:", scramble)
		break
			




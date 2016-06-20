import random
import copy
import pdb

class myCube:
	# Precedence:    UFRBLD
	# Normal colors: ybrgow
	# Non-cross pieces are blank
	def __init__(self):
		self.cubeUF = [' ',' ']
		self.cubeUR = [' ',' ']
		self.cubeUB = [' ',' ']
		self.cubeUL = [' ',' ']
		self.cubeFR = [' ',' ']
		self.cubeRB = [' ',' ']
		self.cubeBL = [' ',' ']
		self.cubeFL = [' ',' ']
		self.cubeFD = ['b','w']
		self.cubeRD = ['r','w']
		self.cubeBD = ['g','w']
		self.cubeLD = ['o','w']
		
allTurns = ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2",
			"B", "B'", "B2", "U", "U'", "U2", "D", "D'", "D2"]

def qArrPrint(inputString, inputArray):
	print inputString, '[%s]' % ', '.join(map(str,inputArray)) 
			
def randTurns(length):
	prevTurn = ""
	output = []
	while len(output) < length:
		next = allTurns[random.randint(0, len(allTurns)-1)]
		if next[:1]!=prevTurn[:1]:
			output.append(next)
			prevTurn=next
	return output
	
def solveCube(thisCube, moveHistory, next, maxSolnLen):
	solutionsToReturn = []
	localCube = myCube()
	localCube = copy.deepcopy(thisCube)
	localCube = makeTurn(localCube,next)
	if scoreCube(localCube) == 8:
		# Done! Return the solution
		moveHistory.append(next)
		if (len(moveHistory) < maxSolnLen):
			maxSolnLen = len(moveHistory)
		solutionsToReturn.append(moveHistory)
	elif len(moveHistory) + 1 >= maxSolnLen:
		# cross isn't solved
		# any more moves would be longer than the best solution
		# pdb.set_trace()
		#print "Solution is too long", len(moveHistory), "Stopping."
		pass
	else:
		moveHistory.append(next)
		for move in allTurns:
			tempHistory = list(moveHistory)
			# skip all R turns if we just did R' or R2
			if move[:1]!=next[:1]:
				tempCube = myCube()
				tempCube = copy.deepcopy(localCube)
				returnedSolutions = solveCube(tempCube, tempHistory, move, maxSolnLen)
				if (returnedSolutions):
					#qArrPrint("Move history:", returnedMoves)
					for solution in returnedSolutions:
						if len(solution) < maxSolnLen:
							maxSolnLen = len(solution)
							solutionsToReturn = []
							solutionsToReturn.append(solution)
						else:
							solutionsToReturn.append(solution)
				else:
					# tried all solutions in this path, no luck
					pass
	return solutionsToReturn

def doR(cube):
	tempU = cube.cubeUR[0]
	tempR = cube.cubeUR[1]
	cube.cubeUR[0]=cube.cubeFR[0]
	cube.cubeUR[1]=cube.cubeFR[1]
	cube.cubeFR[0]=cube.cubeRD[1]
	cube.cubeFR[1]=cube.cubeRD[0]
	cube.cubeRD[0]=cube.cubeRB[0]
	cube.cubeRD[1]=cube.cubeRB[1]
	cube.cubeRB[0]=tempR
	cube.cubeRB[1]=tempU
	return cube
	
def doRp(cube):
	tempU = cube.cubeUR[0]
	tempR = cube.cubeUR[1]
	cube.cubeUR[0]=cube.cubeRB[1]
	cube.cubeUR[1]=cube.cubeRB[0]
	cube.cubeRB[0]=cube.cubeRD[0]
	cube.cubeRB[1]=cube.cubeRD[1]
	cube.cubeRD[0]=cube.cubeFR[1]
	cube.cubeRD[1]=cube.cubeFR[0]
	cube.cubeFR[0]=tempU
	cube.cubeFR[1]=tempR
	return cube
	
def doF(cube):
	tempU = cube.cubeUF[0]
	tempF = cube.cubeUF[1]
	cube.cubeUF[0]=cube.cubeFL[1]
	cube.cubeUF[1]=cube.cubeFL[0]
	cube.cubeFL[0]=cube.cubeFD[0]
	cube.cubeFL[1]=cube.cubeFD[1]
	cube.cubeFD[0]=cube.cubeFR[0]
	cube.cubeFD[1]=cube.cubeFR[1]
	cube.cubeFR[0]=tempF
	cube.cubeFR[1]=tempU
	return cube
	
def doFp(cube):
	tempU = cube.cubeUF[0]
	tempF = cube.cubeUF[1]
	cube.cubeUF[0]=cube.cubeFR[1]
	cube.cubeUF[1]=cube.cubeFR[0]
	cube.cubeFR[0]=cube.cubeFD[0]
	cube.cubeFR[1]=cube.cubeFD[1]
	cube.cubeFD[0]=cube.cubeFL[0]
	cube.cubeFD[1]=cube.cubeFL[1]
	cube.cubeFL[0]=tempF
	cube.cubeFL[1]=tempU
	return cube
	
def doL(cube):
	tempU = cube.cubeUL[0]
	tempL = cube.cubeUL[1]
	cube.cubeUL[0]=cube.cubeBL[0]
	cube.cubeUL[1]=cube.cubeBL[1]
	cube.cubeBL[0]=cube.cubeLD[1]
	cube.cubeBL[1]=cube.cubeLD[0]
	cube.cubeLD[0]=cube.cubeFL[1]
	cube.cubeLD[1]=cube.cubeFL[0]
	cube.cubeFL[0]=tempU
	cube.cubeFL[1]=tempL
	return cube
	
def doLp(cube):
	tempU=cube.cubeUL[0]
	tempL=cube.cubeUL[1]
	cube.cubeUL[0]=cube.cubeFL[1]
	cube.cubeUL[1]=cube.cubeFL[0]
	cube.cubeFL[0]=cube.cubeLD[1]
	cube.cubeFL[1]=cube.cubeLD[0]
	cube.cubeLD[0]=cube.cubeBL[1]
	cube.cubeLD[1]=cube.cubeBL[0]
	cube.cubeBL[0]=tempU
	cube.cubeBL[1]=tempL
	return cube
			
def doU(cube):
	tempU = cube.cubeUF[0]
	tempF = cube.cubeUF[1]
	cube.cubeUF[0]=cube.cubeUR[0]
	cube.cubeUF[1]=cube.cubeUR[1]
	cube.cubeUR[0]=cube.cubeUB[0]
	cube.cubeUR[1]=cube.cubeUB[1]
	cube.cubeUB[0]=cube.cubeUL[0]
	cube.cubeUB[1]=cube.cubeUL[1]
	cube.cubeUL[0]=tempU
	cube.cubeUL[1]=tempF
	return cube

def doUp(cube):
	tempU = cube.cubeUF[0]
	tempF = cube.cubeUF[1]
	cube.cubeUF[0]=cube.cubeUL[0]
	cube.cubeUF[1]=cube.cubeUL[1]
	cube.cubeUL[0]=cube.cubeUB[0]
	cube.cubeUL[1]=cube.cubeUB[1]
	cube.cubeUB[0]=cube.cubeUR[0]
	cube.cubeUB[1]=cube.cubeUR[1]
	cube.cubeUR[0]=tempU
	cube.cubeUR[1]=tempF
	return cube
	
def doB(cube):
	tempU = cube.cubeUB[0]
	tempB = cube.cubeUB[1]
	cube.cubeUB[0]=cube.cubeRB[0]
	cube.cubeUB[1]=cube.cubeRB[1]
	cube.cubeRB[0]=cube.cubeBD[1]
	cube.cubeRB[1]=cube.cubeBD[0]
	cube.cubeBD[0]=cube.cubeBL[0]
	cube.cubeBD[1]=cube.cubeBL[1]
	cube.cubeBL[0]=tempB
	cube.cubeBL[1]=tempU
	return cube

def doBp(cube):
	tempU = cube.cubeUB[0]
	tempB = cube.cubeUB[1]
	cube.cubeUB[0]=cube.cubeBL[1]
	cube.cubeUB[1]=cube.cubeBL[0]
	cube.cubeBL[0]=cube.cubeBD[0]
	cube.cubeBL[1]=cube.cubeBD[1]
	cube.cubeBD[0]=cube.cubeRB[1]
	cube.cubeBD[1]=cube.cubeRB[0]
	cube.cubeRB[0]=tempU
	cube.cubeRB[1]=tempB
	return cube
	
def doD(cube):
	tempF = cube.cubeFD[0]
	tempD = cube.cubeFD[1]
	cube.cubeFD[0]=cube.cubeLD[0]
	cube.cubeFD[1]=cube.cubeLD[1]
	cube.cubeLD[0]=cube.cubeBD[0]
	cube.cubeLD[1]=cube.cubeBD[1]
	cube.cubeBD[0]=cube.cubeRD[0]
	cube.cubeBD[1]=cube.cubeRD[1]
	cube.cubeRD[0]=tempF
	cube.cubeRD[1]=tempD
	return cube
	
def doDp(cube):
	tempF = cube.cubeFD[0]
	tempD = cube.cubeFD[1]
	cube.cubeFD[0]=cube.cubeRD[0]
	cube.cubeFD[1]=cube.cubeRD[1]
	cube.cubeRD[0]=cube.cubeBD[0]
	cube.cubeRD[1]=cube.cubeBD[1]
	cube.cubeBD[0]=cube.cubeLD[0]
	cube.cubeBD[1]=cube.cubeLD[1]
	cube.cubeLD[0]=tempF
	cube.cubeLD[1]=tempD
	return cube
			
def makeTurn(cube, move):
	if move == "U":
		cube = doU(cube)
	elif move == "U'":
		cube = doUp(cube)
	elif move == "U2":
		cube = doU(cube)
		cube = doU(cube)
	elif move == "R":
		cube = doR(cube)
	elif move == "R'":
		cube = doRp(cube)
	elif move == "R2":
		cube = doR(cube)
		cube = doR(cube)
	elif move == "L":
		cube = doL(cube)
	elif move == "L'":
		cube = doLp(cube)
	elif move == "L2":
		cube = doL(cube)
		cube = doL(cube)
	elif move == "F":
		cube = doF(cube)
	elif move == "F'":
		cube = doFp(cube)
	elif move == "F2":
		cube = doF(cube)
		cube = doF(cube)
	elif move == "B":
		cube = doB(cube)
	elif move == "B'":
		cube = doBp(cube)
	elif move == "B2":
		cube = doB(cube)
		cube = doB(cube)
	elif move == "D":
		cube = doD(cube)
	elif move == "D'":
		cube = doDp(cube)
	elif move == "D2":
		cube = doD(cube)
		cube = doD(cube)
	else:
		print "ERROR! Unrecognized move."
	return cube
	
def scoreCube(cube):
	# A score of 8 is a finished cross
	score = 0
	if cube.cubeFD[0] == 'b':
		score += 1
	if cube.cubeFD[1] == 'w':
		score += 1
	if cube.cubeRD[0] == 'r':
		score += 1
	if cube.cubeRD[1] == 'w':
		score += 1
	if cube.cubeBD[0] == 'g':
		score += 1
	if cube.cubeBD[1] == 'w':
		score += 1
	if cube.cubeLD[0] == 'o':
		score += 1
	if cube.cubeLD[1] == 'w':
		score += 1
	return score

def printCube(c):
	# Still hard to visualize, but it's better than nothing
	print c.cubeUF,c.cubeUR,c.cubeUB,c.cubeUL
	print c.cubeFR,c.cubeRB,c.cubeBL,c.cubeFL
	print c.cubeFD,c.cubeRD,c.cubeBD,c.cubeLD
	

import random
gVertices = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print('Vertices in the Graph = ',gVertices)
gEdges = {(1, 2),(2, 3),(2, 7), (3, 4), (4, 5), (5, 6), (5, 1), (6, 8), (6, 9), (9, 3), (9, 7), (8, 10), (8, 2), (10, 4), (10, 7), (7, 1)}
print('\nEdges in the Graph = ',gEdges)
yellow = gVertices
startVer = random.choice(list(gVertices))
Nbr = set()
minDOM = set()

def findNeighbor(startVer, edg):
	v = startVer
	e = edg
	nbr = set()
	
	for i in e:
		if i[0]==v: 
			nbr.add(i[1])
		elif i[1]==v: 
			nbr.add(i[0])
					
	return nbr
	
def findDegrees(gVertices, gEdges):
	degs = dict()
	vert = gVertices
	gedg = gEdges
	for vertex in vert:
		deg = 0
		for edge in gedg:
			if vertex in edge:	
				deg = deg+1
			else: None
		degs[vertex] = deg
	return degs
	
def findMaxDegVer(degrees):
	degreesValues = degrees
	sl = set()
	maxvertex = set()
	for i in degreesValues:
		if degreesValues.get(i) == max(degreesValues.values()):
			sl.add(i)
			maxvertex =i
		if len(sl)>1:
			maxvertex = random.choice(list(sl))
	return maxvertex

while(gVertices):
	deg = dict()
	minDOM.add(startVer)
	yellow.discard(startVer)
	gVertices.discard(startVer)
	Nbr = findNeighbor(startVer, gEdges)

	if len(Nbr)==0:
		break 

	gVertices = gVertices - Nbr

	if len(gVertices)==0:
		break

	rem = set()
	for v in Nbr:
		for s in gEdges:
			if v in s:
				rem.add(s)
	gEdges = gEdges - rem
	if len(gVertices)==1 or len(gVertices)==2:
		last = random.sample(gVertices, 1)
		minDOM.add(last[0])
		break
	elif len(gEdges)==0:
		break
	deg = findDegrees(gVertices, gEdges)
	startVer = findMaxDegVer(deg)

print('\nYellow Vertices = ',yellow)
print('\nMinimum Dominating Set (Red coloured) = ', minDOM)
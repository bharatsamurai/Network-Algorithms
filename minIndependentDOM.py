import random
gVertices = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
print('Vertices in the Graph = ',gVertices)
gEdges = [(1, 2),(2, 3), (3, 4), (4, 5), (2, 5), (2, 6), (6, 7), (7, 8), (2, 9), (2,10), (2, 11), (2, 12), (7, 13)]
print('\nEdges in the Graph = ',gEdges)
S = list()
degrees = dict()
connectedMinSet = []

while len(gVertices)!=0:
	
	def findDegrees():
	
		for vertex in gVertices:
			deg = 0
			for edge in gEdges:
				if vertex in edge:	
					deg = deg+1
				else: None
			degrees[vertex] = deg
		return degrees
	findDegrees()
	maxDegree = max(degrees.values())
	for i in degrees:
		if degrees.get(i) == maxDegree:
			S.append(i)
			maxvertex= i
			
	nbrmaxvertex = set()
	nbrmaxvertex.add(maxvertex)
	gVerticesNew = set()
	for edg in enumerate(gEdges):
		
		if edg[1][0]==maxvertex:
			nbrmaxvertex.add(edg[1][1])
		elif edg[1][1]==maxvertex:
			nbrmaxvertex.add(edg[1][0])

	connectedMinSet.append(nbrmaxvertex)
	gVerticesNew = gVertices - nbrmaxvertex
	gVertices=gVerticesNew

	for v in gEdges:
		for e in gEdges:
			if maxvertex in e:
				gEdges.remove(e)
	
	degrees = dict()
	

print('\nMinimum independent dominating set in the graph = ',set(S))
q = 0
connq = set()
while q < len(S):
	w = q+1
	
	while w < len(S)-q:
		rs = set(connectedMinSet[q]).intersection(set(connectedMinSet[w]))
		
		if len(rs) ==1:
			connq |= rs
		if len(rs) >1:
			connq |= set(random.sample(rs,1))
			
		w +=1
	q +=1

connq |= set(S)
print('\nMinimum connected dominating set in the graph is =',connq)
print('\nDomination number of the graph =', len(connq)) 

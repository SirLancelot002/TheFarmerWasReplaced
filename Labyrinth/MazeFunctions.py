import FarmFunctions

DELTAS = {North: (0, 1), East: (1, 0), South: (0, -1), West: (-1, 0)}#Constant
DIR_ORDER = [North, East, South, West]
OPPOSITE = {North: South, South: North, East: West, West: East}
size = get_world_size()

def getOpposite(direc):
	return OPPOSITE[direc]

def coordInMaze(pos):
	(x, y) = pos
	return ((x >= 0 and x < size) and (y >= 0 and y < size))

#Function to get the coordinates of your neighbor
def getNeighbor(pos, direc):
	(x, y) = pos
	(nx, ny) = DELTAS[direc]
	return (x + nx, y + ny)


def get_direction_from_to(a, b):#THIS ONLY works when a and b are Neighbors
	#Return a direction enum that moves from coord a -> b (adjacent), or None.
	(ax, ay) = a
	(bx, by) = b
	dx = bx - ax
	dy = by - ay
	for d in DIR_ORDER:
		nx, ny = DELTAS[d]
		if nx == dx and ny == dy:
			return d
	return None

def manhattan(a, b):
	(ax, ay) = a
	(bx, by) = b
	return abs(ax - bx) + abs(ay - by)

#stick = get_tick_count()
#get_direction_from_to((0,1), (1,1))
#etick = get_tick_count()
#print(etick - stick)

#Returns which direction can the drone move in
def mOptions():
	return {North: can_move(North), East: can_move(East), South: can_move(South), West: can_move(West)}

def myGet(dic, key):
	if key not in dic:
		return None
	else:
		return dic[key]

def moveByListReverseRecord(mList, maze, inSet):#A MoveByList to use to refresh the map
	for i in range(len(mList)):
		move(mList.pop())
		record_current_tile(maze, inSet)

def init_tile(maze, coord):
	#Create tile entry with all directions None if it doesn't exist.
	if coord not in maze:
		maze[coord] = {North: None, East: None, South: None, West: None}

def init_tileV2(maze, coord):
	#Create tile entry with all directions None if it doesn't exist.
	if coord not in maze:
		maze[coord] = ({North: None, East: None, South: None, West: None}, False)

def getClosestUnecplored(map, inSet, target):
	size = get_world_size()
	if len(map) >= size*size:
		return (0,0)
	(tx, ty) = target
	recDist = 10000
	recPair = (0,0)
	for coord in map:
		(cx, cy) = coord
		if manhattan(coord, target) < recDist and not(coord in inSet):
			recPair = coord
			recDist = manhattan(coord, target)
	return recPair

def record_current_tile(maze, inSet):
	pos = (get_pos_x(), get_pos_y())	#Get our current positon in a tuple
	init_tile(maze, pos)				#Make sure our position exisits in the maze dictionary
	options = mOptions()				#get our move options (in a dictionary)
	maze[pos] = options					#Set our move options on this tile
	if pos not in inSet:
		inSet.add(pos)	
	for i in options:					#Go through our Neighbors and set their move options as well
		if options[i]:					#Can Move?
			nTilePos = getNeighbor(pos, i)		#Where is the Neighbor we are looking at
			if coordInMaze(nTilePos):			#Is it inside the maze?
				init_tile(maze, nTilePos)		#Make sure ut exists in the maze dictionary
				maze[nTilePos][getOpposite(i)] = True		#Set te move value

#Pathfinding Function==============================================
def route_to_target_dirs(target, mazeMap):
	start = (get_pos_x(), get_pos_y())
	if (start == target) or ((target not in mazeMap) or (start not in mazeMap)):#This makes sure that you are not trying to call the function when you shouldn't
		return []

	closedList = {start: {"Parent": None, "Direction": None}}#Dictionary. Tile coordinates are key, value is parent, and direction (from parent to child)
	openList = {}
	current = start
	while current != target:	#If the mazeMap was set up correctly, we must have a path to the target. We go until we reach the target
		#First we explore the new avilable tiles, and add them to the openList
		mOptions = mazeMap[current]
		for mov in mOptions:
			if mOptions[mov] == True:	#We'll only add them if we can move from here to there
				newCoords = getNeighbor(current, mov)
				if (newCoords not in closedList) and (newCoords not in openList):	#Ignore them, if they are already in the closed or openList.
					newScore = manhattan(newCoords, target)
					openList[newCoords] = {"Parent": current, "Direction": mov, "Score": newScore}
					
		#Here we start a minimum value search
		recScore = 1000000		#Since python doesn't have an int.Max, I just gave it a big number. (Note that this'd not be enought on a 100x100 map)
		recCoords = None
		for item in openList:
			lookScore = openList[item]["Score"]
			if lookScore < recScore:
				recScore = lookScore
				recCoords = item
		closedList[recCoords] = openList[recCoords]#After we found the closest tile to the target, we add it to the closedList, delete it from the openList
		openList.pop(recCoords)
		current = recCoords
	
	path = []
	while current != start:
		path.append(closedList[current]["Direction"])
		current = closedList[current]["Parent"]
	return path

#Explore Function. Call it, and it will explore and run until it find the treasure=====================
def exploreStep(map, inSet, target):
	pos = (get_pos_x(), get_pos_y())
	record_current_tile(map, inSet)
	options = mOptions()
	rec = None
	recScore = 1000
	for mov in options:
		coord = getNeighbor(pos, mov)
		if (options[mov] and (coord not in inSet)) and (manhattan(coord, target) < recScore):
			rec = (mov, coord)
			recScore = manhattan(coord, target)
	if rec == None:
		closest = getClosestUnecplored(map, inSet, target)
		route = route_to_target_dirs(closest, map)
		FarmFunctions.moveByListReverse(route)
		exploreStep(map, inSet, target)
		return
	move(rec[0])
	if rec[1] == target:
		record_current_tile(map, inSet)
		return
	exploreStep(map, inSet, target)
size = get_world_size()

#Mindent megművelő fügvény=======================================
def fullFarmTill(TargetGround):
	for i in range(size):
		for j in range(size):
			if (not get_ground_type() == TargetGround):
				till()
			move(North)
		move(East)


def fullFarmTillV2(groundType):
	for i in range(size):
		for j in range(size):
			harvest()
			if (get_ground_type() != groundType):
				till()
			move(North)
		move(East)

def plantAtTargets(list, tarplant):
	for coord in list:
		moveTo(coord[0], coord[1])
		plant(tarplant)

#Mindent bearató fügvény============================================
def oneRoundHarvest(ignHarvRest):
	fail = False
	for i in range(size):
		for j in range(size):
			if can_harvest() or ignHarvRest:
				harvest()
			else:
				success = True
			move(North)
		move(East)
	if fail:
		oneRoundHarvest(ignHarvRest)

#Itt jön két segédfügvény, mert a game csóró==========================	
def xor(a, b):
	if a and b:
		return False
	elif (not a) and (not b):
		return False
	else:
		return a or b

#Itt jön a nagyon fontos MoveTO fügvény=================================
def moveTo(x = 0, y = 0):
	if (x > size or y > size or x < 0 or y < 0):
		return None
	xSteps = x - get_pos_x()
	if abs(xSteps) > size/2:
		if xSteps > 0:
			xSteps -= size
		else:
			xSteps += size
	while(xSteps > 0):
		move(East)
		xSteps-=1
	while(xSteps < 0):
		move(West)
		xSteps+=1
	
	ySteps = y - get_pos_y()
	if abs(ySteps) > size/2:
		if ySteps > 0:
			ySteps -= size
		else:
			ySteps += size
	while(ySteps > 0):
		move(North)
		ySteps-=1
	while(ySteps < 0):
		move(South)
		ySteps+=1

def moveToDumb(x = 0, y = 0):
	if (x > size or y > size or x < 0 or y < 0):
		return None
	xSteps = x - get_pos_x()
	while(xSteps > 0):
		move(East)
		xSteps-=1
	while(xSteps < 0):
		move(West)
		xSteps+=1
	
	ySteps = y - get_pos_y()
	while(ySteps > 0):
		move(North)
		ySteps-=1
	while(ySteps < 0):
		move(South)
		ySteps+=1

def moveByList(mList):
	for m in mList:
		move(m)

def moveByListReverse(mList):
	for i in range(len(mList)):
		move(mList.pop())

#Mindent beültet valamivel ==========================================
def fullFarmPlant(targetPlant):
	for i in range(size):
		for j in range(size):
			plant(targetPlant)
			move(North)
		move(East)


#Mindent beültet Sunflower-rel================
def fullFarmPlantSF():
	measure_dict = {}
	for i in range(size):
		x = get_pos_x()
		for j in range(size):
			y = get_pos_y()
			plant(Entities.Sunflower)
			val = measure()
			if val in measure_dict:
				measure_dict[val].append((x, y))
			else:
				measure_dict[val] = [(x, y)]
			move(North)
		move(East)
	return measure_dict

#Megkeressük az üres cellákat =======================================
def getEmptyCellsOnFullMap():
	list = []
	for i in range(size):
		for j in range(size):
			if not can_harvest():
				list.append((get_pos_x(), get_pos_y()))
			move(North)
		move(East)
	return list


def getEmptyCellsOnFullMapV2():
	list = []
	for i in range(size/3):
		moveTo(min((i*3)+1, size-1), 0)
		for j in range(size):
			dir = [West, None, East]
			for k in range(-1,2):
				if measure(dir[k+1]) == None and get_pos_x() + k < size:
					list.append((get_pos_x()+k, get_pos_y()))
			move(North)
	return list


def getEmptyCells(lookList):
	list = []
	for coord in lookList:
		moveTo(coord[0], coord[1])
		if not can_harvest():
				list.append((get_pos_x(), get_pos_y()))
	return list

#Coordináta list rendező fügvény=================================
def order_cells_toroidal(cell_list):
	if not cell_list:
		return []

	ordered = [cell_list[0]]
	remaining = cell_list[1:]
	used = set()
	used.add(cell_list[0])

	def toroidal_distance(a, b):
		dx = abs(a[0] - b[0])
		dy = abs(a[1] - b[1])
		dx = min(dx, size - dx)
		dy = min(dy, size - dy)
		return dx * dx + dy * dy

	while len(ordered) < len(cell_list):
		last = ordered[-1]
		closest = None
		closest_dist = None
		for c in remaining:
			if c in used:
				continue
			d = toroidal_distance(last, c)
			if closest == None or d < closest_dist:
				closest = c
				closest_dist = d
		ordered.append(closest)
		used.add(closest)

	return ordered

def getMeasureOnFullMap():
	measure_dict = {}
	for i in range(size/3):
		moveTo(min((i*3)+1, size-1), 0)
		for j in range(size):
			dir = [West, None, East]
			x = get_pos_x()
			y = get_pos_y()
			for k in range(-1,2):
				if x + k < size:
					val = measure(dir[k+1])
					if val in measure_dict:
						measure_dict[val].append((x + k, y))
					else:
						measure_dict[val] = [(x + k, y)]
			move(North)
	return measure_dict

def mustHarvest(x = None, y = None):
	if x != None and y != None:
		moveTo(x,y)
	if get_entity_type() == None:
		return
	while True:
		if can_harvest():
			harvest()
			return
		if get_water() < 0.9:
			use_item(Items.Water)

def wait(time = 1):
	enter = get_time()
	while get_time() < enter + time:
		continue
	return

def waitTick(time = 1):
	enter = get_tick_count()
	while get_tick_count() < enter + time:
		continue
	return
	
def mayHarvest(x, y, dic):#ONLY USE if it wasn't the single highest value
	moveTo(x,y)
	if can_harvest():
		harvest()
		return dic
	else:
		val = measure()
		if val in dic:
			dic[val].insert(0, (x, y))
		else:
			dic[val] = [(x, y)]
		bigFlow = max(dic)
		(tarx, tary) = dic[bigFlow].pop()
		if len(dic[bigFlow]) == 0:
			dic.pop(bigFlow)
			mustHarvest(tarx, tary)
			return dic
		else:
			return mayHarvest(tarx, tary, dic)

def plantGrass():
	if not get_entity_type() == Entities.Grass:
		harvest()
	if get_ground_type() == Grounds.Soil:
		till()

def plantBush():
	if not get_entity_type() == Entities.Bush:
		harvest()
	if get_ground_type() == Grounds.Soil:
		till()
	plant(Entities.Bush)

def plantTree():
	if not get_entity_type() == Entities.Tree:
		harvest()
	if get_ground_type() == Grounds.Soil:
		till()
	plant(Entities.Tree)
	#use_item(Items.Fertilizer)

def plantCarrot():
	if not get_entity_type() == Entities.Carrot:
		harvest()
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Carrot)

def makeCompanion():
	companion = get_companion()
	if companion == None:
		return
	plant_type = companion[0]
	(x, y) = companion[1]
	myX = get_pos_x()
	myY = get_pos_y()
	moveTo(x,y)
	if get_entity_type() != plant_type:
		if plant_type == Entities.Grass:
			plantGrass()
		elif plant_type == Entities.Bush:
			plantBush()
		elif plant_type == Entities.Tree:
			plantTree()
		else:
			plantCarrot()
	moveTo(myX,myY)

def plantRandomPoly(gc = 1, bc = 1, tc = 1, cc = 1):
	r = random() * (gc + bc + tc + cc)
	if r < gc:
		plantGrass()
	elif r < (gc + bc):
		plantBush()
	elif r < (gc + bc + tc):
		plantTree()
	else:
		plantCarrot()

def maxKeyInDic(dict):
	max = -10000000000
	for i in dict:
		if i > max:
			max = i
	return max

def divideList(myList, divBy):
	length = len(myList)
	if length == 0:
		return []

	# How many items per sublist (at least)
	base = length // divBy
	# How many sublists get one extra element
	extra = length % divBy

	result = []
	index = 0

	for i in range(min(divBy, length)):
		toPlus = 0
		if i < extra:
			toPlus = 1
		plus = base + toPlus
		result.append(myList[index:index + plus])
		index += plus

	return result
	
def harvestList(coordList):
	while len(coordList) > 1:
		if smallMayHarvest(coordList[-1][0], coordList[-1][1]):
			coordList.pop()
		else:
			keeper = coordList[-1]
			coordList.pop()
			coordList.insert(0, keeper)
	mustHarvest(coordList[-1][0], coordList[-1][1])
		
def smallMayHarvest(x, y):
	moveTo(x,y)
	result = can_harvest()
	if result:
		harvest()
	return result
	
def doRows(plantT, repeat, offset):
	for j in range(repeat):
		for i in range(size):
			plant(plantT)
			move(North)
		for m in range(offset):
			move(East)

def waterRows(level, repeat, offset):
	for j in range(repeat):
		for i in range(size):
			if get_water() < level:
				use_item(Items.Water)
			move(North)
		for m in range(offset):
			move(East)
import FarmFunctions

size = get_world_size()
AreaY = 8
AreaX = 8

def initArea(limitX, limity):
	for i in range(limitX):
		for j in range(limity):
			FarmFunctions.plantRandomPoly()
			move(North)
		move(East)

def polyOnArea(limitX, limity):
	for i in range(limitX):
		for j in range(limity):
			FarmFunctions.makeCompanion()
			harvest()
			FarmFunctions.plantRandomPoly()
			move(North)
		move(East)

def PolyOnArea(x,y):
	FarmFunctions.moveTo(x,y)
	initArea(AreaX, AreaY)
	while True:
		FarmFunctions.moveTo(x,y)
		polyOnArea(AreaX, AreaY)

def KeepAreaWatered(x,y):
	while True:
		FarmFunctions.moveTo(x,y)
		for i in range(AreaX):
			for j in range(AreaY):
				if get_water() < 0.5:
					use_item(Items.Water)
				move(North)
			move(East)

change_hat(Hats.Traffic_Cone)
FarmFunctions.moveTo()
for x in range(0,size,AreaX):
	for y in range(0,size,AreaY):
		def initDrone():
			PolyOnArea(x,y)
		def initWater():
			KeepAreaWatered(x,y)
		if not spawn_drone(initDrone):
			initDrone()
		if not spawn_drone(initWater):
			initWater()
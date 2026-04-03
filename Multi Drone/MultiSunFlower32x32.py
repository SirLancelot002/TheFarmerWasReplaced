import FarmFunctions
import MultiDroneFunctions

size = get_world_size()

FarmFunctions.moveTo()
for i in range(size):
	def toDo():
		MultiDroneFunctions.till_columnV2(Grounds.Soil, Entities.Sunflower)
	if not spawn_drone(toDo):
		toDo()
	move(East)

while True:
	farmMap = FarmFunctions.getMeasureOnFullMap()
	while len(farmMap) != 0:
		max = FarmFunctions.maxKeyInDic(farmMap)
		divfarmMap = FarmFunctions.divideList(farmMap[max], 31)
		for coords in divfarmMap:
			def do():
				FarmFunctions.harvestList(coords)
			spawn_drone(do)
		farmMap.pop(max)
		while num_drones() > 1:
			pass
	for i in range(16):
		def myPlant():
			FarmFunctions.moveTo(i, 0)
			FarmFunctions.doRows(Entities.Sunflower, 2, 16)
		spawn_drone(myPlant)
	FarmFunctions.waitTick(3000)
			
import FarmFunctions

change_hat(Hats.Sunflower_Hat)
FarmFunctions.moveTo(0,0)
FarmFunctions.fullFarmTillV2(Grounds.Soil)
size = get_world_size()
#print(farmMap)

while num_items(Items.Carrot) >= size*size:
	FarmFunctions.moveTo(0,0)
	farmMap = FarmFunctions.fullFarmPlantSF()
	while len(farmMap) != 0:
		bigFlow = max(farmMap)
		(tarx, tary) = farmMap[bigFlow].pop()
		if len(farmMap[bigFlow]) == 0:
			farmMap.pop(bigFlow)
			FarmFunctions.mustHarvest(tarx, tary)
		else:
			FarmFunctions.mayHarvest(tarx, tary, farmMap)

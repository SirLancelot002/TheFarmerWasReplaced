import FarmFunctions

change_hat(Hats.Sunflower_Hat)
FarmFunctions.moveTo(0,0)
FarmFunctions.fullFarmTillV2(Grounds.Soil)
size = get_world_size()
FarmFunctions.moveTo(0,0)
farmMap = FarmFunctions.fullFarmPlantSF()
#print(farmMap)

while num_items(Items.Carrot) > 1:
	bigFlow = max(farmMap)
	(tarx, tary) = farmMap[bigFlow].pop()
	if len(farmMap[bigFlow]) == 0:
		farmMap.pop(bigFlow)
		FarmFunctions.mustHarvest(tarx, tary)
	else:
		FarmFunctions.mayHarvest(tarx, tary, farmMap)
	plant(Entities.Sunflower)
	val = measure()
	if val in farmMap:
		farmMap[val].append((tarx, tary))
	else:
		farmMap[val] = [(tarx, tary)]
import FarmFunctions
FarmFunctions.moveTo(0,0)
FarmFunctions.fullFarmTillV2(Grounds.Soil)

while (num_items(Items.Wood) > 0 and num_items(Items.Hay) > 0):
	for i in range(get_world_size()):
		move(North)
		if (can_harvest()):
			harvest()
		if num_items(Items.Wood) > 0 and num_items(Items.Hay) > 0:
			plant(Entities.Carrot)
		if random() > 0.9:
			use_item(Items.Fertilizer)
	move(East)
FarmFunctions.oneRoundHarvest(False)
print("Out of stuff")
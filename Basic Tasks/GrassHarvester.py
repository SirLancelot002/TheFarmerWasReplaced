import FarmFunctions

change_hat(Hats.Straw_Hat)
FarmFunctions.fullFarmTillV2(Grounds.Grassland)

while (True):
	for i in range(get_world_size()):
		move(North)
		if (can_harvest()):
			harvest()
	move(East)
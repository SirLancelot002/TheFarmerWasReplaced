import FarmFunctions

FarmFunctions.fullFarmTill(Grounds.Grassland)

change_hat(Hats.Tree_Hat)

while (True):
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		if (get_pos_x() + get_pos_y())%2 == 0 and get_entity_type() != Entities.Tree:
			plant(Entities.Tree)
		move(North)
	move(East)
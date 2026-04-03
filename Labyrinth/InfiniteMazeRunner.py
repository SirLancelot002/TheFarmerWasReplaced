import FarmFunctions
import MazeFunctions

#ttf = 5			#Target Time Frame, if getting to target took more time, explore on way
size = MazeFunctions.size
substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
change_hat(Hats.The_Farmers_Remains)

while num_items(Items.Weird_Substance) >= substance:
	FarmFunctions.moveTo(size/2, size/2)
	harvest()
	if get_ground_type() != Grounds.Grassland:
		till()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, substance)
	i = -1
	map = {}
	mapSet = set()
	#recordWhileTravel = False
	while num_items(Items.Weird_Substance) >= substance and i < 300:
		i += 1
		MazeFunctions.record_current_tile(map, mapSet)
		targetCoords = measure()
		PLAM = 2 + ((300 - i)/ 100)#Path Length Acceptance Modifier. How much diviance from straight path we accept
		if targetCoords in map:
			route = MazeFunctions.route_to_target_dirs(targetCoords, map)
			airDist = MazeFunctions.manhattan(targetCoords, (get_pos_x(), get_pos_y()))
			if len(route) > airDist * PLAM:
				MazeFunctions.moveByListReverseRecord(route, map, mapSet)
			else:
				FarmFunctions.moveByListReverse(route)
		else:
			closest = MazeFunctions.getClosestUnecplored(map, mapSet, targetCoords)
			route = MazeFunctions.route_to_target_dirs(closest, map)
			airDist = MazeFunctions.manhattan(closest, (get_pos_x(), get_pos_y()))
			if len(route) > airDist * PLAM:
				MazeFunctions.moveByListReverseRecord(route, map, mapSet)
			else:
				FarmFunctions.moveByListReverse(route)
			MazeFunctions.exploreStep(map, mapSet, targetCoords)
		if i != 300:
			use_item(Items.Weird_Substance, substance)
		else:
			harvest()
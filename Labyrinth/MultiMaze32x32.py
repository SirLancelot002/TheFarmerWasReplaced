import FarmFunctions
import MazeFunctions

center = get_world_size()/2
substance = 8 * 2**(num_unlocked(Unlocks.Mazes) - 1)

def MazeRunning(x, y):
	FarmFunctions.moveToDumb(x, y)
	if get_entity_type() != Entities.Grass:
		harvest()
	if get_ground_type() != Grounds.Grassland:
		till()
	while num_drones() < 16:
		pass
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
		PLAM = 1 + ((300 - i)/ 100)#Path Length Acceptance Modifier. How much diviance from straight path we accept
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

coords_priority = [
	# Corners
	(28, 28), (4, 28), (4, 4), (28, 4),
	# Edge midpoints
	(20, 28), (12, 28), (4, 20), (4, 12),
	(12, 4), (20, 4), (28, 12), (28, 20),
	# Middle 2×2
	(20, 20), (12, 20), (12, 12), (20, 12)
]

FarmFunctions.moveTo(center, center)
for i in coords_priority:
	(x, y) = i
	def initDrone():
		MazeRunning(x, y)
	spawn_drone(initDrone)
			
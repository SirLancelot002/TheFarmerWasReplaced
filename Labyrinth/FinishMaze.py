import FarmFunctions
import MazeFunctions

map = {}
mapSet = set()
MazeFunctions.record_current_tile(map, mapSet)
targetCoords = measure()
if targetCoords in map:
	route = MazeFunctions.route_to_target_dirs(targetCoords, map)
	FarmFunctions.moveByListReverse(route)
else:
	closest = MazeFunctions.getClosestUnecplored(map, mapSet, targetCoords)
	route = MazeFunctions.route_to_target_dirs(closest, map)
	FarmFunctions.moveByListReverse(route)
	MazeFunctions.exploreStep(map, mapSet, targetCoords)
harvest()
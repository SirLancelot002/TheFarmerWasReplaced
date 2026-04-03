# Maze functions.

Here the most important file is the `MazeFunctions.py`. This contains all helper functions I've used in the other files. Even the graph solver algorithm is in there. 
## The help we get in-game:
> `Items.Weird_Substance`, which is obtained by fertilizing plants, has a strange effect on bushes. If the drone is over a bush and you call `use_item(Items.Weird_Substance, amount)` the bush will grow into a maze of hedges.
The size of the maze depends on the amount of `Items.Weird_Substance` used (the second argument of the `use_item()` call).
Without maze upgrades, using n `Items.Weird_Substance` will result in a nxn maze. Each maze upgrade level doubles the treasure, but it also doubles the amount of `Items.Weird_Substance` needed. 
So to make a full field maze:
`plant(Entities.Bush)`
`substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)`
`use_item(Items.Weird_Substance, substance)`
For some reason the drone can't fly over the hedges, even though they don't look that high.
There is a treasure hidden somewhere in the hedge. Use `harvest()` on the treasure to receive gold equal to the area of the maze. (For example, a 5x5 maze will yield 25 gold.)
If you use `harvest()` anywhere else the maze will simply disappear.
`get_entity_type()` is equal to Entities.Treasure if the drone is over the treasure and Entities.Hedge everywhere else in the maze.
Mazes do not contain any loops unless you reuse the maze (see below how to reuse a maze). So there is no way for the drone to end up in the same position again without going back.
You can check if there is a wall by trying to move through it. 
`move()` returns True if it succeeded and False otherwise.
`can_move()` can be used to check if there is a wall without moving.
If you have no idea how to get to the treasure, take a look at Hint 1. It shows you how to approach a problem like this.
Using `measure()` anywhere in the maze returns the position of the treasure.
`x, y = measure()`
For an extra challenge you can also reuse the maze by using the same amount of Items.Weird_Substance on the treasure again. 
This will collect the treasure and spawn a new treasure at a random position in the maze.
Each time the treasure is moved, some of the maze's walls may be randomly removed. So reused mazes can contain loops.
Note that loops in the maze make it much more difficult because it means that you can get to the same location again without moving back.
Reusing a maze doesn't give you more gold than just harvesting and spawning a new maze.
This is 100% an extra challenge that you can just skip.
It's only worth it if the extra information and the shortcuts help you solve the maze faster.
The treasure can be relocated up to 300 times. After that, using weird substance on the treasure won't increase the gold in it anymore and it won't move anymore.

## What I'd like to add.
In short, the most efficient way to complete the maze is to map it once, then reuse it 300 times. This is because the game can only take away walls; it can't put in new ones. And it's reasonable to assume that going from **A** to **B** in a maze we know is more efficient than solving a new one.So this was what I did.

## How my code works.
The drone starts from the middle of the maze, since this gives it the best chance to be closer to the treasure. Then it's trying to go in the rough direction of the chest, mapping the tiles it goes over.
It notes that the mapped tile has connections to which tiles. This goes on until it reaches a deadend. At which point, it calculates the closest tile to the chest it knows the way to. Goes there, then continues exploring.
This can only end up with the drone on the chest. It reuses the maze, then repeats 300 times.

## `InfiniteMazeRunner.py`
It does exactly as I wrote above, until it runs out of resources. On the largest map it takes about 30 minutes to finish but is very satisfying to watch.
<img width="1114" height="820" alt="image" src="https://github.com/user-attachments/assets/4346b24f-3d04-442e-a1e8-8d9a3bb1ea6f" />

I've also entered this code into the global leaderboard and got rank #40. 🥳 *(First I had a bug in the code, so it was way slower and only reached rank 450, so there are at least that many people who tried).*
![Maze_Single_Leaderboard](https://github.com/user-attachments/assets/56400b45-f816-4cc2-8281-a601691cd019)

## `FinishMaze.py`
It was for debugging; if I just want to finish the maze, not to wait until the very end, it does it in a max of 30 seconds.

## `MultiMaze32x32`
I made it to work with multiple drones. The mazes can only be squares, so I had to make some choices. I want 16 drones instead of 32 because I could not get them in a nice order, and if I have just one large maze, that's going to slow the whole thing down, so there is no point in making just some mazes smaller. Otherwise, they function identically to the large maze solver.
<img width="1303" height="1039" alt="image" src="https://github.com/user-attachments/assets/8abe52a9-a54d-4b7d-931e-8db85b50c63b" />

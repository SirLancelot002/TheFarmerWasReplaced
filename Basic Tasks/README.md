# Basic task descriptions.

By far the most important file in this folder is the ```FarmFunctions.py```. This holds all the helper functions I made. Also, some functions are there in multiple generations, so you can see the improvements I made as I got new and improved ideas on how to make the code run better. The best example is the ```moveTo(x, y)```. After the first edition, I made use of the fact that if you go off the map's east side, you just come around the west side.

## Description for each problem (in increasing difficulty order).

<details>
<summary>Wheat (or grass) harvesting</summary>

This is by far the most simple task. By default, this just grows out of the ground; you only need to `harvest()` it. The only wrong way for this is if you harvest it before it fully grows. But this grows so fast that if your drone is just going around the map, the grass will grow back before you get back to it again, so no checks are needed for this. Only if the ground is already tilled from a previous script do you need to un-till it. 

<img width="1327" height="1039" alt="image" src="https://github.com/user-attachments/assets/4648230a-d7b1-4bc8-8aba-3683b57079bf" />

</details>

<details>
<summary>Bush planting</summary>

The only difficulty increase compared to the grass is that bushes need to be planted first (and when harvested they give wood). This can be done with the `plant(Entites.Bush)` function. These are honestly almost the same.
<img width="1359" height="825" alt="image" src="https://github.com/user-attachments/assets/f04a0f0e-be4b-4e0a-bedc-12e66dd12988" />

</details>

<details>
<summary>Carrots</summary>

Carrots are only one step above bushes. They can only be planted on tilled soil, which means you have to use the `till()` function. But the ground remains tilled after harvest, which means you either have to check the ground before planting (which is inefficient), or you can till the whole map and plant it after that (only repeating the planting commands).
<img width="1601" height="799" alt="image" src="https://github.com/user-attachments/assets/a6da5e5b-b110-4f98-a476-0f57e456aa1e" />

</details>

<details>
<summary>Tree planting</summary>

Trees are the first plants the player has to think about for a second. To quote from the game:
> **Trees** are a better way to get wood than bushes. They give 5 wood each. Like bushes, they can be planted on grass or soil.
Trees like to have some space and planting them right next to each other will slow down their growth. The growing time is doubled for each tree that is on a tile directly to the north, east, west or south of it. So if you plant trees on every tile, they will take 2x2x2x2 = 16 times longer to grow.

This means that you want to plant them in a checkerboard formation to maximize growth time. (You will need it this time).
<img width="891" height="812" alt="image" src="https://github.com/user-attachments/assets/8eb1ed76-c785-47a9-9dbe-bb3bded15eb4" />

</details>

<details>
<summary>Pumpkin planting</summary>

> **Pumpkins** grow like carrots on tilled soil. Planting them costs carrots.
When all the pumpkins in a square are fully grown, they will grow together to form a giant pumpkin. Unfortunately, pumpkins have a 20% chance of dying once they are fully grown, so you will need to replant the dead ones if you want them to merge. 
When a pumpkin dies, it leaves behind a dead pumpkin that won't drop anything when harvested. Planting a new plant in its place automatically removes the dead pumpkin, so there is no need to harvest it. `can_harvest()` always returns False on dead pumpkins.
The yield of a giant pumpkin depends on the size of the pumpkin.
A 1x1 pumpkin yields 1*1*1 = 1 pumpkins.
A 2x2 pumpkin yields 2*2*2 = 8 pumpkins instead of 4.
A 3x3 pumpkin yields 3*3*3 = 27 pumpkins instead of 9.
A 4x4 pumpkin yields 4*4*4 = 64 pumpkins instead of 16.
A 5x5 pumpkin yields 5*5*5 = 125 pumpkins instead of 25.
A nxn pumpkin yields n*n*6 pumpkins for n >= 6.
It's a good idea to get at least 6x6 size pumpkins to get the full multiplier. 
This means that even if you plant a pumpkin on every tile in a square, one of the pumpkins may die and prevent the mega pumpkin from growing.

What you can see above is the official text, but there is something it does not tell you. The `can_harvest()` function can only be called where the drone is, and as we know, moving the drone makes it inefficient. But I found that the `measure()` function also works on rotten pumpkins, but that can be cast sideways, meaning the drone only has to travel ~1/3 of the original distance since it can look at the two rows next to the one it's scanning.

Otherwise, I just store the whole field in the drone's memory, and after it knows the whole field, it replants the rotten pumpkins, then rescanns them. It repeats this until the whole field is one giant pumpkin.
<img width="1574" height="750" alt="image" src="https://github.com/user-attachments/assets/b0c6e5d0-6a83-4920-9019-9162fd3d8224" />

</details>

<details>
<summary>Polyculture</summary>

Hidden content here

</details>

<details>
<summary>Sunflower planting</summary>

Hidden content here

</details>

<details>
<summary>Cactus planting</summary>

Hidden content here

</details>

<details>
<summary>Dino Ranching</summary>

Hidden content here

</details>

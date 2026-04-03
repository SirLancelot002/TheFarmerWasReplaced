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
<summary>Tree planting</summary>

Trees are the first plants the player hes to think about for a second. To quote from the game:
> **Trees** are a better way to get wood than bushes. They give 5 wood each. Like bushes, they can be planted on grass or soil.

> Trees like to have some space and planting them right next to each other will slow down their growth. The growing time is doubled for each tree that is on a tile directly to the north, east, west or south of it. So if you plant trees on every tile, they will take 2*2*2*2 = 16 times longer to grow.
This means that you want to plant them in a checker board formation to maximalize growth time. (You will need it this time).

</details>

# Basic task descriptions.

By far the most important file in this folder is the ```FarmFunctions.py```. This holds all the helper functions I made. Also, some functions are there in multiple generations, so you can see the improvements I made as I got new and improved ideas on how to make the code run better. The best example is the ```moveTo(x, y)```. After the first edition, I made use of the fact that if you go off the map's east side, you just come around the west side.

## Description for each problem (in increasing difficulty order).

<details>
<summary>Wheat (or grass) harvesting</summary>

This is by far the most simple task. By default, this just grows out of the ground; you only need to `harvest()` it. The only wrong way for this is if you harvest it before it fully grows. But this grows so fast that if your drone is just going around the map, the grass will grow back before you get back to it again, so no checks are needed for this. Only if the ground is already tilled from a previous script do you need to un-till it. 

<img width="1327" height="1039" alt="image" src="https://github.com/user-attachments/assets/4648230a-d7b1-4bc8-8aba-3683b57079bf" />

</details>

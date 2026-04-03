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
A 1x1 pumpkin yields 1x1x1 = 1 pumpkins.
A 2x2 pumpkin yields 2x2x2 = 8 pumpkins instead of 4.
A 3x3 pumpkin yields 3x3x3 = 27 pumpkins instead of 9.
A 4x4 pumpkin yields 4x4x4 = 64 pumpkins instead of 16.
A 5x5 pumpkin yields 5x5x5 = 125 pumpkins instead of 25.
A nxn pumpkin yields nxnx6 pumpkins for n >= 6.
It's a good idea to get at least 6x6 size pumpkins to get the full multiplier. 
This means that even if you plant a pumpkin on every tile in a square, one of the pumpkins may die and prevent the mega pumpkin from growing.

What you can see above is the official text, but there is something it does not tell you. The `can_harvest()` function can only be called where the drone is, and as we know, moving the drone makes it inefficient. But I found that the `measure()` function also works on rotten pumpkins, but that can be cast sideways, meaning the drone only has to travel ~1/3 of the original distance since it can look at the two rows next to the one it's scanning.

Otherwise, I just store the whole field in the drone's memory, and after it knows the whole field, it replants the rotten pumpkins, then rescanns them. It repeats this until the whole field is one giant pumpkin.
<img width="1574" height="750" alt="image" src="https://github.com/user-attachments/assets/b0c6e5d0-6a83-4920-9019-9162fd3d8224" />

</details>

<details>
<summary>Polyculture</summary>

> You may have already noticed that sometimes plants yield more when planted together.
Grass, bushes, trees, and carrots yield more when they have the right plant companion. Companion preference is different for each individual plant and cannot be predicted. Fortunately, the companion preference of the plant under the drone can be measured using `get_companion()`. It returns a tuple where the first element is the type of plant it wants as its companion and the second element is the position where it wants its companion.
`plant_type, (x, y) = get_companion()`
For example if you plant a bush and then call `get_companion()` it will return something like `(Entities.Carrot, (3, 5))`. This means that this bush would like to have carrots at the position (3,5). So if you plant carrots at (3,5) and then harvest the bush, it will yield more wood. The growth stage of the carrot doesn't matter.
A plant's companion preference can be either `Entities.Grass`, `Entities.Bush`, `Entities.Tree` or `Entities.Carrot`. Each plant chooses this randomly, but it will always choose a different plant than itself. The position can also be any position within 3 moves of the plant except the position of the plant itself.
If there is no plant under the drone that has a companion preference `get_companion()` will return None.
Before polyculture is unlocked, the yield multiplier is 5. It doubles everytime you upgrade it.

I'd add to the dev's description that a plant cannot have a companion that is the same type as it is. Otherwise, I can't add anything smart to this. I made it random what the drone plants at the spot, then goes through the whole map; if the plant has its companion, it is harvested; otherwise, it gets its companion. *In case you are wondering: No, if **plant X** wants **plant Y** as its companion, that does not mean that **Plant Y** wants **Plant X** as its companion.*
<img width="1097" height="701" alt="image" src="https://github.com/user-attachments/assets/c6d8c967-819b-4e70-b20c-9ddc9876f1d8" />

</details>

<details>
<summary>Sunflower planting</summary>

> Sunflowers collect the power of the sun. You can harvest that power. 
Planting them works exactly like planting carrots or pumpkins. 
Harvesting a grown sunflower yields power.
If there are at least 10 sunflowers on the farm and you harvest the one with the largest number of petals you get 8 times more power!
If you harvest a sunflower while there is another sunflower with more petals, the next sunflower you harvest will also only give you the normal amount of power (not the 8x bonus).
`measure()` returns the number of petals of the sunflower under the drone.
Sunflowers have at least 7 and at most 15 petals.
They can already be measured before they are fully grown.
Several sunflowers can have the same number of petals so there can also be several sunflowers with the largest number of petals. In this case, it doesn't matter which one of them you harvest.
As long as you have power the drone will use it to run twice as fast. 
It consumes 1 power every 30 actions (like moves, harvests, plants...)
Executing other code statements can also use power but a lot less than drone actions.
In general, everything that is sped up by speed upgrades is also sped up by power.
Anything sped up by power also uses power proportional to the time it takes to execute it, ignoring speed upgrades.

The most effective way to do this is to work in waves. I've experimented with replanting the harvested flowers straightaway, but that took more time because I had to wait for them to grow again if the new flower had the most petals. Instead, I `measure()` the whole field, put everything in a dictionary, where the key is the number of petals, and the value is a list of coordinates where those sunflowers were found. Then it works its way backward and collects them. Replant, and do again.
<img width="1164" height="746" alt="image" src="https://github.com/user-attachments/assets/3f64ba5e-df82-4ff3-8b1f-72430c0ed1a2" />

Also, I've submitted my code for the global leaderboard, and I've reached rank #73 from multiple hundred people.
![Sunflower_Single_Leaderboard](https://github.com/user-attachments/assets/b79af748-e4fd-4d96-9190-462c6812ce89)


</details>

<details>
<summary>Cactus planting</summary>

> Like other plants, cacti can be grown on soil and harvested as usual.
However, they come in various sizes and have a strange sense of order.
If you harvest a fully-grown cactus and all neighboring cacti are in sorted order, it will also harvest all neighboring cacti recursively.
A cactus is considered to be in sorted order if all neighboring cacti to the North and East are fully grown and larger or equal in size and all neighboring cacti to the South and West are fully grown and smaller or equal in size.
The harvest will only spread if all adjacent cacti are fully grown and in sorted order.
This means that if a square of grown cacti is sorted by size and you harvest one cactus, it will harvest the entire square.
A fully grown cactus will appear brown if it is not sorted. Once sorted, it will turn green again.
You will receive cactus equal to the number of harvested cacti squared. So if you harvest n cacti simultaneously you will receive n^2 `Items.Cactus`.
The size of a cactus can be measured with `measure()`.
It is always one of these numbers: 0,1,2,3,4,5,6,7,8,9.
You can also pass a direction into `measure(direction)` to measure the neighboring tile in that direction of the drone.
You can swap a cactus with its neighbor in any direction using the `swap()` command.
`swap(direction)` swaps the object under the drone with the object one tile in the direction of the drone.

<img width="854" height="392" alt="image" src="https://github.com/user-attachments/assets/c6285e1a-de54-44c8-826e-18576db1aac5" />


In short: The cacti have to be sorted, so the largest ones are on the east or north. We cannot insert, so the logical answer for the fastest algorithm is the **improved bubble sort**.
<img width="1616" height="994" alt="image" src="https://github.com/user-attachments/assets/6d388dce-34e1-4ee8-a604-84356929cb1d" />

I've also submitted my algorithm to the global leaderboard, and it got rank #127. (The best 300 are visible, so there were at least that many people who tried).
![Cactus_Single_Leaderboard](https://github.com/user-attachments/assets/90337f4e-a84f-439f-afe3-2cb603008ead)

</details>

<details>
<summary>Dino Ranching</summary>

> Dinosaurs are ancient, majestic creatures that can be farmed for ancient bones.
Unfortunately dinosaurs have gone extinct a long time ago, so the best we can do now is dressing up as one.
For this purpose you have received the new dinosaur hat.
The hat can be equipped with
`change_hat(Hats.Dinosaur_Hat)`
Unfortunately it doesn't quite look like on the advertisement...
If you equip the dinosaur hat and have enough cactus, an apple will automatically be purchased and placed under the drone.
When the drone is over an apple and moves again, it will eat the apple and grow its tail by one. If you can afford it, a new apple will be purchased and placed in a random location.
The apple cannot spawn if something else is planted where it wants to be.
The tail of the dinosaur will be dragged behind the drone filling the previous tiles the drone moved over. If a drone tries to move on top of the tail `move()` will fail and return False. 
The last segment of the tail will move out of the way during the move, so you can move onto it. However, if the snake fills out the whole farm, you will not be able to move anymore. So you can check if the snake is fully grown by checking if you can't move anymore.
While wearing the dinosaur hat, the drone can't move over the farm border to get to the other side.
Using `measure()` on an apple will return the position of the next apple as a tuple.
`next_x, next_y = measure()`
When the hat is unequipped again by equipping a different hat, the tail will be harvested.
You will receive bones equal to the tail length squared. So for a tail of length n you will receive n^2 Items.Bone. 
For Example:
length 1 => 1 bone
length 2 => 4 bones
length 3 => 9 bones
length 4 => 16 bones
length 16 => 256 bones
length 100 => 10000 bones
The Dinosaur Hat is very heavy, so if you equip it, it will make `move()` take 400 ticks instead of 200. However, each time you pick up an apple, the number of ticks used by `move()` is reduced by 3% (rounded down), because a longer tail can help you move.
The following loop prints the number of ticks used by `move()` after any number of apples:
```
ticks = 400
for i in range(100):
    print("ticks after ", i, " apples: ", ticks)
    ticks -= ticks * 0.03 // 1
```

Honestly, I didn't really like this challenge, since it was way more complex than what it was useful for. As the dev says, it's really easy to make a snake that just goes around the map in a loop but does not specifically seek out apples. And that makes so much bone in one round that with two rounds on the largest map, you can make more bone than you can spend on upgrades. This takes about an hour, so I did not think it was worth the time investment to make a better one. *(Since I didn't have an idea, it would have taken much more time, and I wanted to get to the exciting part, the maze).*
<img width="1679" height="618" alt="image" src="https://github.com/user-attachments/assets/f8b83c1d-946a-4361-a8c9-45158f8211dc" />

</details>

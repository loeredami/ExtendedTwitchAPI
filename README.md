# Setup new project.
1. Install twichAPI
```
pip install twitchAPI --upgrade
```
2. Copy Repository
3. Enter App ID in file: app_id
4. Enter App Secret in file: app_secret
5. Add redirect to twitch Application: http://localhost:17563
6. Create Plugins Folder
7. Write first plugin
```python
import asyncio
import random
import sys
from datetime import datetime, timedelta

from twitchAPI.chat import ChatCommand

sys.path.append("../")
sys.path.append("../../")

import Plugin
import PluginManager

class Fun(Plugin.Plugin):
    n = fullmoon.NextFullMoon()

    def __init__(self):
        super().__init__("Fun")

fun = Fun()
async def ami(cmd: ChatCommand):
    if len(cmd.parameter) == 0:
        await cmd.send("Yes, you are yourself")
        return
    if cmd.parameter.lower() in cmd.user.name.lower():
        await cmd.send(f"Yes, you are {cmd.parameter}.")
    else:
        await cmd.send(f"No, you are not {cmd.parameter}.")

async def dramatic_pause(cmd: ChatCommand):
    await cmd.send("SOMETHING AMAZING IS GOING TO HAPPEN . . . . .")
    await asyncio.sleep(random.randint(3,10))
    await cmd.send("Nevermind, nothing happened")

async def gacha_pull(cmd: ChatCommand):

    await cmd.send(f"{cmd.user.name} is pulling something . . . . .")
    await asyncio.sleep(3)
    if random.randint(0, 20) == 3:
        await cmd.send("OMG THE TRAIL IS GOLDEN")
        await asyncio.sleep(3)
        await cmd.send("... it's qiqi")
        return
    await cmd.send("Nothing usefull.")

async def flip(cmd: ChatCommand):
    
    if random.randint(0, 100) < 50:
        await cmd.reply("Unfortunately, it landed on it's side... whatever that means.")
    elif random.randint(0, 100) < 50:
        await cmd.reply(f"Heads.")
    else:
        await cmd.reply(f"Tails.")

async def stinky(cmd: ChatCommand):
    num = 0

    for i in range(-10, 10):
        num += random.randint(int(-i*0.8),i*len(cmd.user.name)) * (1/max(1,((Fun.n.set_origin_now().next_full_moon()-datetime.now()).days)))
    
    num = min(num, 100)
    num = round(num, 2)
    
    if len(cmd.parameter) != 0:
        await cmd.send(f"{cmd.parameter} is {num}% stinky.")
        return

    await cmd.send(f"{cmd.user.display_name} is {num}% stinky.")

async def sus(cmd: ChatCommand):
    num = random.randint(0, 100)
    
    if len(cmd.parameter) != 0:
        await cmd.send(f"{cmd.parameter} is {num}% sus.")
        return

    await cmd.send(f"{cmd.user.display_name} is {num}% sus.")

async def braincells(cmd: ChatCommand):
    num = random.randint(-10,20)
    if len(cmd.parameter) != 0:
        await cmd.send(f"{cmd.parameter} has {num} braincells.")
        return

    await cmd.send(f"{cmd.user.display_name} has {num} braincells.")

fun.add_command(ami, "ami")
fun.add_command(dramatic_pause, "dramatic_break")
fun.add_command(gacha_pull, "gacha_pull")
fun.add_command(stinky, "stinky")
fun.add_command(braincells, "braincells")
fun.add_command(sus, "sus")
fun.add_command(flip, "coin")

def setup(pl: PluginManager.PluginManager):
    pl.setup(fun)
```
8. Run the Client
```
python client.py
```

from twitchAPI.chat import Chat
from twitchAPI.twitch import Twitch
import asyncio
class PluginManager:
    def __init__(self, twitch, chat):
        self.chat: Chat = chat
        self.twitch: Twitch = twitch
        self.plugins = {}

    def setup(self, plugin):
        self.plugins[plugin.name] = plugin
        plugin.manager = self
        for name, command in plugin.commands.items():
            self.chat.register_command(name, command)

    async def on_tick(self):
        for _, plugin in self.plugins.items():
            await plugin.on_tick()
        await asyncio.sleep(1/20)
    async def on_message(self, msg):
        for _, plugin in self.plugins.items():
            await plugin.on_message(msg)
    
    async def on_ready(self, ready):
        for key, plugin in self.plugins.items():
            print("Readying Module...", key)
            await plugin.on_ready(ready)
        print("Ready")
    
    async def on_sub(self, sub):
        for _, plugin in self.plugins.items():
            await plugin.on_sub(sub)
    
    async def on_raid(self, data):
        for _, plugin in self.plugins.items():
            await plugin.on_raid(data)
            
    async def on_join(self, data):
        for _, plugin in self.plugins.items():
            await plugin.on_join(data)

    async def on_joined(self, data):
        for _, plugin in self.plugins.items():
            await plugin.on_joined(data)
    
    async def on_room_state_change(self, data):
        for _, plugin in self.plugins.items():
            await plugin.on_room_state_change(data)

    async def on_left(self,data):
        for _, plugin in self.plugins.items():
            await plugin.on_left(data)
    
    async def on_whisper(self,data):
        for _, plugin in self.plugins.items():
            await plugin.on_whisper(data)
    
    async def on_user_left(self,data):
        for _, plugin in self.plugins.items():
            await plugin.on_user_left(data)
    
    async def on_notice(self,data):
        for _, plugin in self.plugins.items():
            await plugin.on_notice(data)
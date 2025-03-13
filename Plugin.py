from PluginManager import PluginManager
from twitchAPI.chat import ChatMessage, EventData, JoinedEvent, LeftEvent, NoticeEvent, JoinEvent


class Plugin:
    def __init__(self, name):
        self.commands = {}
        self.name = name
        self.manager: PluginManager

    
    def add_command(self, func, name):
        self.commands[name] = func

    async def on_message(self, msg: ChatMessage):
        #print(self.name, msg.room.name, msg.user.display_name, msg.text)
        pass

    async def on_ready(self, event: EventData):
        #print(self.name, "ready", event.chat.username)
        pass

    async def on_tick(self):
        pass
    
    async def on_sub(self, sub):
        pass#print("Unhandled by", self.name, sub)
    
    async def on_raid(self, data):
        #print("Unhandled by", self.name, data)
        pass
    
    async def on_join(self, data: JoinEvent):
        #print(self.name, data.user_name, "joined", data.room.name)
        pass

    async def on_joined(self, data: JoinedEvent):
        #print(self.name, data.user_name, "joined", data.room_name)
        pass

    async def on_room_state_change(self, data):
        pass
    
    async def on_left(self, data: LeftEvent):
        #print(self.name, data.user_name, "joined", data.room_name)
        pass
    
    async def on_whisper(self, data):
        #print("Unhandled by", self.name, data)
        pass
    
    async def on_user_left(self, data: LeftEvent):
        #print(self.name, data.user_name, "joined", data.room_name)
        pass
    
    async def on_notice(self, data: NoticeEvent):
        print("Unhandled by", self.name, data.message, "in", data.room.name)
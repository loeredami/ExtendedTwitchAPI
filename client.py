while True:
    try:
        import asyncio
        import importlib
        import os
        import sys

        from PluginManager import PluginManager
        from twitchAPI.chat import Chat
        from twitchAPI.oauth import UserAuthenticator
        from twitchAPI.twitch import Twitch
        from twitchAPI.type import AuthScope, ChatEvent

        pl: PluginManager

        sys.path.append("../")

        from Shared.temporaryData import TemporaryDataCollection

        APP_SECRET, APP_ID = "", ""

        bootTDC = TemporaryDataCollection()
        try:
            with open("app_secret", "r") as src:
                APP_SECRET = bootTDC.add(src.read())

            with open("app_id", "r") as src:
                APP_ID = bootTDC.add(src.read())
        except Exception as e:
            exit(f"Could not start program. {e}")


        USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT, AuthScope.WHISPERS_READ, AuthScope.USER_MANAGE_WHISPERS, AuthScope.CLIPS_EDIT]

        async def run():
            global pl
            print("Setting Up Twitch")
            twitch = await Twitch(bootTDC.get(APP_ID), bootTDC.get(APP_SECRET))
            auth = UserAuthenticator(twitch, USER_SCOPE)
            print("Authenticating")
            
            tokensID = bootTDC.add(await auth.authenticate())
            token, refresh_token = bootTDC.get(tokensID)
            await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)
            print("Authenticated")

            del token, refresh_token

            chat = await Chat(twitch)

            pl = PluginManager(twitch, chat)


            chat.register_event(ChatEvent.READY, pl.on_ready)
            chat.register_event(ChatEvent.MESSAGE, pl.on_message)
            chat.register_event(ChatEvent.SUB, pl.on_sub)
            chat.register_event(ChatEvent.RAID, pl.on_raid)
            chat.register_event(ChatEvent.JOIN, pl.on_join)
            chat.register_event(ChatEvent.JOINED, pl.on_joined)
            chat.register_event(ChatEvent.ROOM_STATE_CHANGE, pl.on_room_state_change)
            chat.register_event(ChatEvent.LEFT, pl.on_left)
            chat.register_event(ChatEvent.WHISPER, pl.on_whisper)
            chat.register_event(ChatEvent.USER_LEFT, pl.on_user_left)
            chat.register_event(ChatEvent.NOTICE, pl.on_notice)

            for plugin in os.listdir("./plugins"):
                print("Loading plugin",plugin)
                if not plugin.endswith(".py"): continue
                mod = importlib.import_module(f"plugins.{plugin.replace('.py','')}")
                print(mod, mod.setup(pl))


            print("Running Main Process")
            chat.start()
            print("Ready.")
            try:
                while True:
                    await pl.on_tick()
                    await asyncio.sleep(1)
            finally:
                chat.stop()
                await twitch.close()


        asyncio.run(run())
    except:
        pass
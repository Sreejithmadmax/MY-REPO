import re, asyncio, random
import os
from pyrogram import Client
           

Sree = Client(
              "NEW BOT SET",
              bot_token = os.environ["BOT_TOKEN"],
              api_id = int(os.environ["API_ID"]),
              api_hash = os.environ["API_HASH"],
              plugins=dict(root="plugins"),
              )                   

async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")


Sree.run() 

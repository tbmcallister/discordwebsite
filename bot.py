import discord
import os
import logging
import asyncio
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)
load_dotenv()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

async def is_user_online(user_id):
    try:
        # Fetch the user
        user = await client.fetch_user(user_id)
        
        # Check if the user is online
        return user.status == discord.Status.online
    
    except discord.errors.NotFound:
        # The user was not found
        return False
    
    except discord.errors.Forbidden:
        # The bot doesn't have permission to fetch user information
        print("Bot doesn't have permission to fetch user information.")
        return False
    
    except discord.errors.HTTPException as e:
        # Handle other Discord API errors
        print(f"Error while fetching user: {e}")
        return False
    
    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return False


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    print('------')

async def start_bot():
    await client.login(os.getenv('TOKEN'))
    await client.start(os.getenv('TOKEN'))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())

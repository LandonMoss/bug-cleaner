import discord
from discord.ext import commands
import asyncio
from config import config  # Ensure this import is correct

# Bot setup
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def main():
    # Load extensions
    await load_cogs()
    # Start bot
    await bot.start(config['token'])

async def load_cogs():
    for cog in config['cogs']:
        await bot.load_extension(cog)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    bot.bug_report_channel = discord.utils.get(bot.get_all_channels(), name='bug-reports')

asyncio.run(main())

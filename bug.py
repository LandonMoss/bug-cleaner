import discord
from discord.ext import commands
import asyncio
from config import config  # Ensure this import is correct

# Bot setup
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

#Track Command usage
command_usage = {}

async def main():
    # Load extensions
    await load_cogs()
    # Start bot
    await bot.start(config['token'])

async def load_cogs():
    for cog in config['cogs']:
        await bot.load_extension(cog) #Load each cog

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    bot.bug_report_channel = discord.utils.get(bot.get_all_channels(), name='bug-reports')

# Event to track command usage
@bot.event
async def on_command(ctx):
    print(f"Command used: {ctx.command.name}") #Print everytime a command is used
    command_name = ctx.command.name
    if command_name in command_usage:
        command_usage[command_name] += 1
    else:
        command_usage[command_name] = 1

# Command to display command usage statistics
@bot.command(name='command_usage', help='Displays the command usage statistics.')
async def display_command_usage(ctx):
    if not command_usage:
        await ctx.send('No commands have been used yet.')
    else:
        usage_stats = '\n'.join([f'{cmd}: {count} times' for cmd, count in command_usage.items()])
        await ctx.send(f'Command usage statistics:\n{usage_stats}')

asyncio.run(main())

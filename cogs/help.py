# cogs/help.py
import discord
from discord.ext import commands

class HelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help", description="Here is a list of available commands:", color=discord.Color.blue())
        for cog, commands in mapping.items():
            command_list = "\n".join([f"!{command.name}" for command in commands])
            if command_list:
                embed.add_field(name=cog.qualified_name if cog else "No Category", value=command_list, inline=False)
        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=f"!{command.name}", description=command.help or "No description provided", color=discord.Color.blue())
        embed.add_field(name="Usage", value=f"!{command.name} {command.signature}")
        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(title=f"{cog.qualified_name} Commands", description=cog.description or "No description provided", color=discord.Color.blue())
        command_list = "\n".join([f"!{command.name}" for command in cog.get_commands()])
        if command_list:
            embed.add_field(name="Commands", value=command_list, inline=False)
        channel = self.get_destination()
        await channel.send(embed=embed)

class HelpCog(commands.Cog, name="Help"):
    def __init__(self, bot):
        self.bot = bot
        bot.help_command = HelpCommand()

    @commands.command()
    async def help(self, ctx, *args):
        """Shows this help message"""
        if args:
            command_name = args[0]
            command = self.bot.get_command(command_name)
            if command:
                await ctx.send_help(command)
            else:
                await ctx.send(f"No command named '{command_name}' found.")
        else:
            await ctx.send_help()

async def setup(bot):
    await bot.add_cog(HelpCog(bot))

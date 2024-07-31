from discord.ext import commands
import logging

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Missing required argument. Please check your command and try again silly goose.')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('Bad argument bozo. Please check your command and try again.')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found moron. Please check your command and try again.')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the required permissions to run this command silly goose.')
        else:
            await ctx.send('An error occurred while processing your command.')
            logging.error(f'Error in command {ctx.command}: {error}')

def setup(bot):
    bot.add_cog(ErrorHandler(bot))

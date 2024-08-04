from discord.ext import commands
from utils.file_utils import load_bug_data

class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      #  self.bug_data = load_bug_data()

    @commands.command()
    async def view_bugs(self, ctx):
        user_id = str(ctx.author.id)
        #Check if user has not submitted any bugs
        if user_id not in self.bug_data or len(self.bug_data[user_id]) == 0:
            await ctx.send('You have not submitted any bugs.')
            return

        bug_list = '' #Store bug details
        for bug in self.bug_data[user_id]:
            bug_list += f"ID: {bug['id']}, Description: {bug['description']}, Status: {bug['status']}, Rewarded: {bug['rewarded']}\n"
        await ctx.send(f'Your submitted bugs:\n{bug_list}')

    @commands.command()
    async def search_bugs(self, ctx, *, keyword):
        user_id = str(ctx.author.id)
        #Check if user has not submitted any bugs
        if user_id not in self.bug_data or len(self.bug_data[user_id]) == 0:
            await ctx.send('You have not submitted any bugs.')
            return

            #See if the bugs match the keyword in their description
        matched_bugs = [bug for bug in self.bug_data[user_id] if keyword.lower() in bug['description'].lower()]
        if not matched_bugs: #Check if no bugs matched the search
            await ctx.send('No bugs matched your search.')
            return

        bug_list = ''
        for bug in matched_bugs:
            bug_list += f"ID: {bug['id']}, Description: {bug['description']}, Status: {bug['status']}, Rewarded: {bug['rewarded']}\n"
        await ctx.send(f'Bugs matching "{keyword}":\n{bug_list}')

def setup(bot):
    bot.add_cog(UserCommands(bot))

from discord.ext import commands
#from utils.file_utils import load_bug_data, save_bug_data

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot #Initialize bot instance
       # self.bug_data = load_bug_data()

    @commands.command() #Define command reward
    @commands.has_permissions(administrator=True) #Restrict command to admin 
    async def reward(self, ctx, user: discord.User, bug_id: int):
        user_id = str(user.id) #Get user Id as string
        #Check if bug ID is invalid or bug has already been rewarded
        if user_id not in self.bug_data or len(self.bug_data[user_id]) < bug_id or self.bug_data[user_id][bug_id - 1]['rewarded']:
            await ctx.send('Invalid bug ID or already rewarded.') #Send error message
            return
    #Bug has been rewarded
        self.bug_data[user_id][bug_id - 1]['rewarded'] = True
        save_bug_data(self.bug_data) #Save bug data
        await ctx.send(f'Bug #{bug_id} by {user.mention} has been rewarded.')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def update_status(self, ctx, user: discord.User, bug_id: int, status: str):
        user_id = str(user.id) #Get user ID as string
        if user_id not in self.bug_data or len(self.bug_data[user_id]) < bug_id:
            await ctx.send('Invalid bug ID.')
            return
            #Check if status is valid
        if status not in ['open', 'in progress', 'closed']:
            await ctx.send('Invalid status. Please use "open", "in progress", or "closed".')
            return
        #Update status of the bug
        self.bug_data[user_id][bug_id - 1]['status'] = status
        save_bug_data(self.bug_data)
        await ctx.send(f'Status of bug #{bug_id} by {user.mention} has been updated to {status}.')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def list_all_bugs(self, ctx):
        if not self.bug_data: #Check if there is not bugs submitted
            await ctx.send('No bugs have been submitted.')
            return

        all_bugs = '' #Initialize a string to store all bugs
        for user_id, bugs in self.bug_data.items(): #Iterate through the bug data
            user = await self.bot.fetch_user(int(user_id)) #Fetch user object
            all_bugs += f'Bugs submitted by {user.mention}:\n' #Add user mention to string
            for bug in bugs: #Iterate throguh the bugs submitted by the user
                all_bugs += f"ID: {bug['id']}, Description: {bug['description']}, Status: {bug['status']}, Rewarded: {bug['rewarded']}\n"
            all_bugs += '\n'
        await ctx.send(f'All submitted bugs:\n{all_bugs}') #Send the list of all bugs

def setup(bot):
    bot.add_cog(AdminCommands(bot))
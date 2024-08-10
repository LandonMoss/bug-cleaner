from discord.ext import commands
from utils.database import db
import json
import os

class BugManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot #Initialize bot instance

    @commands.command(help="Submit a new bug report.")
    async def submit_bug(self, ctx):
        await ctx.send('Please provide the bug description:') 
        #Check message is from the same user and channel
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        
        msg = await self.bot.wait_for('message', check=check) #Wait for the users message
        bug_description = msg.content #Store bug description
        
        await ctx.send('Please provide the bug priority (low, medium, high):')
        msg = await self.bot.wait_for('message', check=check)
        priority = msg.content.lower()
        
        if priority not in ['low', 'medium', 'high']:
            await ctx.send('Invalid priority. Please use "low", "medium", or "high".')
            return
        
        user_id = str(ctx.author.id)
        db.add_bug(user_id, bug_description, 'open', priority)
        await ctx.author.send(f'Thank you for your bug submission!')
        await ctx.send(f'Bug submitted by {ctx.author.mention} with priority {priority}.')

    @commands.command(help="View your submitted bugs.")
    async def view_bugs(self, ctx):
        user_id = str(ctx.author.id)
        bugs = db.get_bugs(user_id) #Retrieve users bugs from database
        if not bugs:
            await ctx.send('You have not submitted any bugs.')
            return

        bug_list = ''
        for bug in bugs:
            #Add each bug details to the string
            bug_list += f"ID: {bug[0]}, Description: {bug[2]}, Status: {bug[3]}, Rewarded: {'Yes' if bug[5] else 'No'}\n"
        await ctx.send(f'Your submitted bugs:\n{bug_list}')

    @commands.command(help="Update the status of a bug (admin only).")
    @commands.has_permissions(administrator=True)
    async def update_status(self, ctx, bug_id: int, status: str):
        #validate the status input
        if status not in ['open', 'in progress', 'closed']:
            await ctx.send('Invalid status. Please use "open", "in progress", or "closed".')
            return

        db.update_bug_status(bug_id, status) #Update bug status in database
        await ctx.send(f'Status of bug #{bug_id} has been updated to {status}.')

    @commands.command(help="Reward a bug (admin only).")
    @commands.has_permissions(administrator=True)
    async def reward(self, ctx, bug_id: int):
        db.reward_bug(bug_id) #Mark bug rewarded in database
        await ctx.send(f'Bug #{bug_id} has been rewarded.')

    @commands.command(help="Delete a bug (admin only).")
    @commands.has_permissions(administrator=True)
    async def delete_bug(self, ctx, bug_id: int):
        db.delete_bug(bug_id) #Delete bug from database
        await ctx.send(f'Bug #{bug_id} has been deleted.')

    @commands.command(help="List all submitted bugs (admin only).")
    @commands.has_permissions(administrator=True)
    async def list_all_bugs(self, ctx):
        all_bugs = db.get_all_bugs() #Retrive all bugs from database
        if not all_bugs: #Check if theres no bugs silly goose
            await ctx.send('No bugs have been submitted.')
            return

        bug_list = ''
        for bug in all_bugs:
            bug_list += f"ID: {bug[0]}, User ID: {bug[1]}, Description: {bug[2]}, Status: {bug[3]}, Priority: {bug[4]}, Rewarded: {'Yes' if bug[5] else 'No'}\n"
        await ctx.send(f'All submitted bugs:\n{bug_list}')

    @commands.command(help="Get bug statistics.")
    async def stats(self, ctx):
        #Initalized bug counters
        total_bugs = 0
        open_bugs = 0
        in_progress_bugs = 0
        closed_bugs = 0

        all_bugs = db.get_all_bugs() #Retrive bugs from database
        for bug in all_bugs: #Iterate through all the bugs
            total_bugs += 1
            if bug[3] == 'open': #Check if bug is open
                open_bugs += 1
            elif bug[3] == 'in progress': #Check if in progress
                in_progress_bugs += 1
            elif bug[3] == 'closed': #Check if closed
                closed_bugs += 1

        await ctx.send(f"**Bug Statistics**\n"
                   f"Total Bugs: {total_bugs}\n"
                   f"Open Bugs: {open_bugs}\n"
                   f"In Progress Bugs: {in_progress_bugs}\n"
                   f"Closed Bugs: {closed_bugs}")
        
    

async def setup(bot):   
    await bot.add_cog(BugManagement(bot))

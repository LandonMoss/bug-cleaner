import discord
from discord.ext import commands
import os
import json

class BugManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        if os.path.exists('bugs.json'):
            with open('bugs.json', 'r') as f:
                self.bug_data = json.load(f)
        else:
            self.bug_data = {}

    def save_bug_data(self):
        with open('bugs.json', 'w') as f:
            json.dump(self.bug_data, f, indent=4)

    @commands.command()
    async def submit_bug(self, ctx):
        await ctx.send('Please provide the bug description:')

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        msg = await self.bot.wait_for('message', check=check)
        bug_description = msg.content

        await ctx.send('Please provide the bug priority (low, medium, high):')
        msg = await self.bot.wait_for('message', check=check)
        priority = msg.content.lower()

        if priority not in ['low', 'medium', 'high']:
            await ctx.send('Invalid priority. Please use "low", "medium", or "high".')
            return

        user_id = str(ctx.author.id)
        if user_id not in self.bug_data:
            self.bug_data[user_id] = []
        bug_id = len(self.bug_data[user_id]) + 1
        self.bug_data[user_id].append({
            'id': bug_id,
            'description': bug_description,
            'status': 'open',
            'priority': priority,
            'rewarded': False
        })
        self.save_bug_data()
        await ctx.author.send(f'Thank you for your bug submission! Bug #{bug_id} has been recorded.')
        await ctx.send(f'Bug #{bug_id} submitted by {ctx.author.mention} with priority {priority}.')
        if self.bot.bug_report_channel:
            await self.bot.bug_report_channel.send(f'New bug submitted by {ctx.author.mention}:\nID: {bug_id}, Description: {bug_description}, Priority: {priority}')

    @commands.command()
    async def view_bugs(self, ctx):
        user_id = str(ctx.author.id)
        if user_id not in self.bug_data or len(self.bug_data[user_id]) == 0:
            await ctx.send('You have not submitted any bugs.')
            return

        bug_list = ''
        for bug in self.bug_data[user_id]:
            bug_list += f"ID: {bug['id']}, Description: {bug['description']}, Status: {bug['status']}, Rewarded: {bug['rewarded']}\n"
        await ctx.send(f'Your submitted bugs:\n{bug_list}')

    # Define other commands...

async def setup(bot):
    await bot.add_cog(BugManagement(bot))

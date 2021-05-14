from discord.ext import commands
from ..logic import functions


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', description='Ping! :)')
    async def ping(self, context, *args):
        """Do a ping!"""
        if not context.author.bot:
            # If no arguments are given do a simple 'Pong'.
            if len(*args) is 0:
                await context.send("Pong!")
            # If 1 argument is given ping someone his username once
            elif len(*args) is 1:
                member = find_user(context, str(args[0]))
                if member is not None:
                    await context.send("Ping! " + "<@" + str(member.id) + ">!")
                else:
                    await context.send("Could not find the member you are asking for.")
            # If 2 arguments are given ping someone his username multiple times (based on parameter)
            elif len(*args) is 2:
                member = find_user(context, str(args[0]))
                if member is not None:
                    if functions.is_int(args[1]):
                        for i in range (0, int(args[1])):
                            await context.send("Ping! " + "<@" + str(member.id) + ">!")
                            if i > 9:
                                await context.send("I've spammed enough now.")
                                break
                    else:
                        await context.send("You need to set a number. Try using !ping [username] [amount]")
                else:
                    await context.send("Could not find the member you are asking for. Try using !ping [username] [amount]")
            # If none of the correct parameters are given do this.
            else:
                await context.send("I don't understand what you are trying to do. Try using !ping [username] [amount]")

    @commands.command(name='pong', description='Pong! (:')
    async def pong(self, context):
        """Do a pong!"""
        if not context.author.bot:
            await context.send("Ping!")


def find_user(context, username):
    for member in context.channel.members:
        if member.name.lower() == username.lower():
            return member.id
        elif member.nick.lower() == username.lower():
            return member.id
        elif member.display_name.lower() == username.lower():
            return member.id
    return None




def setup(bot):
    bot.add_cog(Ping(bot))
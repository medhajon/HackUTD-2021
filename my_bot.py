# import Discord Package
import discord
from discord.ext import commands
from datetime import timedelta, datetime
import os
import json
import random 
import time
import asyncio


# client (our Bot)
client = commands.Bot(command_prefix='--')

@client.command(name='!assign')
async def version(context):

    myEmbed = discord.Embed(title="Current Version", description="The bot is in Version 1.0", color=0x00ff00)
    myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Release:", value="July 18th, 2020", inline=False)
    myEmbed.set_footer(text="This is my sample footer")
    myEmbed.set_author(name="MJ")

    await context.message.channel.send(embed=myEmbed)

@client.event
async def on_ready():
    #Do Stuff
    general_channel = client.get_channel(815538922531979334)
    await general_channel.send('Hello, World!')

@client.event
async def on_message(message):
    general_channel = client.get_channel(815538922531979334)
    if message.content == '!assign':       

        myEmbed = discord.Embed(title="HW1", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit...", color=0x00ff00)
     ##   myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date due:", value="01/01/2021", inline=False)
        myEmbed.set_image(url="https://media.istockphoto.com/vectors/report-on-sheet-of-paper-vector-icon-flat-isolated-vector-id1223982866?k=6&m=1223982866&s=612x612&w=0&h=yHf0YOtEHSmY6Z9GKkJl63w9Jp-YwdRLHwFmI3iRqfE=")
        myEmbed.set_footer(text="Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
        myEmbed.set_author(name="Prof XYZ")

        await general_channel.send(embed=myEmbed)

    if message.content == '!add':
        print("Information is added")
        myEmbed = discord.Embed(title="HW2", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit...", color=0x00ff00)
     ##   myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date due:", value="01/23/2021", inline=False)
        myEmbed.set_image(url="https://media.istockphoto.com/vectors/report-on-sheet-of-paper-vector-icon-flat-isolated-vector-id1223982866?k=6&m=1223982866&s=612x612&w=0&h=yHf0YOtEHSmY6Z9GKkJl63w9Jp-YwdRLHwFmI3iRqfE=")
        myEmbed.set_footer(text="Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
        myEmbed.set_author(name="Prof XYZ")

        await general_channel.send(embed=myEmbed)
        await general_channel.send("New Date is added")
    
    if message.content == '!change':
        dateList = []
        myEmbed = discord.Embed(title="HW1", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit...", color=0x00ff00)
     ##   myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date due:", value="01/10/2021", inline=False)
        myEmbed.set_image(url="https://media.istockphoto.com/vectors/report-on-sheet-of-paper-vector-icon-flat-isolated-vector-id1223982866?k=6&m=1223982866&s=612x612&w=0&h=yHf0YOtEHSmY6Z9GKkJl63w9Jp-YwdRLHwFmI3iRqfE=")
        myEmbed.set_footer(text="Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
        myEmbed.set_author(name="Prof XYZ")

        await general_channel.send(embed=myEmbed)
        await general_channel.send("Date has been changed")
        
    
    if message.content == '!clear':
        dataList = []
        await general_channel.send(dataList)

    if message.content == '!list':
        dataList = []

        myEmbed = discord.Embed(title="HW1", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit...", color=0x00ff00)
     ##   myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date due:", value="01/01/2021", inline=False)
        myEmbed.set_image(url="https://media.istockphoto.com/vectors/report-on-sheet-of-paper-vector-icon-flat-isolated-vector-id1223982866?k=6&m=1223982866&s=612x612&w=0&h=yHf0YOtEHSmY6Z9GKkJl63w9Jp-YwdRLHwFmI3iRqfE=")
        myEmbed.set_footer(text="Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
        myEmbed.set_author(name="Prof XYZ")

        await general_channel.send(embed=myEmbed)

        myEmbed = discord.Embed(title="HW1.5", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit...", color=0x00ff00)
     ##   myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date due:", value="01/05/2021", inline=False)
        myEmbed.set_image(url="https://media.istockphoto.com/vectors/report-on-sheet-of-paper-vector-icon-flat-isolated-vector-id1223982866?k=6&m=1223982866&s=612x612&w=0&h=yHf0YOtEHSmY6Z9GKkJl63w9Jp-YwdRLHwFmI3iRqfE=")
        myEmbed.set_footer(text="Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
        myEmbed.set_author(name="Prof XYZ")

        await general_channel.send(embed=myEmbed)

        myEmbed = discord.Embed(title="Lab 1.1", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit...", color=0x00ff00)
     ##   myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date due:", value="01/06/2021", inline=False)
        myEmbed.set_image(url="https://media.istockphoto.com/vectors/report-on-sheet-of-paper-vector-icon-flat-isolated-vector-id1223982866?k=6&m=1223982866&s=612x612&w=0&h=yHf0YOtEHSmY6Z9GKkJl63w9Jp-YwdRLHwFmI3iRqfE=")
        myEmbed.set_footer(text="Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        myEmbed.set_author(name="Prof XYZ")

        await general_channel.send(embed=myEmbed)
  

    await client.process_commands(message)



# run the client on the server
client.run('ODE1NTAyMzY4OTIwNTY3ODI4.YDtVxA.KMAeMSkAWn_s1r-AKCRCqeDww98')

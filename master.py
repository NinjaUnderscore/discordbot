import discord
""" Requires Discord.py """

import asyncio
""" Requires asyncio, which I think you also need for Discord.py? """

import time
""" Only used for time.sleep, and in how many seconds. Main problem is.. this stops the bot completely. """

""" Again, W.I.P, I think asyncio may have a wait function without stopping bot COMPLETELY. """

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------")     

@client.event   
async def on_message(message):
    if message.content.startswith("?ping"):
        pingpong = await client.send_message(message.channel, 'Pong!')
        time.sleep(2)
        await client.delete_message(message)
        await client.delete_message(pingpong)
        

    elif message.content.startswith("?greetings"):
        hai = await client.send_message(message.channel, 'Hello.')
        time.sleep(2)
        await client.delete_message(message)
        time.sleep(1)
        await client.delete_message(hai)


    elif message.content.startswith("?embed-t"):
        embed = discord.Embed(title="Tile", description="Desc",)
        embed.add_field(name="Fiel1", value="hi", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith("?gun"):
        embed = discord.Embed()
        gun = embed.set_image(url='https://i.imgur.com/0e8voVb.png')
        await client.delete_message(message)
        await client.send_message(message.channel, embed=gun)

    elif message.content.startswith("?thatsheresy"):
        embed = discord.Embed()
        thatsheresy = embed.set_image(url='http://i0.kym-cdn.com/photos/images/facebook/001/208/722/808.jpg')
        await client.delete_message(message)
        await client.send_message(message.channel, embed=thatsheresy)

    elif message.content.startswith("?itsays"):
        embed = discord.Embed()
        itsays = embed.set_image(url='http://i0.kym-cdn.com/photos/images/facebook/000/706/073/4cf.jpg')  
        await client.delete_message(message)
        await client.send_message(message.channel, embed=itsays)
    
    elif message.content.startswith("?notfine"):
        embed = discord.Embed()
        notfine = embed.set_image(url='https://cdn.discordapp.com/attachments/342216929982808066/347541935990374400/not_fine.gif')
        await client.delete_message(message)
        await client.send_message(message.channel, embed=notfine)

    elif message.content.startswith("?delet"):
        embed = discord.Embed()
        delet = embed.set_image(url='https://cdn.discordapp.com/attachments/342216929982808066/347541962305568769/Igotthis_258d31f8f47ec27e84df2276877e7180.jpg')
        """ Add colour later. """
        await client.send_message(message.channel, embed=delet)
        await client.delete_message(message)

    elif message.content.startswith("?help"):
        embed = discord.Embed(title="Commands:", description="Need commands? Here you go!   ",)
        embed.add_field(name="?ping", value="Ping pong!", inline=False)
        embed.add_field(name="?greetings", value="Say hello!", inline=False)
        embed.add_field(name="?thatsheresy", value="Thats heresy.", inline=False)
        embed.add_field(name="?itsays", value="That you are a heretic.", inline=False)
        embed.add_field(name="?delet", value="Delete this heresy.", inline=False)
        embed.add_field(name="?notfine", value="Why are we still here? Just to suffer?", inline=False)
        embed.add_field(name="?gun", value="GUN", inline=False)
        embed.add_field(name="?help", value="Brings you to this pm!", inline=False)
        await client.send_message(message.author, embed=embed)
        time.sleep(1)
        await client.delete_message(message)
        
        """ Very much still in progress, will be making more edits once I have more free-time and will to code. """
        """ This is where the client run token should be, but sadly I must keep that secret. :) """

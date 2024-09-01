
from libraries import *

from init import *

'''
@bot.event
async def on_message(m):
    username = str(ctx.author)
    content = str(ctx.context)
    channel = str(ctx.channel)

    #bot.process_commands(m)
'''

def datetimeInput(timestamp):
    pass

# -HTML 2024 09 01:02 10:22pm 10:30pm

@bot.command(aliases=['HTML', 'html'])
async def getHTML(ctx, *arg):
    username = str(ctx.author)
    content = str(ctx.message.content)
    channel = str(ctx.channel)

    if not (channel == '일상-역극' or channel == '메인-스토리-진행' or channel == "test1"):
        return

    timestamps = content.split()[1:]

    year = int(timestamps[0])
    month = int(timestamps[1])
    day1 = int(timestamps[2].split(':')[0])
    day2 = day1
    if len(timestamps[2].split(':')) > 1:
        day2 = int(timestamps[2].split(':')[1])

    time1 = timestamps[3]
    time2 = timestamps[4]
    
    print(year)
    print(month)
    print(day1)
    print(day2)
    print(time1)
    print(time2)


    

    pass

@bot.command(aliases=['오프', '끄기', 'exit'])
async def quit(ctx, *arg):
    #exit_event.set()
    #restore_timer.join()
    await bot.close()

@bot.command(aliases=["헤브", "헤부"])
async def geb_line(ctx):

    username = str(ctx.author)
    content = str(ctx.message.content)
    channel = str(ctx.channel)

    await ctx.message.delete()
    
    content = content[content.index(" ")+1:]

    await ctx.send(f"{Emote.GEB.value}")
    await ctx.send(f"{content}\n{blnk}")
    #await ctx.send(Cookbook1a)

@bot.command(aliases=['이상'])
async def yisang_line(ctx):

    username = str(ctx.author)
    content = str(ctx.message.content)
    channel = str(ctx.channel)
    await ctx.message.delete()
    
    content = content[content.index(" ")+1:]

    await ctx.send(f"{Emote.YISANG.value}")
    await ctx.send(f"{content}\n{blnk}")   


@bot.command(aliases=['이금'])
async def yigeum_line(ctx):

    username = str(ctx.author)
    content = str(ctx.message.content)
    channel = str(ctx.channel)
    await ctx.message.delete()
    
    content = content[content.index(" ")+1:]

    await ctx.send(f"{Emote.YIGEUM.value}")
    await ctx.send(f"{content}\n{blnk}")   


@bot.command(aliases=['베스'])
async def beth_line(ctx):

    username = str(ctx.author)
    content = str(ctx.message.content)
    channel = str(ctx.channel)
    await ctx.message.delete()
    
    content = content[content.index(" ")+1:]

    await ctx.send(f"{Emote.BETH.value}")
    await ctx.send(f"{content}\n{blnk}")   


@bot.command(aliases=['류드밀라', '류드'])
async def ludmila_line(ctx):

    username = str(ctx.author)
    content = str(ctx.message.content)
    channel = str(ctx.channel)
    await ctx.message.delete()
    
    content = content[content.index(" ")+1:]

    await ctx.send(f"{Emote.LUDMILA.value}")
    await ctx.send(f"{content}\n{blnk}")   


@bot.command(aliases=['몬태그'])
async def montag_line(ctx):

    username = str(ctx.author)
    content = str(ctx.message.content)
    channel = str(ctx.channel)
    await ctx.message.delete()
    
    content = content[content.index(" ")+1:]

    await ctx.send(f"{Emote.MONTAG.value}")
    await ctx.send(f"{content}\n{blnk}")   


@bot.command(aliases=['가환'])
async def gahwan_line(ctx):

    username = str(ctx.author)
    content = str(ctx.message.content)
    channel = str(ctx.channel)
    await ctx.message.delete()
    
    content = content[content.index(" ")+1:]

    await ctx.send(f"{Emote.GAHWAN.value}")
    await ctx.send(f"{content}\n{blnk}")   

@bot.command(aliases=['플뢰르'])
async def fleur_line(ctx):

    username = str(ctx.author)
    content = str(ctx.message.content)
    channel = str(ctx.channel)
    await ctx.message.delete()
    
    content = content[content.index(" ")+1:]

    await ctx.send(f"{Emote.FLEUR.value}")
    await ctx.send(f"{content}\n{blnk}")   


@bot.command(aliases=['홍루'])
async def honglu_line(ctx):
    username = str(ctx.author)
    content = str(ctx.message.content)
    channel = str(ctx.channel)
    await ctx.message.delete()
    
    content = content[content.index(" ")+1:]

    await ctx.send(f"{Emote.HONGLU.value}")
    await ctx.send(f"{content}\n{blnk}")   


@bot.command(aliases=['밍기뉴', '밍'])
async def ming_line(ctx):
    username = str(ctx.author)
    content = str(ctx.message.content)
    channel = str(ctx.channel)
    await ctx.message.delete()
    
    content = content[content.index(" ")+1:]

    await ctx.send(f"{Emote.MING.value}")
    await ctx.send(f"{content}\n{blnk}")   


@bot.command(aliases=['히스', '히클', '히스클리프'])
async def heath_line(ctx):
    username = str(ctx.author)
    content = str(ctx.message.content)
    channel = str(ctx.channel)
    await ctx.message.delete()
    
    content = content[content.index(" ")+1:]

    await ctx.send(f"{Emote.HEATH.value}")
    await ctx.send(f"{content}\n{blnk}")   

bot.run(TOKEN)

#boop beep

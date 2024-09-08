
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

@bot.command(aliases=['HTML', 'html'])
async def getHTML(ctx, *arg):
    username = str(ctx.author)
    content = str(ctx.message.content)
    channel = str(ctx.channel)

    if not (channel == '일상-역극' or channel == '메인-스토리-진행' or channel == "test1"):
        return

    # -HTML (idnum) (idnum)

    parsed = content.split()[1:]
    message1 = await ctx.fetch_message(int(parsed[0]))
    message2 = await ctx.fetch_message(int(parsed[1]))

    # start building string

    # alwyas include DIV_HEADER @ start
    # div starter -> div_profile_NAME(HTML[character].value) -> div_text_starter -> text -> div_ender

    HTML_doc = DIV_HEADER

    # get first character

    character = message1.content.split(":")[1].split("_")[0]

    #HTML_doc += HTML[character].value

    async for message in ctx.channel.history(limit=1000, before=message2.created_at, after=message1.created_at, oldest_first=True):

        # character emoji message - change character
        if(message.content.find('_main') != -1):
            print(message.content)
            character = message.content.split(":")[1].split("_")[0]
        
        # text message - push HTML code onto HTML_doc
        else:
            HTML_doc += DIV_STARTER + HTML[character].value + DIV_TEXT_STARTER + message.content + DIV_ENDER

    HTML_doc += DIV_STARTER + HTML[character].value + DIV_TEXT_STARTER + message2.content + DIV_ENDER

    f = open("discord_html_send.txt", "w")
    f.write(HTML_doc)
    f.close()

    nameoffile = datetime.now().strftime("%Y%m%d")
    nameoffile += "-htmloutput.txt"
    
    await ctx.send(file=discord.File(r"c:\Users\amapon\Desktop\SyndicateArcana\discord_html_send.txt", filename=nameoffile))


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

import discord 
from discord.ext import commands
import datetime
import os

tsbot = commands.Bot(command_prefix='헵자야 ')




@tsbot.event
async def on_member_join(member):
    ctx = member.guild.get_channel(853657788697542656)
    await ctx.send(f'어서오세요 {member.author.mention}!')



@tsbot.event
async def on_ready():
    print(f'{tsbot.user} login!')
    await tsbot.change_presence(activity=discord.Game("헵자야 도움말"))




@tsbot.command()
async def 도움말(ctx):
    embed=discord.Embed(title="명령어", description="", color=0xffc0cb)
    embed.add_field(name="헵자야 안녕", value="헵자가 인사를 해줘요", inline=False)
    embed.add_field(name="헵자야 내정보", value="헵자가 내정보를 알려줘요", inline=False)
    embed.add_field(name="헵자야 유튜브", value="헵자가 유튜브 링크를 알려줘요", inline=False)
    embed.add_field(name="헵자야 트위치", value="헵자가 트위치 링크를 알려줘요", inline=False)
    embed.add_field(name="헵자야 트위터", value="헵자가 트위터 링크를 알려줘요", inline=False)
    embed.add_field(name="헵자야 인스타", value="헵자가 인스타 링크를 알려줘요", inline=False)
    embed.set_footer(text='Quin#8782',
                    icon_url='https://cdn.discordapp.com/avatars/853622678073507840/a97a1df70aad805cab9e793324992ce4.webp?size=128')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/787611001390497832/787612375767187456/heavygiant.png?width=676&height=676")
    await ctx.send(embed=embed)


@tsbot.command()
async def 내정보(ctx):
    user = ctx.author
    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
    await ctx.send(f"""
{ctx.author.mention}님의 정보  
```cs
이름: {user}  
디스코드 가입일: {date.year}/{date.month}/{date.day}
```
        """)







@tsbot.command()
async def 내프사(ctx):
    user = ctx.author
    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
    await ctx.send(f"{user.avatar_url}")



@tsbot.command()
async def 생년월일(ctx):
    embed = discord.Embed(title="HEAVYgiant", description="HEAVYgiant#0217", color=0xffc0cb)
    embed.add_field(name="2005년", value="2월 17일", inline=False)
    embed.set_footer(text='Quin#8782',
                  icon_url='https://cdn.discordapp.com/avatars/853622678073507840/a97a1df70aad805cab9e793324992ce4.webp?size=128')
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/787611001390497832/787612375767187456/heavygiant.png?width=676&height=676")
    await ctx.send(embed=embed)





@tsbot.command()
async def 시간(ctx):
    await ctx.send(embed=discord.Embed(title="헵자 시계", timestamp=datetime.datetime.utcnow(), color=0xffc0cb))


@tsbot.command()
async def 안녕(ctx):
    await ctx.send('ㅎㅇㅎㅇ')

@tsbot.command()
async def 마인크래프트(ctx):
    await ctx.send('갓똥겜')

@tsbot.command()
async def 멍청이(ctx):
    await ctx.send('힝 나빠써 ㅠㅜ')

@tsbot.command()
async def 힝(ctx):
    await ctx.send('히ㅇ이이이이이이이이이이이이잉ㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠ')

@tsbot.command()
async def 귀여워(ctx):
    await ctx.send('뀨?')

@tsbot.command()
async def 헵자(ctx):
    await ctx.send('머요')

@tsbot.command()
async def 사랑해(ctx):
    await ctx.send('나듀 사량해 💕💕')

@tsbot.command()
async def 나이(ctx):
    await ctx.send('17')

@tsbot.command()
async def 생일(ctx):
    await ctx.send('2월 17일')

@tsbot.command()
async def 냥(ctx):
    await ctx.send('냥!')

@tsbot.command()
async def 크시(ctx):
    await ctx.send('쌉괴')

@tsbot.command()
async def 빌스(ctx):
    await ctx.send('빌스!!💕')






# url

@tsbot.command()
async def 디스코드(ctx):
    await ctx.reply('https://discord.com/invite/gUTAY9Cqbc')

@tsbot.command()
async def 인스타(ctx):
    await ctx.reply('https://instagram.com/heavygiant?igshid=1ewywjzmyfdwy')

@tsbot.command()
async def 유튜브(ctx):
    await ctx.reply('https://www.youtube.com/c/heavygiant')

@tsbot.command()
async def 트위터(ctx):
    await ctx.reply('https://twitter.com/heavygiant217')

@tsbot.command()
async def 트위치(ctx):
    await ctx.reply('https://www.twitch.tv/heavygiant217')



tsbot.run(os.environ['token'])

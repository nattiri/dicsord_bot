import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from asyncio import sleep


load_dotenv()

#トークン読み込み
TOKEN = os.environ['TOKEN']
CHANNEL_ID = int(os.environ['CHANNEL_ID'])

# client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Hello World!!!')


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def start(ctx, hour):
    #intは時間が入力される想定
    mokumoku_time = int(hour) * 60 * 60
    await ctx.send("もくもく開始！今日もがんばろう！")
    await sleep(mokumoku_time)
    await ctx.send(str(hour) + "時間経過。よくがんばった！")


bot.run(TOKEN)






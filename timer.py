import discord
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv()

#トークン読み込み
TOKEN = os.environ['TOKEN']
CHANNEL_ID = int(os.environ['CHANNEL_ID'])

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Hello')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '/hello':
        await message.channel.send('Hello World!')

    if message.content == '/start':
        #もくもく会の開始時に実行
        #2時間をカウントする
        mokumoku = client.get_channel(CHANNEL_ID)
        mokumoku_time = 60 * 60 * 2

        await mokumoku.send('もくもく開始！今日もがんばろう！')
        sleep(mokumoku_time)
        hour = mokumoku_time / 60 / 60
        await mokumoku.send(str(hour) + '時間経過。よくがんばった！')

client.run(TOKEN)






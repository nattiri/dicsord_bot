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
        mokumoku_time = 10

        await mokumoku.send('もくもく開始！今日もがんばろう！')
        for i in range(0,mokumoku_time):
            sleep(1)

        hour = mokumoku_time / 60 / 60
        await mokumoku.send(str(hour) + '時間経過。よくがんばった！')

client.run(TOKEN)






import discord
import random
import os, sys, codecs

client = discord.Client()

TOKEN = BOT_TOKEN

lirycdict1 = {}
lirycdict2 = {}
lirycdict3 = {}

#Login
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#New Member Join
@client.event
async def on_member_join(member):
    chid = ENTRANCE_CHANNEL_ID
    defchannel = member.server.get_channel(chid)
    msg = msg_edit(reply1, member.name)
    await client.send_message(defchannel, msg)

#Message Reply
@client.event
async def on_message(message):
    msg = ""
    if client.user != message.author:
        if message.content.startswith(":j "):
            if "おはよ" in message.content or "morning" in message.content:
                msg = msg_edit(reply2,message.author.name)
            else:
                msg = msg_edit(reply3,message.author.name)

    # メッセージが送られてきたチャンネルへメッセージを送ります
    if msg != "":
        await client.send_message(message.channel, msg)

# Message File Read
def readDic(filename):
    field = {}
    file = codecs.open(filename, "r","utf_8")
    next(file)
    for row in file:
        row = row.rstrip("\r\n")
        result= row.split(",")
        field[result[0]] = result[1]

    return field

# Message Edit
def msg_edit(msgdict, name):
    idx = 0
    num = random.randint(1,len(msgdict))
    for i in msgdict:
        idx += 1
        if idx == num:
            return msgdict.get(i).replace("PRODUCER_NAME", name)

mypath = os.path.dirname(os.path.abspath(sys.argv[0]))
reply1 = readDic(mypath + "\_replydict/_reply1.txt")
reply2 = readDic(mypath + "\_replydict/_reply2.txt")
reply3 = readDic(mypath + "\_replydict/_reply3.txt")

client.run(TOKEN)

# インストールした discord.py を読み込む
import discord
import search_book
import kaiseki #解決
from datetime import datetime
#import yahoo_search
from discord.ext import commands
from discord.ext import tasks
import os
import traceback

# 自分のBotのアクセストークンに置き換えてください
TOKEN = os.environ['DISCORD_BOT_TOKEN']
server_admin = "koni"
# 接続に必要なオブジェクトを生成
bot = commands.Bot(command_prefix='/')
CHANNEL_ID = 677051725412171776 # 任意のチャンネルID(int)
command = 0
menber_authority = []
maybe_alarm = []
alarm_list = []
#channel = client.get_channel(CHANNEL_ID)

# 起動時に動作する処理
@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    search_book.setup_list()
    #yahoo_search.setup()
    channel = bot.get_channel(CHANNEL_ID)
    config = 0
    menber_list = [member.display_name for member in bot.get_all_members()]   
    menber_list.remove("koni_book")
    for i in menber_list:
        menber_authority.append([i,0,0])
    await channel.send("ログインしました")
    loop.start()

@tasks.loop(seconds=60)
async def loop():
    if alarm_list != []:
        nowtime = datetime.now().strftime('%H:%M')
        if nowtime == '01:':
            nowdate = datetime.now().strftime('%d')
            for i in alarm_list:
                if i[2] == nowdate:
                    user = bot.get_user(i[0])
                    print(type(i[1]))
                    await user.send("本日は"+i[1]+"の発売日です")

# メッセージ受信時に動作する処理
@bot.event
async def on_message(message):
    global command
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    maybe = 0
    for i in maybe_alarm:
        if message.author.id == i[0]:
            maybe = 1
    group = False
    try:
        group = message.author.guild_permissions.administrator
    except:
        pass
    if group:
        if  message.author.name == server_admin:
            if message.content == "/end":
                #await bot.logout()
                await message.channel.send("そのコマンドは禁止されています")
            elif command != 0:
                hitflag = 0
                for i in menber_authority:
                    if message.content in i:
                        if command == 1:
                            i[1] = 0
                            await message.channel.send(i[0]+"の検索条件に成年向けを削除しました")
                        elif command == 2:
                            i[1] = 1
                            await message.channel.send(i[0]+"の検索条件に成年向けを追加しました")
                        elif command == 3:
                            i[2] = 0
                            await message.channel.send(i[0]+"の検索結果をパブリックにしました")
                        elif command == 4:
                            i[2] = 1
                            await message.channel.send(i[0]+"の検索結果をプライベートにしました")
                        command = 0
                        hitflag = 1
                if hitflag == 0:
                    await message.channel.send("ユーザ名が間違えている可能性があります")
            elif message.content == "/lock":
                command = 1
                await message.channel.send("誰の検索条件に成年向けを削除しますか？")
            elif message.content == "/unlock":
                command = 2
                await message.channel.send("誰の検索条件に成年向けを追加しますか？")
            elif message.content == "/public":
                command = 3
                await message.channel.send("誰の検索結果をパブリックにしますか？")
            elif message.content == "/private":
                command = 4
                await message.channel.send("誰の検索結果をプライベートにしますか？")
            elif message.content == "/alarm":
                await message.channel.send(alarm_list)
    
    elif maybe == 1:
        for i,book in enumerate(maybe_alarm):
            if message.author.id == book[0]:
                if message.content == "はい":
                    alarm_list.append(book)
                maybe_alarm.pop(0)
    
    else:
        await message.channel.send("検索中")
        book_data = search_book.search(kaiseki.analysis(message.content))
        await message.channel.send("検索終了")
        adultflag = 0
        minorflag = 0
        maybeflag = 0
        message_status = [i for i in menber_authority if message.author.name in i]
        message_status = message_status[0]
        if book_data:
            for book in book_data:
                if len(book) > 3:
                    book.pop(0)
                if "（成）" not in book[0] or message_status[1] == 1:
                    await message.channel.send(book[0])
                    await message.channel.send("著者:"+book[2])
                    await message.channel.send(book[1]+"日発売です")
                    minorflag = 1     
                    if len(book_data) == 1:
                        """
                        try:
                            #await message.channel.send("検索中")
                            await message.channel.send(yahoo_search.search(book[0]))
                        except:
                            pass
                        
                        if message_status[2] != 1:
                            channel = bot.get_channel(CHANNEL_ID)
                            await channel.send(message.author.name+"が'"+book[0]+"'を欲しがっています")
                        """
                        for l in alarm_list:
                            if len(l) < 4:
                                maybeflag = 2
                        if maybeflag == 0:
                            book.insert(0,message.author.id)
                            maybe_alarm.append(book)                        
                            maybeflag = 1
                    await message.channel.send("------------------------------------------------------------")
                else:
                    adultflag=1
            if minorflag == 1:
                await message.channel.send("以上です")
            if adultflag == 1:
                await message.channel.send("あなたに不適切と思われる書籍が含まれていたので表示しませんでした")
            if maybeflag == 1:
                await message.channel.send("この本の発売日に連絡しますか？　はい/いいえ")
            if maybeflag == 2:
                await message.channel.send("この本はすでに登録済みです")
        else:
            await message.channel.send("ありません")
    
    
# Botの起動とDiscordサーバーへの接続
bot.run(TOKEN)

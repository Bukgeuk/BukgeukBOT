import discord
import asyncio
import datetime
import os
import string
import random
import sys
import time
from discord.ext import commands
prefix = "&"
bot = commands.Bot(command_prefix=prefix)

client = discord.Client()
access_password = "bukgeukbot8999"
developer_id = "390637401195675648"
update_is = 0
f = open('update.txt', 'w+t')
f.write(str(update_is))
f.close()

@client.event
async def on_ready():
    print('Logged in as', client.user)
    print('( name =', client.user.name, ', id =', client.user.id, ')')

    activity = discord.Activity(name='Messages | &b help', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)


@client.event
async def on_reaction_add(reaction, user):
    a = reaction.message.content.split("\n")
    b = a[0][10:]
    c = b.split(" ")
    servername = c[0]
    noticeid = c[1]
    f = open(str(noticeid) + '-' + servername + '.txt', 'a+t')
    f.write(str(user.id) + ',')
    f.close()
    file = str(noticeid) + '-' + servername + '.txt'
    if os.path.isfile(file):
        f = open(str(noticeid) + '-' + servername + '.txt', 'rt')
        s = f.read()
        print(s)
        memberlist = s[:-1].split(",")
        f.close()
        memberlist = list(set(memberlist))
        print(memberlist)
        f = open(str(noticeid) + '-' + servername + '.txt', 'w+t')
        f.write(",".join(memberlist) + ",")
        f.close()
    return



@client.event
async def on_message(message):
    if message.content.startswith('&b'):
        f = open('update.txt', 'rt')
        update_is = f.read()
        f.close()
        if int(update_is) == 1 and not('&b finishupdate ' in message.content):
            await message.channel.send('업데이트 중인 관계로 명령어를 사용 하실 수 없습니다.')
            return

        if message.content == '&b help':
            now = datetime.datetime.now()

            #embed1 설정
            embed1 = discord.Embed(title="소개", description="기획 : Bukgeuk\n개발 : Bukgeuk\n테스트 : Bukgeuk\n버전 : v3.3\nBukgeukBOT의 저작권은 개발자에게 있습니다.", color=0xf9dddc)
            if now.hour > 12:
                embed1.set_footer(text = str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + "오후 " + str(now.hour-12) + "시 " + str(now.minute) + "분 " + str(now.second) +  "초")
            else:
                embed1.set_footer(text = str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + "오전 " + str(now.hour) + "시 " + str(now.minute) + "분 " + str(now.second) +  "초")

            #embed2 설정
            text = "&b help : 도움말\n&b addmember [서버 이름] [@유저] : 멤버 추가\n&b viewmember [서버 이름] : 멤버 출력\n&b notice [서버 이름] [공지 이름] [내용] : 공지 추가\n&b noticesend [서버 이름] [공지 이름] : 공지 확인 안한 멤버에게 확인 메시지 전송\n&b noticedelete [서버 이름] [공지 이름] : 공지 삭제\n&b noticenow [서버 이름] : 진행중인 공지 출력\n&b resetmember [서버 이름] : 멤버 초기화\n&b deletemember [서버 이름] [@유저] : 멤버 삭제\n"
            text += "&b viewreactionuser [서버 이름] [공지 이름] : 리액션한 유저 출력\n&b addreactionuser [서버 이름] [공지 이름] [@유저] : 리액션 목록에 멤버 추가\n&b deletereactionuser [서버 이름] [공지 이름] [@유저] : 리액션 목록에서 멤버 삭제\n&b resetreactionuser [서버 이름] [공지 이름] : 리액션 목록 초기화\n"
            text += "&b dmsend : 개인메시지로 메시지 전송\n&b random [최소값] [최대값] : 랜덤으로 범위 내의 숫자 출력\n&b startupdate [#채널] : 봇 업데이트 시작 공지\n&b finishupdate [#채널] : 봇 업데이트 완료 공지\n&b shutdown : BukgeukBOT 강제 종료"
            embed2 = discord.Embed(title="명령어", description=text, color=0xf9dddc)
            if now.hour > 12:
                embed2.set_footer(text = str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + "오후 " + str(now.hour-12) + "시 " + str(now.minute) + "분 " + str(now.second) +  "초")
            else:
                embed2.set_footer(text = str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + "오전 " + str(now.hour) + "시 " + str(now.minute) + "분 " + str(now.second) +  "초")

            #embed3 설정
            embed3 = discord.Embed(title="주의사항", description="항목에 공백이 있으면 오류가 발생합니다\nnotice 명령어를 사용할 때 '[내용]' 항목은 한 줄 내려서 입력해 주세요\nresetreactionuser 명령어를 사용하시면 공지를 작성한 멤버도 리액션 목록에서 삭제됩니다.", color=0xf9dddc)
            if now.hour > 12:
                embed3.set_footer(text = str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + "오후 " + str(now.hour-12) + "시 " + str(now.minute) + "분 " + str(now.second) +  "초")
            else:
                embed3.set_footer(text = str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + "오전 " + str(now.hour) + "시 " + str(now.minute) + "분 " + str(now.second) +  "초")
            #embed 출력
            await message.author.send('BukgeukBOT 도움말 입니다.', embed=embed1)
            await message.author.send('', embed=embed2)
            await message.author.send('', embed=embed3)
            await message.channel.send('개인 메시지로 도움말이 전송되었습니다.')
            return



        elif message.content == '&b dmsend':
            await message.channel.send('전송할 메시지를 입력해 주세요')
            try:
                def check(m):
                    return m.author == message.author and m.channel == message.channel
                msg = await client.wait_for('message', check=check, timeout=15.0)
            except asyncio.TimeoutError:
                await message.channel.send('시간이 초과되었습니다.')
                return
            else:
                await message.author.send(msg.content)
                await message.channel.send('개인메시지로 전송되었습니다')
                return



        elif message.content.startswith('&b addmember '):
            if(0 == message.author.guild_permissions.administrator):
                await message.channel.send('이런, 권한이 부족하네요...')
                return
            after=message.content[13:]
            members = after.split(" ")
            servername = members[0]
            f = open('memberlist-' + servername + '.txt', 'a+t')
            f.close()
            f = open('memberlist-' + servername + '.txt', 'rt')
            membertext = f.read()
            f.close()
            f = open('memberlist-' + servername + '.txt', 'a+t')
            if '<@' in members[1]:
                nm = members[1][2:-1]
            else:
                nm = members[1]
            if nm in membertext:
                await message.channel.send('이미 추가 되어 있는 멤버입니다.')
                return
            f.write(nm + ',')
            f.close()
            await message.channel.send('"' + str(client.get_user(int(nm))) + '" 멤버가 "' + servername + '" 서버에 정상적으로 추가되었습니다.')
            return



        elif message.content.startswith('&b viewmember '):
            if(0 == message.author.guild_permissions.administrator):
                await message.channel.send('이런, 권한이 부족하네요...')
                return
            servername = message.content[14:]
            file = 'memberlist-' + servername + '.txt'
            if os.path.isfile(file):
                f = open('memberlist-' + servername + '.txt', 'rt')
                s = f.read()
                memberlist = s.split(",")
                f.close()
                members = ""
                i = 0
                for m in memberlist:
                    if i == len(memberlist) - 1:
                        break
                    members += str(client.get_user(int(m))) + '\n'
                    i += 1

                await message.channel.send('"' + servername + '" 서버의 멤버 목록 입니다.\n' + '```\n' + members + '\n```')
                return
            else:
                await message.channel.send('"' + servername + '" 서버의 멤버 파일이 없습니다')
                return




        elif message.content.startswith('&b notice '):
            if(0 == message.author.guild_permissions.administrator):
                await message.channel.send('이런, 권한이 부족하네요...')
                return
            after = message.content.split("\n")
            abc = after[0][10:]
            last = abc.split(" ")
            servername = last[0]
            noticeid = last[1]
            file = noticeid + '-' + servername + '.txt'
            if os.path.isfile(file):
                await message.channel.send('이미 진행중인 공지입니다.')
            else:
                f = open(str(noticeid) + '-' + servername + '.txt', 'a+t')
                f.write(str(message.author.id) + ',')
                f.close()
                delmsg = await message.channel.send('"' + str(noticeid) + '" 공지가 "' + servername + '" 서버에 정상적으로 추가 되었습니다.')
                await asyncio.sleep(3)
                await delmsg.delete()
                return



        elif message.content.startswith('&b noticesend '):
            if(0 == message.author.guild_permissions.administrator):
                await message.channel.send('이런, 권한이 부족하네요...')
                return
            a = message.content[14:]
            b = a.split(" ")
            servername = b[0]
            noticeid = b[1]
            f = open('memberlist-' + servername + '.txt', 'rt')
            s = f.read()
            s = s[:-1]
            members = s.split(",")
            f.close()
            f = open(str(noticeid) + '-' + servername + '.txt', 'rt')
            s = f.read()
            s = s[:-1]
            reactionusers = s.split(",")
            f.close()
            for m in members:
                run = 0
                for ru in reactionusers:
                    if run == len(reactionusers) - 1:
                        if m == ru:
                            break
                        else:
                            await client.get_user(int(m)).send('"' + servername + '" 서버의 "' + noticeid + '" 공지를 읽어 주시기 바랍니다.')
                            await message.channel.send('"' + str(client.get_user(int(m))) + '" 님에게 전송을 완료하였습니다.')
                            break
                    else:
                        if m == ru:
                            break
                        else:
                            run = run + 1

            os.remove(str(noticeid) + '-' + servername + '.txt')
            await message.channel.send('전송을 완료하였습니다.')
            return



        elif message.content.startswith('&b noticedelete '):
            if(0 == message.author.guild_permissions.administrator):
                await message.channel.send('이런, 권한이 부족하네요...')
                return
            a = message.content[16:]
            b = a.split(" ")
            servername = b[0]
            noticeid = b[1]
            file = noticeid + '-' + servername + '.txt'
            if os.path.isfile(file):
                os.remove(file)
                await message.channel.send('공지 파일 삭제에 성공했습니다!\n공지는 직접 삭제해 주세요')
                return
            else:
                await message.channel.send('이런, 일치하는 공지가 없네요...')
                return



        elif message.content.startswith('&b noticenow '):
            if(0 == message.author.guild_permissions.administrator):
                await message.channel.send('이런, 권한이 부족하네요...')
                return
            servername = message.content[13:]
            path = "./"
            file_list = os.listdir(path)
            notices = ""
            for x in file_list:
                if 'memberlist' not in x:
                    if servername in x:
                        a = x[:-4]
                        b = a.split("-")
                        notices += b[0] + '\n'
            await message.channel.send('"' + servername + '" 서버에서 진행중인 공지 입니다.\n' + '```\n' + notices + '\n```')
            return



        elif message.content.startswith('&b resetmember '):
            if(0 == message.author.guild_permissions.administrator):
                await message.channel.send('이런, 권한이 부족하네요...')
                return
            servername = message.content[15:]
            file = 'memberlist-' + servername + '.txt'
            if os.path.isfile(file):
                os.remove(file)
                await message.channel.send('멤버 파일 삭제에 성공했습니다!')
                return
            else:
                await message.channel.send('이런, 일치하는 파일이 없네요...')
                return



        elif message.content.startswith('&b deletemember '):
            if(0 == message.author.guild_permissions.administrator):
                await message.channel.send('이런, 권한이 부족하네요...')
                return
            a = message.content[16:]
            b = a.split(" ")
            servername = b[0]
            tm = b[1]
            if '<@' in tm:
                nm = tm[2:-1]
            else:
                nm = tm

            file = 'memberlist-' + servername + '.txt'
            if os.path.isfile(file):
                f = open('memberlist-' + servername + '.txt', 'rt')
                s = f.read()
                members = s.split(",")
                f.close()
                try:
                    members.remove(nm)
                    f = open('memberlist-' + servername + '.txt', 'wt')
                    f.write(",".join(members))
                    f.close()
                    await message.channel.send('"' + str(client.get_user(int(nm))) + '" 멤버를 삭제했습니다.')
                except ValueError:
                    await message.channel.send('"' + str(client.get_user(int(nm))) + '" 멤버가 없습니다.')
                    return
            else:
                await message.channel.send('멤버 파일이 없습니다.')
                return


        elif message.content.startswith('&b random '):
            a = message.content[10:]
            b = a.split(" ")
            min = b[0]
            max = b[1]
            await message.channel.send('이번에 나온 숫자는 "' + str(random.randrange(int(min), int(max) + 1)) + '" 입니다!')
            return



        elif message.content.startswith('&b viewreactionuser '):
            a = message.content[20:]
            b = a.split(" ")
            servername = b[0]
            noticeid = b[1]
            file = str(noticeid) + '-' + servername + '.txt'

            if os.path.isfile(file):
                f = open(str(noticeid) + '-' + servername + '.txt', 'rt')
                s = f.read()
                memberlist = s[:-1].split(",")
                f.close()
                memberlist = list(set(memberlist))
                members = ""
                i = 0
                for m in memberlist:
                    if i == len(memberlist):
                        break
                    members += str(client.get_user(int(m))) + "\n"
                    i += 1

                await message.channel.send('"' + servername + '" 서버의 "' + noticeid + '" 공지에 리액션한 유저들 입니다.\n' + '```\n' + members + '\n```')
                return
            else:
                await message.channel.send('이런, 일치하는 공지가 없네요...')
                return



        elif message.content.startswith('&b addreactionuser '):
            a = message.content[19:]
            b = a.split(" ")
            servername = b[0]
            noticeid = b[1]
            c = b[2]
            user = c[2:-1]
            file = str(noticeid) + '-' + servername + '.txt'
            if os.path.isfile(file):
                f = open(str(noticeid) + '-' + servername + '.txt', 'rt')
                s = f.read()
                users = s[:-1].split(",")
                for u in users:
                    if u == user:
                        await message.channel.send('이미 추가되어 있는 멤버예요!')
                        return

                f = open(str(noticeid) + '-' + servername + '.txt', 'a+t')
                f.write(user + ",")
                f.close()
                await message.channel.send('"' + str(client.get_user(int(user))) + '" 멤버가 "' + servername + '" 서버의 "' + noticeid + '" 공지에 성공적으로 추가되었습니다.')
                return
            else:
                await message.channel.send('이런, 일치하는 공지가 없네요...')
                return



        elif message.content.startswith('&b deletereactionuser '):
            a = message.content[22:]
            b = a.split(" ")
            servername = b[0]
            print(servername)
            noticeid = b[1]
            print(noticeid)
            c = b[2]
            user = c[2:-1]
            print(user)
            file = str(noticeid) + '-' + servername + '.txt'
            print(file)
            if os.path.isfile(file):
                f = open(str(noticeid) + '-' + servername + '.txt', 'rt')
                s = f.read()
                users = s[:-1].split(",")
                users = list(set(users))
                try:
                    users.remove(user)
                except ValueError:
                    await message.channel.send('"' + str(client.get_user(int(user))) + '" 멤버는 "' + servername + '" 서버의 "' + noticeid + '" 공지에 추가 되어 있지 않아요!')
                    return

                f.close()
                f = open(str(noticeid) + '-' + servername + '.txt', 'wt')
                f.write(",".join(users) + ",")
                f.close()
                await message.channel.send('"' + str(client.get_user(int(user))) + '" 멤버가 "' + servername + '" 서버의 "' + noticeid + '" 공지의 reactionuser 목록에서 삭제되었습니다.')
                return

            else:
                await message.channel.send('이런, 일치하는 공지가 없네요...')
                return



        elif message.content.startswith('&b resetreactionuser '):
            a = message.content[21:]
            b = a.split(" ")
            servername = b[0]
            noticeid = b[1]
            file = str(noticeid) + '-' + servername + '.txt'
            if os.path.isfile(file):
                os.remove(file)
                await message.channel.send('"' + servername + '" 서버의 "' + noticeid + '" 공지의 reactionuser 파일을 성공적으로 초기화 하였습니다.')
                return
            else:
                await message.channel.send('해당하는 공지의 reactionuser 파일이 없습니다만...')
                return



        elif message.content.startswith('&b shutdown'):
            await message.channel.send('{ STARTING SHUTDOWN }')
            await message.channel.send('Shutdown Progress : 0%')
            if str(message.author.id) == developer_id:
                await message.channel.send('Shutdown Progress : 40%')
                await message.author.send('Enter password to access Developer Commands.')
                try:
                    def check(m):
                        return m.author == message.author
                    await message.channel.send('Shutdown Progress : 80%')
                    msg = await client.wait_for('message', check=check, timeout=15.0)
                except asyncio.TimeoutError:
                    await message.channel.send('Failed to access shutdown that is Developer command : TIMEOUT')
                    return
                else:
                    if msg.content == access_password:
                        await message.channel.send('Succeeded to access shutdown that is Developer command')
                        await message.channel.send('Shutdown Progress : 100%')
                        await message.channel.send('{ FINISHED SHUTDOWN }')
                        sys.exit()
                    else:
                        await message.channel.send('Failed to access shutdown that is Developer command : INVALID PASSWORD')
                        return

            else:
                await message.channel.send('Failed to access shutdown that is Developer command : PERMISSION ERROR')
                return

        elif message.content.startswith('&b startupdate '):
            if str(message.author.id) == developer_id:
                await message.author.send('Enter password to access Developer Commands.')
                try:
                    def check(m):
                        return m.author == message.author
                    msg = await client.wait_for('message', check=check, timeout=15.0)
                except asyncio.TimeoutError:
                    await message.author.send('Failed to access shutdown that is Developer command : TIMEOUT')
                    return
                else:
                    if msg.content == access_password:
                        await message.author.send('Succeeded to access shutdown that is Developer command')
                        a = message.content[15:]
                        b = a[2:-1]
                        ch = client.get_channel(int(b))
                        await ch.send('@everyone @BukgeukBOT#8999 업데이트를 시작합니다.')
                        update_is = 1
                        f = open('update.txt', 'w+t')
                        f.write(str(update_is))
                        f.close()
                        return
                    else:
                        await message.author.send('Failed to access shutdown that is Developer command : INVALID PASSWORD')
                        return

            else:
                await message.channel.send('Failed to access shutdown that is Developer command : PERMISSION ERROR')
                return

        elif message.content.startswith('&b finishupdate '):
            if str(message.author.id) == developer_id:
                await message.author.send('Enter password to access Developer Commands.')
                try:
                    def check(m):
                        return m.author == message.author
                    msg = await client.wait_for('message', check=check, timeout=15.0)
                except asyncio.TimeoutError:
                    await message.author.send('Failed to access shutdown that is Developer command : TIMEOUT')
                    return
                else:
                    if msg.content == access_password:
                        await message.author.send('Succeeded to access shutdown that is Developer command')
                        a = message.content[16:]
                        b = a[2:-1]
                        ch = client.get_channel(int(b))
                        await ch.send('@everyone @BukgeukBOT#8999 업데이트가 완료되었습니다.')
                        update_is = 0
                        f = open('update.txt', 'w+t')
                        f.write(str(update_is))
                        f.close()
                        return
                    else:
                        await message.author.send('Failed to access shutdown that is Developer command : INVALID PASSWORD')
                        return

            else:
                await message.channel.send('Failed to access shutdown that is Developer command : PERMISSION ERROR')
                return

        else:
            await message.channel.send('알 수 없는 구문이네요...')
            return
    else:
        return


access_token = "NTY5NDY3Mjk0Mzc2Mzk0NzYy.XLxD0g.48usJxdt3w_vbYVOk0ZDsL2x1_w"
client.run(access_token)

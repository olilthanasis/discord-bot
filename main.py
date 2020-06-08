import discord
import requests
from bs4 import BeautifulSoup
import random
from pathlib import Path
import time
import lyricsgenius
players = ""
headers = ""


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
            global headers
            if message.author.id == self.user.id:
                return

            if message.content.startswith('!status'):
                if message.author.id == (484100857995198472):
                    await message.channel.send("με ποτσεπηδες δεν μιλαω")
                else:
                    url = "https://psolil.aternos.me/"

                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
                    try:
                        page = requests.get(url, headers=headers)
                        soup = BeautifulSoup(page.content, 'html.parser')
                        server_status = soup.find(attrs={"status-label offline"}).get_text()
                        server_status = server_status.strip()
                        await message.channel.send("the server is " + server_status)
                    except AttributeError:
                        page = requests.get(url, headers=headers)
                        time.sleep
                        soup = BeautifulSoup(page.content, 'html.parser')
                        server_status = soup.find(attrs={"status-label online"}).get_text()
                        server_status = server_status.strip()
                        players = soup.find(attrs={"info-label"}).get_text()
                        players = players[:-3]
                        players = int(players)

                        if players == 0:
                            await message.channel.send("the server is " + server_status + " but no one is playing")
                        elif players == 1:

                            num = 0
                            real_final = ""
                            page = requests.get(url, headers=headers)
                            soup = BeautifulSoup(page.content, 'html.parser')
                            alt = soup.find("div", attrs="row no-bottom-padding")
                            alt = str(alt.find_all("img", title=True))
                            alt = alt.split(",")
                            for i in alt:
                                i = i.split()
                                i = i[1]
                                i = i[5:-1]
                                if num != 0:
                                    real_final = real_final + ", " + i
                                else:
                                    real_final = real_final + i
                                num = num + 1
                            players = str(players)

                            await message.channel.send("the server is " + server_status + " and " + players +
                                                       ' person is playing at the moment' + "(" + real_final + ")")
                        else:
                            players = str(players)
                            num = 0
                            real_final = ""
                            page = requests.get(url, headers=headers)
                            soup = BeautifulSoup(page.content, 'html.parser')
                            alt = soup.find("div", attrs="row no-bottom-padding")
                            alt = str(alt.find_all("img", title=True))
                            alt = alt.split(",")
                            for i in alt:
                                i = i.split()
                                i = i[1]
                                i = i[5:-1]
                                if num != 0:
                                    real_final = real_final + ", " + i
                                else:
                                    real_final = real_final + i
                                num = num + 1

                            await message.channel.send("the server is "+server_status+ " and " + players +
                                                       ' people are playing at the moment'+"("+real_final+")")

            if message.content.startswith('!subscribers'):
                if message.author.id == (484100857995198472):
                    await message.channel.send("με ποτσεπηδες δεν μιλαω")
                else:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
                    url2 = "https://socialblade.com/youtube/channel/UC9m5vXVCb0gYd_Rpgc6o8Mw"
                    page = requests.get(url2, headers=headers)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    subs = soup.find(id="youtube-stats-header-subs").get_text()
                    await message.channel.send("lil's channel currently has " + subs+" subscribers")
            if message.content.startswith('!spam'):
                if message.author.id == (484100857995198472):
                    await message.channel.send("με ποτσεπηδες δεν μιλαω")
                else:
                    text = message.content
                    target = text[6:]
                    num = text[-3:]
                    num = int(num)
                    print(text)
                    for i in range(0,num):
                        await message.channel.send(target)
            if message.content.startswith('!version'):
                if message.author.id == (484100857995198472):
                    await message.channel.send("με ποτσεπηδες δεν μιλαω")
                else:
                    url = "https://psolil.aternos.me/"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
                    page = requests.get(url, headers=headers)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    server_version = soup.find(attrs={"info"}).get_text()
                    server_version = server_version.strip()
                    await message.channel.send("the server is running on" + server_version[23:])
            if message.content.startswith('!fuck'):
                if message.author.id == (484100857995198472):
                    await message.channel.send("με ποτσεπηδες δεν μιλαω")
                else:
                    await message.channel.send("oh snap! "+str(message.author)+" fucked "+str(message.content[6:])+"'s "+"mother. How will he ever recover?")
            if message.content.startswith('!lilfact'):
                if message.author.id == (484100857995198472):
                    await message.channel.send("με ποτσεπηδες δεν μιλαω")
                else:
                    lil_facts = [
                        "ο λιλ θανασης ειναι ο πιο καλος ραπερ στον κοσμο οπως αποδείχθηκε απο την cambridge analytica σε ερευνα του 2019 "
                        ,
                        "ο λιλ θανασης εχει γαμησει πανω απο 5000 μανες και 20000 θειες στα  λιγα χρονια της ζωης του. Συμφωνα με προσφατες στατιστικες αναλυσεις ο συνολικος αριθμος αυτος θα φτασει τις 500 χιλιαδες πριν το 2030",
                        "ο λιλ θανασης ειναι ο ικανοτερος προγραμματιστης της προσφατης ιστοριας και ο κωδικας του εξεταζεται καθημερινα απο χιλιαδες φαν και αλλους επαγγελματιες στον χωρο",
                        "ο λιλ θανασης εγραψε την παλαια και την καινη διαθηκη σε ηλικια μονο 12 ετων  ",
                        "ο λιλ απλως γαμαει. Τελεία",
                        "Ο Θανάσης σε μικρή ηλικία έπεσε με το κεφάλι από την κούνια",
                        "το πρότυπο του σε μικρή ηλικία ήταν ο Ζαμπρας και ο 2J. Το χιουμορ τους τον επηρεασε εμφανως",
                        " ο Θανάσης είναι καραφλος και έχει μακρυά μαλλιά για να μην φαίνεται",
                        "ο Θανάσης είμαι ο χαμένος γιος του Ανδρέα Παπανδρέου",
                        "ο Θανάσης είναι εγγονός του Παπακαλιάτη",

                        ]

                    await message.channel.send(random.choice(lil_facts))


            if message.content.startswith("!order"):
                if message.author.id == (484100857995198472):
                    await message.channel.send("με ποτσεπηδες δεν μιλαω")
                else:
                    print("order")
                    text = message.content[7:]
                    print(text)
                    words = text.split()
                    print(words)
                    order_client = message.author
                    user1 = str(words[0:1])
                    user = client.get_user(user1)
                    order_item = words[1:2]
                    order_price = words[2:3]
                    print(user)
                    print(order_item)
                    print(order_client)
                    print(order_price)
                    await message.channel.send("Order placed!")
                    await message.author.send('Order placed!')

                    # user = client.get_user(381870129706958858)
                    await message.user(order_client+"ordered"+order_item+"for the price of"+order_price)

                    #await user.send(order_client+"ordered"+order_item+"for the price of"+order_price)
            if message.content.startswith("!lilsong"):
                if message.author.id == (484100857995198472):
                    await message.channel.send("με ποτσεπηδες δεν μιλαω")
                else:
                    song_request = message.content[9:]
                    await message.channel.send(file=discord.File(str(Path("C:/Users/mitth/PycharmProjects/skroutz/")) + song_request+".mp3"))
            if message.content.startswith('!ip'):
                if message.author.id == (484100857995198472):
                    await message.channel.send("με ποτσεπηδες δεν μιλαω")
                else:
                    await message.channel.send("psolil.aternos.me")

            if message.content.startswith("!help"):
                await message.channel.send(("```commands:\n'!status'\n'!subscribers'\n'!spam'(!spam @target xxx<---(amount of messages))\n'!version'\n")+(r"'!lilsong'(!lilsong\(song name))")+("\n'!lyrics'(!lyrics (song name))")+("\n'!ip'\nsource code:https://gist.github.com/olilthanasis/e7f400b8cf4675351723481abd753663```"))
            if message.content.startswith("!lyrics"):
                genius = lyricsgenius.Genius("s-RGdLPs5u-tSJgHnMDel6n7LORSVWsCezBENBsxW5XhiIbxFFxGze5aFnRvibq_")
                req = message.content[8:]
                print(req)
                song = genius.search_song(req)
                string = song.lyrics
                for chunk in [string[i:i + 1900] for i in range(0, len(string), 2000)]:
                    await message.channel.send("```"+chunk+"```")
            if message.content.startswith('!corona'):
                url = "https://www.worldometers.info/coronavirus/"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
                page = requests.get(url, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                main = (soup.find(attrs={"maincounter-number"}).get_text()).strip()
                await message.channel.send("Total Covid-19 Cases: " + main)
            if message.content.startswith('!owoifier'):
                full_text = message.content[10:]
                a = list(full_text)
                ret_val = ""
                for i in a:
                    if i =="l" or i == "r":
                        ret_val+="w"
                    elif i =="L" or i == "R":
                        ret_val+="W"
                    elif i!= "l" or i != "r" or i !="L" or i != "R":
                        ret_val+=i
                await message.channel.send(ret_val)
            if "@everyone" in message.content:
                await message.channel.send('σκασε')

client = MyClient()
client.run('********************************************')

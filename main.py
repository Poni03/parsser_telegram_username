from telethon.sync import TelegramClient
from telethon import functions, types

import telethon
import datetime
import time
import config

client = TelegramClient(config.phone, config.api_id, config.api_hash)
client.start()
limit, cur_id = 100, 0
usernames = set()
names_canals = [] # here need input lists telegram names canale "@context_1"
client.connect()

for i in names_canals:
    count = 0
    posts = client.get_messages(i, limit=2000)
    post_ids = []
    for post in posts:
        post_ids.append(post.id)


    for idd in post_ids:

        try:
            for message in client.iter_messages(i, reply_to=idd, reverse=True):

                if isinstance(message.sender, types.User):
                    if message.sender.username not in usernames:

                        usernames.add(message.sender.username)
                        print(message.sender.username)

                        with open(f"zak/{i}.txt", "a", encoding="utf-8") as f:
                            f.write(f"{count} - @{message.sender.username}\n")

                        count += 1
                        #time.sleep(1)
                else:
                    print(f"Сообщение от канала или бота")

        except telethon.errors.rpcerrorlist.MsgIdInvalidError:
            print(f"ID сообщения {idd} недействителен, пропускаем...")
            continue

client.disconnect()

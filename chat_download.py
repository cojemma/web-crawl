from chat_downloader import ChatDownloader
import matplotlib.pyplot as plt

chats = []
chats_time = {}
url = 'https://www.youtube.com/watch?v=ljUsRNYzl0k'
chat = ChatDownloader().get_chat(url)       # create a generator

for message in chat:                        # iterate over messages
    message = chat.format(message)             # print the formatted message
    message = message.split(' ')
    min = message[0][:-3]
    if min not in chats_time:
        chats_time[min] = 1
    else:
        chats_time[min] += 1

# print(chats_time)
# print(max([chats_time[min] for min in chats_time]))

plt.plot([min for min in chats_time], [chats_time[min] for min in chats_time])
plt.show()
import sys
import time
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
#    print(msg)
    if msg['text']=='/start':
        bot.sendMessage(chat_id, 'hii ! it is a simple calculator with python.enter numbers.')
    else:
        try:
            re=eval(msg['text'])
        except:
            re="error"
        bot.sendMessage(chat_id, "result= "+str(re))

bot = telepot.Bot('6940359512:AAEmKJi2G8K7L3cs0ud7g4vjMxq87tvLarU')
MessageLoop(bot, {'chat': handle
                  }).run_as_thread()
print ('Listening ...')

while 1:
    time.sleep(10)
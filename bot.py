import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")

print "bot run"
import telebot
import random
import json
import time
from pprint import pprint

bot = telebot.TeleBot("Your Token")

@bot.message_handler(commands=['feedback'])
def Hello(m):
    str = m.text
    txt = str.replace("/feedback", "")
    idA, cid = m.chat.id, m.chat.id
    bot.send_message('-100576894', "*° You Have New Message My Admin °*  : \n\n ```{}``` \n\n _Sender Id_ : *{}*".format(txt,idA), parse_mode="Markdown")
    bot.reply_to(m, "*Your Message Recived To Allwen :)*", parse_mode="Markdown")

@bot.message_handler(commands=['j'])
def j(m):
        datafile = [line.rstrip('\n') for line in open('admins.txt','rt')]
        tmt = m.from_user.id
        idA, cid = m.chat.id, m.chat.id
        for line in datafile:
            if str(tmt) not in datafile:
                bot.send_message(cid, "You're Nit Allwen !", parse_mode="Markdown")
                return
        to_id = m.text.split()[1]
        txt = m.text.split()[2:]
        text = ' '.join(txt)
        from_id = m.from_user.first_name
        bot.send_message(to_id, "{}Allwens Answer: \n ```{}```".format(from_id,text), parse_mode="Markdown")

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, "Hello welcome to *Allwen* Support \n\n [Made Your Bot!](https://telegram.me/MadeYourBots)\n\n\n Send Message : /feedback [text]", parse_mode="Markdown")

bot.polling()

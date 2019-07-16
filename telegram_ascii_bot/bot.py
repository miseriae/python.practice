#!/usr/bin/env python

import random
import secrets
import json
import telebot
from telebot.types import Message


TOKEN = secrets.TOKEN
STICKER_ID = 'CAADAQADswEAAml6MQVCfralNHScdwI'

bot = telebot.TeleBot(TOKEN)

USERS = set()


def log_writer(data):
    with open('log_file.json', 'a+') as log_file:
        json.dump(data, log_file)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    log_writer(message.json)
    if '/start' in message.text:
        bot.send_message(message.chat.id, "Hello there, traveler!")
        with open('hologram.gif.mp4', 'rb') as f:
            bot.send_document(message.chat.id, f)
    elif '/help' in message.text:
        bot.reply_to(message, "Sorry, I can't really help you atm, but you can send me a character and I will return ascii code.")


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    log_writer(message.json)
    print(message.from_user.id)
    reply = str([ord(c) for c in message.text])
    if message.from_user.id in USERS:
        reply += f" Your id is:{message.from_user.id}"
    bot.reply_to(message, reply)
    USERS.add(message.from_user.id)


@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    # print(message)
    # print(message.sticker)
    log_writer(message.json)
    bot.send_sticker(message.chat.id, STICKER_ID)
    


bot.polling(timeout=60)

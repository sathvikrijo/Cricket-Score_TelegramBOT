from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup
from cricket import *
keyboardPage0 = [[KeyboardButton("Cricket")],[KeyboardButton("Football")],[KeyboardButton("Tennis")]]
keyboardPage1 = [[KeyboardButton("1"),KeyboardButton("2"),KeyboardButton("3")],[KeyboardButton("4"),KeyboardButton("5"),KeyboardButton("6")],[KeyboardButton("7"),KeyboardButton("8"),KeyboardButton("9")],[KeyboardButton("10"),KeyboardButton("11"),KeyboardButton("12")]]
sports_reply = ReplyKeyboardMarkup(keyboardPage0,True,False)
no_reply = ReplyKeyboardMarkup(keyboardPage1,True,False)

def start(bot,update):
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name

    if last_name is None:
        user_name = first_name
    else:
        user_name = first_name + " " + last_name

    welcome_msg = "Welcome " + user_name + "\nI'm your bot speaking.\nI can do these kind of things👇\n\n" \
                    + "1  >>  Cricket Scores\n" + "2  >>  Football Scores\n" + "3  >>  Badmiton Scores"
    bot.send_message(chat_id=update.message.chat.id, text=welcome_msg, reply_markup=sports_reply)

def valid(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="You not allowed to call these commands, I'm Sorry")

def textMsg(bot,update):
    msg = str(update.effective_message.text)
    if msg == 'Cricket':
        match_titles = match()
        bot.send_message(chat_id=update.message.chat_id,text=match_titles, reply_markup=no_reply)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup
from cricket import *
keyboardPage0 = [[KeyboardButton("Cricket")],[KeyboardButton("Football")],[KeyboardButton("Tennis")]]
keyboardPage1 = [[KeyboardButton("1"),KeyboardButton("2"),KeyboardButton("3")],[KeyboardButton("4"),KeyboardButton("5"),KeyboardButton("6")],[KeyboardButton("7"),KeyboardButton("8"),KeyboardButton("9")],[KeyboardButton("10"),KeyboardButton("11"),KeyboardButton("Next page")]]
keyboardPage2 = [[KeyboardButton("12"),KeyboardButton("13"),KeyboardButton("14")],[KeyboardButton("15"),KeyboardButton("16"),KeyboardButton("17")],[KeyboardButton("Prev page"),KeyboardButton("18"),KeyboardButton("19")]]
sports_reply = ReplyKeyboardMarkup(keyboardPage0,True,False)
no_reply1 = ReplyKeyboardMarkup(keyboardPage1,True,False)
no_reply2 = ReplyKeyboardMarkup(keyboardPage2,True,False)

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
        bot.send_message(chat_id=update.message.chat_id,text=match_titles, reply_markup=no_reply1)
    elif msg == 'Next page':
        bot.send_message(chat_id=update.message.chat_id,text=msg, reply_markup=no_reply2)
    elif msg == 'Prev page':
        bot.send_message(chat_id=update.message.chat_id,text=msg, reply_markup=no_reply1)

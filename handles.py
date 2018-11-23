from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup
from cricket import *
import cricket
#keyboardPage0 = [[KeyboardButton("Cricket")],[KeyboardButton("Football")],[KeyboardButton("Tennis")]]
keyboardPage1 = [[KeyboardButton("1"),KeyboardButton("2"),KeyboardButton("3")],[KeyboardButton("4"),KeyboardButton("5"),KeyboardButton("6")],[KeyboardButton("7"),KeyboardButton("8"),KeyboardButton("9")],[KeyboardButton("10"),KeyboardButton("11"),KeyboardButton("Next page")]]
keyboardPage2 = [[KeyboardButton("12"),KeyboardButton("13"),KeyboardButton("14")],[KeyboardButton("15"),KeyboardButton("16"),KeyboardButton("17")],[KeyboardButton("18"),KeyboardButton("19"),KeyboardButton("20")],[KeyboardButton("Prev page"),KeyboardButton("21"),KeyboardButton("Next page")]]
keyboardPage3 = [[KeyboardButton("22"),KeyboardButton("23"),KeyboardButton("24")],[KeyboardButton("25"),KeyboardButton("26"),KeyboardButton("27")],[KeyboardButton("28"),KeyboardButton("29"),KeyboardButton("30")],[KeyboardButton("Prev page"),KeyboardButton("31"),KeyboardButton("32")]]
keyboardPage4 = [[KeyboardButton("33"),KeyboardButton("34"),KeyboardButton("35")],[KeyboardButton("36"),KeyboardButton("37"),KeyboardButton("38")],[KeyboardButton("39"),KeyboardButton("40"),KeyboardButton("41")],[KeyboardButton("Prev page"),KeyboardButton("42"),KeyboardButton("Next page")]]
keyboardPage5 = [[KeyboardButton("43"),KeyboardButton("44"),KeyboardButton("45")],[KeyboardButton("46"),KeyboardButton("47"),KeyboardButton("48")],[KeyboardButton("49"),KeyboardButton("50"),KeyboardButton("51")],[KeyboardButton("Prev page"),KeyboardButton("52"),KeyboardButton("53")]]
#sports_reply = ReplyKeyboardMarkup(keyboardPage0,True,False)
no_reply1 = ReplyKeyboardMarkup(keyboardPage1,True,False)
no_reply2 = ReplyKeyboardMarkup(keyboardPage2,True,False)
no_reply3 = ReplyKeyboardMarkup(keyboardPage3,True,False)
no_reply4 = ReplyKeyboardMarkup(keyboardPage4,True,False)
no_reply5 = ReplyKeyboardMarkup(keyboardPage5,True,False)
var = 0

def start(bot,update):
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name

    if last_name is None:
        user_name = first_name
    else:
        user_name = first_name + " " + last_name
    #welcome_msg = "Welcome " + user_name + "\nI'm your bot speaking.\nI can do these kind of things👇\n\n" \
                    #+ "1  >>  Cricket Scores\n" + "2  >>  Football Scores\n" + "3  >>  Badmiton Scores"
    welcome_msg = "Welcome " + user_name + "\nI'm your bot speaking.\nChoose any of the following matches from above👇"
    matcheses = match()
    bot.send_message(chat_id=update.message.chat.id, text=matcheses)
    bot.send_message(chat_id=update.message.chat.id, text=welcome_msg, reply_markup=no_reply1)

def valid(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="You not allowed to call these commands, I'm Sorry")

def textMsg(bot,update):
    msg = str(update.effective_message.text)
    global var
    if msg == 'Next page':
        if var == 0:
            bot.send_message(chat_id=update.message.chat_id, text=msg, reply_markup=no_reply2)
            var+=1
        elif var == 1:
            bot.send_message(chat_id=update.message.chat_id, text=msg, reply_markup=no_reply3)
            var+=1
        elif var == 2:
            bot.send_message(chat_id=update.message.chat_id, text=msg, reply_markup=no_reply4)
            var+=1
        elif var == 3:
            bot.send_message(chat_id=update.message.chat_id, text=msg, reply_markup=no_reply5)
            var+=1
        print(var)
    elif msg == 'Prev page':
        if var == 1:
            bot.send_message(chat_id=update.message.chat_id, text=msg, reply_markup=no_reply1)
            var-=1
        elif var == 2:
            bot.send_message(chat_id=update.message.chat_id, text=msg, reply_markup=no_reply2)
            var-=1
        elif var == 3:
            bot.send_message(chat_id=update.message.chat_id, text=msg, reply_markup=no_reply3)
            var-=1
        elif var == 4:
            bot.send_message(chat_id=update.message.chat_id, text=msg, reply_markup=no_reply4)
            var-=1
        print(var)
    else:
        value = validate(msg)
        link_no = int(msg)
        if value == True:
            match_name = extract_live_match(cricket.live_match_links[link_no-1])
        else:
            #print(link_no-cricket.live_match_len-1)
            match_name = extract_completed_match(cricket.completed_match_links[link_no-cricket.live_match_len-1])
        bot.send_message(chat_id=update.message.chat_id, text=match_name)

def validate(m):
    m = int(m)
    if m <= cricket.live_match_len:
        print("True")
        return True
    elif m <= cricket.live_match_len + cricket.completed_match_len:
        print("False")
        return False

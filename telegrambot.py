from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handles import *
import handles
botToken = "741591211:AAF9ZNd6kASuGMeeM6sO5TvzIFngWPgVdUY"

def main():
    updater = Updater(botToken)
    dp = updater.dispatcher
    updater.start_polling()

    #welcome_msg = CommandHandler('start',start)
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(MessageHandler(Filters.command,valid))
    dp.add_handler(MessageHandler(Filters.text,textMsg))

    updater.idle()

if __name__ == '__main__':
    main()

from telegram.ext import Updater, CommandHandler
from telegram import ReplyKeyboardMarkup

updater = Updater(token="token")


def favor_keyboard(bot, update):
    # import pdb; pdb.set_trace()
    chat_id = update.message.chat_id
    keyboard = [
        ['/icecream'],
        ['/coffee']
    ]
    bot.sendMessage(chat_id, "regster",
                    reply_markup=ReplyKeyboardMarkup(keyboard))


favor_command = CommandHandler('favor', favor_keyboard)

updater.dispatcher.add_handler(favor_command)

updater.start_polling()
updater.idle()

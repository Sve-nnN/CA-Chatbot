from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
import os
import messages
import buttons
import logging
import json
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
# if __version_info__ < (20, 0, 0, "alpha", 1):
#    raise RuntimeError(
#        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
#        f"{TG_VER} version of this example, "
#        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
#    )

# Enable logging
PORT = int(os.environ.get('PORT', 5000))

token = os.environ['CHATBOT_TOKEN']
#token = ""
updater = Updater(
    token=token, use_context=True)
dispatcher = updater.dispatcher
app = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

OK_RESPONSE = {
    'statusCode': 200,
    'headers': {'Content-Type': 'application/json'},
    'body': json.dumps('ok')
}
ERROR_RESPONSE = {
    'statusCode': 400,
    'body': json.dumps('Oops, something went wrong!')
}


def main():
    def help_command(update: Update, context: CallbackContext) -> None:
        keyboard = [
            ['/start']
        ]
        """Displays info on how to use the bot."""
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text="Use /start to test this bot.", reply_markup=ReplyKeyboardMarkup(
                keyboard, one_time_keyboard=True, input_field_placeholder="Elige una opción"
            ),)
        return message

    help_handler = CommandHandler(("help"), help_command)
    dispatcher.add_handler(help_handler)

    def echo_command(update: Update, context: CallbackContext) -> None:
        """Echo the user message."""
        message = update.message.reply_text(update.message.text)
        return message

    echo_handler = MessageHandler(Filters.text("esto es un eco"), echo_command)
    dispatcher.add_handler(echo_handler)

    def start(update: Update, context: CallbackContext):

        keyboard = buttons.combo_start
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.start(update), reply_markup=ReplyKeyboardMarkup(
                keyboard, one_time_keyboard=True, input_field_placeholder="Elige una opción"
            ),)
        return message

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    def scalping_command(update: Update, context: CallbackContext):
        keyboard = buttons.combo_scalping
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.scalping_club, reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        return message

    scalping_handler = MessageHandler(
        Filters.text(buttons.scalping_club), scalping_command)
    dispatcher.add_handler(scalping_handler)

    def mil_command(update: Update, context: CallbackContext):
        keyboard = buttons.combo_scalping
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.scalping_club, reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        return message

    mil_handler = MessageHandler(Filters.text(
        buttons.mil_al_millon), mil_command)
    dispatcher.add_handler(mil_handler)

    def cuenta_command(update: Update, context: CallbackContext):
        keyboard = buttons.combo_cuenta
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.scalping_club, reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        return message

    def ambos_command(update: Update, context: CallbackContext):
        keyboard = buttons.combo_ambos
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.dos_servicios, reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        return message

    ambos_handler = MessageHandler(
        Filters.text(buttons.dos_servicios), ambos_command)
    dispatcher.add_handler(ambos_handler)

    def cuentas_command(update: Update, context: CallbackContext):
        keyboard = buttons.combo_cuentas
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.cuenta_bybit, reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        return message

    cuentas_handler = MessageHandler(
        Filters.text(buttons.cuentas_bybit), cuentas_command)
    dispatcher.add_handler(cuentas_handler)

    def precio30_command(update: Update, context: CallbackContext):
        ammount = 30
        keyboard = buttons.pagos
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        return message

    precio30_handler = MessageHandler(
        Filters.text(buttons.uno_treinta), precio30_command)
    dispatcher.add_handler(precio30_handler)

    def precio50_command(update: Update, context: CallbackContext):
        ammount = 50
        keyboard = buttons.pagos
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        return message

    precio50_handler = MessageHandler(
        Filters.text(buttons.uno_cincuenta), precio50_command)
    dispatcher.add_handler(precio50_handler)

    def precio95_command(update: Update, context: CallbackContext):
        ammount = 95
        keyboard = buttons.pagos
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        return message

    precio95_handler = MessageHandler(
        Filters.text(buttons.dos_nuevecinco), precio95_command)
    dispatcher.add_handler(precio95_handler)

    def precio135_command(update: Update, context: CallbackContext):
        ammount = 140
        keyboard = buttons.pagos
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        return message

    precio135_handler = MessageHandler(
        Filters.text(buttons.tres_cien), precio135_command)
    dispatcher.add_handler(precio135_handler)

    def precio17_command(update: Update, context: CallbackContext):
        ammount = 17
        keyboard = buttons.pagos
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        return message

    precio17_handler = MessageHandler(
        Filters.text(buttons.medio_diecisiete), precio17_command)
    dispatcher.add_handler(precio17_handler)

    def precio55_command(update: Update, context: CallbackContext):
        ammount = 55
        keyboard = buttons.pagos
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        return message

    precio55_handler = MessageHandler(
        Filters.text(buttons.dos_cincocinco), precio55_command)
    dispatcher.add_handler(precio55_handler)

    def precio75_command(update: Update, context: CallbackContext):
        ammount = 75
        keyboard = buttons.pagos
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        return message
    precio75_handler = MessageHandler(
        Filters.text(buttons.tres_sietecinco), precio75_command)
    dispatcher.add_handler(precio75_handler)

    def precio30_command(update: Update, context: CallbackContext):
        ammount = 30
        keyboard = buttons.pagos
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
        return message

    precio30_handler = MessageHandler(
        Filters.text(buttons.medio_treinta), precio30_command)
    dispatcher.add_handler(precio30_handler)

    def pago_command(update: Update, context: CallbackContext):
        keyboard = [
            [
                InlineKeyboardButton(
                    "Ir al bot", url="http://t.me/criptoavancespagos_bot"),
            ],

        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.pago_realizado, reply_markup=reply_markup)
        return message

    pago_handler = MessageHandler(
        Filters.text(buttons.pago), pago_command)
    dispatcher.add_handler(pago_handler)

    def unknown(update: Update, context: CallbackContext):
        message = context.bot.send_message(chat_id=update.effective_chat.id,
                                           text="Disculpa, no te he entendido. Puedes intentar diciendo: /start")
        return message

    unknown_handler = MessageHandler(Filters.text, unknown)
    dispatcher.add_handler(unknown_handler)

    webhook = updater.start_polling()
    if webhook:
        updater.start_polling()
        return OK_RESPONSE
    else:
        return ERROR_RESPONSE


main()
app.run(debug=False, host='0.0.0.0')

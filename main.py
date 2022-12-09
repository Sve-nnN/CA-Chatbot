from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from flask import Flask
import os
import messages
import buttons
import logging
app = Flask(__name__)

token = os.environ.get('TOKEN')
updater = Updater(
    token=token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def help_command(update: Update, context: CallbackContext) -> None:
    keyboard = [
        ['/start']
    ]
    """Displays info on how to use the bot."""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Use /start to test this bot.", reply_markup=ReplyKeyboardMarkup(
            keyboard, one_time_keyboard=True, input_field_placeholder="Elige una opción"
        ),)


def echo_command(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def start(update: Update, context: CallbackContext):

    keyboard = buttons.combo_start
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.start(update), reply_markup=ReplyKeyboardMarkup(
            keyboard, one_time_keyboard=True, input_field_placeholder="Elige una opción"
        ),)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def scalping_command(update: Update, context: CallbackContext):
    keyboard = buttons.combo_scalping
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.scalping_club, reply_markup=ReplyKeyboardMarkup(keyboard))


def mil_command(update: Update, context: CallbackContext):
    keyboard = buttons.combo_scalping
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.scalping_club, reply_markup=ReplyKeyboardMarkup(keyboard))


def cuenta_command(update: Update, context: CallbackContext):
    keyboard = buttons.combo_cuenta
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.scalping_club, reply_markup=ReplyKeyboardMarkup(keyboard))


def ambos_command(update: Update, context: CallbackContext):
    keyboard = buttons.combo_ambos
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.dos_servicios, reply_markup=ReplyKeyboardMarkup(keyboard))


def cuentas_command(update: Update, context: CallbackContext):
    keyboard = buttons.combo_cuentas
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.cuenta_bybit, reply_markup=ReplyKeyboardMarkup(keyboard))


def precio30_command(update: Update, context: CallbackContext):
    ammount = 30
    keyboard = buttons.pagos
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard))


def precio50_command(update: Update, context: CallbackContext):
    ammount = 50
    keyboard = buttons.pagos
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard))


def precio95_command(update: Update, context: CallbackContext):
    ammount = 95
    keyboard = buttons.pagos
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard))


def precio135_command(update: Update, context: CallbackContext):
    ammount = 135
    keyboard = buttons.pagos
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard))


def precio17_command(update: Update, context: CallbackContext):
    ammount = 17
    keyboard = buttons.pagos
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard))


def precio55_command(update: Update, context: CallbackContext):
    ammount = 17
    keyboard = buttons.pagos
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard))


def precio75_command(update: Update, context: CallbackContext):
    ammount = 17
    keyboard = buttons.pagos
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard))


def precio17_command(update: Update, context: CallbackContext):
    ammount = 17
    keyboard = buttons.pagos
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.funcPago(ammount), reply_markup=ReplyKeyboardMarkup(keyboard))


def pago_command(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton(
                "Ir al bot", url="http://t.me/criptoavancespagos_bot"),
        ],

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.pago_realizado, reply_markup=reply_markup)


def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Disculpa, no te he entendido. Puedes intentar diciendo: /start")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text("esto es un eco"), echo_command)
dispatcher.add_handler(echo_handler)


help_handler = CommandHandler(("help"), help_command)
dispatcher.add_handler(help_handler)

scalping_handler = MessageHandler(
    Filters.text(buttons.scalping_club), scalping_command)
dispatcher.add_handler(scalping_handler)

mil_handler = MessageHandler(Filters.text(buttons.mil_al_millon), mil_command)
dispatcher.add_handler(mil_handler)

ambos_handler = MessageHandler(
    Filters.text(buttons.dos_servicios), ambos_command)
dispatcher.add_handler(ambos_handler)

cuentas_handler = MessageHandler(
    Filters.text(buttons.cuentas_bybit), cuentas_command)
dispatcher.add_handler(cuentas_handler)

precio30_handler = MessageHandler(
    Filters.text(buttons.uno_treinta), precio30_command)
dispatcher.add_handler(precio30_handler)

precio17_handler = MessageHandler(
    Filters.text(buttons.medio_diecisiete), precio17_command)
dispatcher.add_handler(precio17_handler)

precio55_handler = MessageHandler(
    Filters.text(buttons.dos_cincocinco), precio55_command)
dispatcher.add_handler(precio55_handler)

precio75_handler = MessageHandler(
    Filters.text(buttons.tres_sietecinco), precio75_command)
dispatcher.add_handler(precio75_handler)

precio50_handler = MessageHandler(
    Filters.text(buttons.uno_cincuenta), precio50_command)
dispatcher.add_handler(precio50_handler)

precio95_handler = MessageHandler(
    Filters.text(buttons.dos_nuevecinco), precio95_command)
dispatcher.add_handler(precio95_handler)

precio135_handler = MessageHandler(
    Filters.text(buttons.tres_cien), precio135_command)
dispatcher.add_handler(precio135_handler)

pago_handler = MessageHandler(
    Filters.text(buttons.pago), pago_command)
dispatcher.add_handler(pago_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4444)))
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


updater.start_polling()

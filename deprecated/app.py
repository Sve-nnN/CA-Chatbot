from flask import Flask
from flask import request
from flask import Response
import requests

TOKEN = "token"
app = Flask(__name__)
message_start = """Únete a los Servicios exclusivos de CA, solo tiene que seguir los siguientes pasos:
                    1️⃣Elija el servicio que desea
                    2️⃣Seleccione la promoción
                    3️⃣Envié el pago correspondiente a la dirección indicada, desde cualquier billetera o intercambio.
                    4️⃣Ingrese a nuestra plataforma de Discord y envíe sus datos correspondientes.
                    5️⃣ El pago se confirmará dentro de 15 a 20 minutos, y se le asignará los roles correspondientes.
                    Cualquier duda puede comunicarse con un administrador: @ Gabypecr o @ Susana_scalper"""
message_scalping_club = """¡Excelente!
Al contratar este servicio, obtendrás acceso a lo siguiente:
🔸Alertas 24/7
🔸Estrategia de Scalping
🔸Sesiones por la plataforma de zoom
🔸Excel´s para elegir la agresividad para operar
🔸Drive con material y sesiones grabadas.
🔸Chat para interactuar con otros usuarios VIP.
Selecciona la promoción que deseas contratar.
"""
message_mil_al_millon = """¡Excelente!
Al contratar este servicio, obtendrás acceso a lo siguiente:
🔸Acceso al canal de señales
🔸Estrategia de trading
🔸Sesiones en vivo por la plataforma de zoom.
🔸Excel’s para operar.
🔸Drive con material de apoyo y sesiones grabadas.
🔸Canal para interactuar con otros usuarios VIP.
Si tienes una cuenta en Bybit obtienes un 70% de descuento en el servicio. Si no tienes una cuenta, crea tu cuenta con el siguiente enlace: https://partner.bybit.com/b/CriptoAvances
"""
message_cuenta_bybit = """¡Muy bien!
Ahora selecciona la promoción que deseas contratar.
"""
message_dos_servicios = """¡Excelente!
Al contratar los dos servicios de Cripto Avances, obtendrás acceso a lo siguiente:
🔸Acceso a los canales de señales y de alertas 24/7.
🔸Estrategia de trading
🔸Sesiones en vivo por la plataforma de zoom.
🔸Excel’s para operar.
🔸Drive con material de apoyo y sesiones grabadas.
🔸Canal para interactuar con otros usuarios VIP.
Si tienes una cuenta en Bybit obtienes un 70% de descuento en el servicio. Si no tienes una cuenta, crea tu cuenta con el siguiente enlace: https://partner.bybit.com/b/CriptoAvances
"""
message_pago_realizado = """¡Bienvenido a la comunidad VIP de Cripto Avances!
Esta muy cerca de comenzar a disfrutar de los beneficios de unirse a nuestra exclusiva comunidad.
Por favor ingrese a nuestra plataforma de Discord
https://discord.com/invite/SHhXMCjFZC

Envíe en un solo mensaje y en este orden los siguientes datos:
Nombre apellido (Cripto Avance)
Usuario discord (ejemplo#1234
Telegram (@ejemplo)
Email (ejemplo@gmail.com)
TxId de pago (Le llega en un correo o lo puede encontrar en el historial de transacciones de su Exchange)
Pais (México)
"""
message_ultima_respuesta = """¡Excelente!
Bienvenido al servicio exclusivo de Cripto Avances. En un momento se le activara los roles para que pueda ver y acceder a los canales del servicio.
Cualquier duda puede comunicarse con un administrador: @Gabypecr o @Susana_scalper
"""
message_default = """Esta es una respuesta por defecto. Puedes empezar a usar el bot tocando el botón de abajo"""
2
keyboard = [['ES', 'EN']]


def sendMoney(ammount):
    text = """Envíe %i USDT  a la siguiente dirección:
TZ5xVaDMKCQBinsyHA3hmBRyaEuwASftA6
Recuerde enviar solo USDT, utilizando la red TRC20.
Asegúrese de incluir la tarifa de red.
""" % ammount
    return text


button_start = [[
    {
        "text": "Iniciar Bot",
        "callback_data": "empezar"
    }]
]
button_combo_start = [[
    {
        "text": button_scalping_club,
        "callback_data": "scalping"
    },
    {
        "text": button_mil_al_millon,
        "callback_data": "millon"
    },
    {
        "text": button_dos_servicios,
        "callback_data": "ambos"
    }]
]
button_combo_scalping = [[
    {
        "text": button_medio_diecisiete,
        "callback_data": "scalping"
    },
    {
        "text": button_uno_treinta,
        "callback_data": "millon"
    },
    {
        "text": button_dos_cincocinco,
        "callback_data": "ambos"
    },    {
        "text": button_tres_sietecinco,
        "callback_data": "ambos"
    }]
]


def responseDefault(chat_id):

    ReplyKeyboardMarkup(*args, **kwargs)


def responseStart(chat_id):
    tel_send_inlinebutton(chat_id, message_start, button_combo_start)


def responseScalping(chat_id):
    tel_send_inlinebutton(chat_id, message_scalping_club,
                          button_combo_scalping)


def responseMillon(chat_id):
    tel_send_inlinebutton(chat_id, message_mil_al_millon, button_cuenta_bybit)


def responseBybit(chat_id):
    tel_send_inlinebutton(chat_id, message_cuenta_bybit, button_combo_scalping)


def responseBoth(chat_id):
    tel_send_inlinebutton(chat_id, message_dos_servicios, button_cuenta_bybit)


def parse_message(message):
    print("message-->", message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id, txt


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)
    return r


def tel_send_inlinebutton(chat_id, text, button):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': {
            "inline_keyboard": button
        }
    }
    r = requests.post(url, json=payload)
    return r


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        chat_id, txt = parse_message(msg)

        if txt == "empezar":
            responseStart(chat_id)
        elif txt == "scalping":
            responseScalping(chat_id)
        elif txt == "millon":
            responseMillon(chat_id)
        elif txt == "bybit":
            responseBybit(chat_id)
        elif txt == "ambos":
            responseBoth(chat_id)
        else:
            responseDefault(chat_id)

        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"


if __name__ == '__main__':
    app.run(debug=True)

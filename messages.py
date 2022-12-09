
scalping_club = """¡Excelente!
Al contratar este servicio, obtendrás acceso a lo siguiente:
🔸Alertas 24/7
🔸Estrategia de Scalping
🔸Sesiones por la plataforma de zoom
🔸Excels para elegir la agresividad para operar
🔸Drive con material y sesiones grabadas.
🔸Chat para interactuar con otros usuarios VIP.
Selecciona la promoción que deseas contratar.
"""
mil_al_millon = """¡Excelente!
Al contratar este servicio, obtendrás acceso a lo siguiente:
🔸Acceso al canal de señales
🔸Estrategia de trading
🔸Sesiones en vivo por la plataforma de zoom.
🔸Excel’s para operar.
🔸Drive con material de apoyo y sesiones grabadas.
🔸Canal para interactuar con otros usuarios VIP.
Si tienes una cuenta en Bybit obtienes un 70% de descuento en el servicio. Si no tienes una cuenta, crea tu cuenta con el siguiente enlace: https://partner.bybit.com/b/CriptoAvances
"""
cuenta_bybit = """¡Muy bien!
Ahora selecciona la promoción que deseas contratar.
"""
dos_servicios = """¡Excelente!
Al contratar los dos servicios de Cripto Avances, obtendrás acceso a lo siguiente:
🔸Acceso a los canales de señales y de alertas 24/7.
🔸Estrategia de trading
🔸Sesiones en vivo por la plataforma de zoom.
🔸Excel’s para operar.
🔸Drive con material de apoyo y sesiones grabadas.
🔸Canal para interactuar con otros usuarios VIP.
Si tienes una cuenta en Bybit obtienes un 70% de descuento en el servicio. Si no tienes una cuenta, crea tu cuenta con el siguiente enlace: https://partner.bybit.com/b/CriptoAvances
"""
pago_realizado = """¡Bienvenido a la comunidad VIP de Cripto Avances!
Esta muy cerca de comenzar a disfrutar de los beneficios de unirse a nuestra exclusiva comunidad.

Por favor, envie un mensaje a este bot: @criptoavancespagos_bot con los siguientes datos:
- Nombre apellido (Cripto Avance)
- Usuario discord (ejemplo#1234
- Telegram (@ejemplo)
- Email (ejemplo@gmail.com)
- TxId de pago (Le llega en un correo o lo puede encontrar en el historial de transacciones de su Exchange)
- Pais (México)

Lo invitamos a unirse a nuestra plataforma de Discord
https://discord.com/invite/SHhXMCjFZC
"""


def funcPago(precio):
    enviar_dinero = """Envíe $%s a la siguiente dirección:
TZ5xVaDMKCQBinsyHA3hmBRyaEuwASftA6
Recuerde enviar solo USDT, utilizando la red TRC20. 
Asegúrese de incluir la tarifa de red. 
""" % precio
    return enviar_dinero


def start(update):
    user = update.message.from_user
    start = """Hola {}! Únete a los Servicios exclusivos de CA, solo tiene que seguir los siguientes pasos:
1️⃣Elija el servicio que desea
2️⃣Seleccione la promoción
3️⃣Envié el pago correspondiente a la dirección indicada, desde cualquier billetera o intercambio.
4️⃣Ingrese a nuestra plataforma de Discord y envíe sus datos correspondientes.
5️⃣ El pago se confirmará dentro de 15 a 20 minutos, y se le asignará los roles correspondientes.
Cualquier duda puede comunicarse con un administrador: @Gabypecr o @Susana_scalper""".format(
        user['username'])
    return start


ultima_respuesta = """¡Excelente!
Bienvenido al servicio exclusivo de Cripto Avances. En un momento se le activara los roles para que pueda ver y acceder a los canales del servicio.
Cualquier duda puede comunicarse con un administrador: @Gabypecr o @Susana_scalper
"""
default = """Esta es una respuesta por defecto. Puedes empezar a usar el bot tocando el botón de abajo"""

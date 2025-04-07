import os
from twilio.rest import Client

def send_whatsapp_message(to, message):
    Account = os.getenv("TWILIO_ACCOUNT")
    Token = os.getenv("TWILIO_TOKEN")
    Number = os.getenv("TWILIO_PHONE")

    client = Client(Account, Token)

    try:
        message = client.messages.create(
            from_=Number,
            body=message,
            to=f"whatsapp:{to}"
        )
        print(f"Mensaje enviado: {message.sid}")
    except Exception as e:
        print(f"Error al enviar mensaje: {e}")


if __name__ == "__main__":
    send_whatsapp_message("+52XXXXXXXXXX", "¡Hola desde Python!")




from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hola' in incoming_msg:
        msg.body("¡Hola! ¿Cómo puedo ayudarte?")
    else:
        msg.body("Gracias por tu mensaje. Estoy procesando tu solicitud.")

    return str(resp)

@app.route("/", methods=["GET"])
def home():
    return "Bot funcionando 🟢"

if __name__ == "__main__":
    app.run()

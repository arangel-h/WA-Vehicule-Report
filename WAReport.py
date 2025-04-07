
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

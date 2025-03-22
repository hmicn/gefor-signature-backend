import requests
import base64

url = 'http://localhost:5000/api/v1/check-signature-now'
response = requests.post(url)
print(response.json())

url = 'http://localhost:5000/api/v1/login'
response = requests.post(url, json={'username': 'student', 'password': 'school'})
print(response.json())
jwt = response.json()['token']

url = 'http://localhost:5000/api/v1/signatures'
with open('signature.png', 'rb') as f:
    image_data = f.read()
    # Encode en base64 et décodage en chaîne de caractères
    image_b64 = base64.b64encode(image_data).decode('utf-8')
    print(image_b64)
    response = requests.post(url, json={'image': image_b64}, headers={'Authorization': 'Bearer ' + jwt})
    print(response.json())
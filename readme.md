# Simple mock backend for RN

### 1. Install dependencies

```
pip install Flask flask-cors PyJWT
```

### 2. Run the backend! 

```
python backend.py
```

This should produce the following lines in the terminal :

```
 * Serving Flask app 'backend'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 616-941-285
```

### 3. Run the tests

```
python test.py
```

This should produce the following lines in the terminal :

```
{'shouldSign': True}
{'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InN0dWRlbnQiLCJleHAiOjE3NDI2NjU2NTl9.xW5o72pYavNZEh51pU5hY-bZH0bSFr49IlFfIUgfYwQ'}
{'filename': 'signature_20250322171741658189.png', 'message': 'Signature enregistrée avec succès'}
```
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>Click the link to fetch your phone number</h1>
        <a href="/get_phone_number">Customization Link</a>
    '''

@app.route('/get_phone_number')
def get_phone_number():
    # Fetching phone number (mocking the actual fetching process)
    phone_number = os.popen('termux-telephony-call-log').read()
    return f'<h1>Your Phone Number: {phone_number}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

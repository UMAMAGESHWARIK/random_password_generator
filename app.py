from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_passwords', methods=['POST'])
def generate_passwords():
    numofpwds = int(request.form['numofpwds'])
    pwdlen = int(request.form['pwdlen'])
    randomchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*"
    passwords = []

    for i in range(numofpwds):
        pwd = ''.join(random.choice(randomchars) for j in range(pwdlen))
        passwords.append(pwd)

    return jsonify(passwords)

if __name__ == '__main__':
    app.run(debug=True)

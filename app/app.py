# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///keys.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    nfc_key = db.Column(db.String(120), unique=True, nullable=False)

db.create_all()

@app.route('/register', methods=['POST'])
def register_key():
    username = request.form['username']
    nfc_key = request.form['nfc_key']
    if User.query.filter_by(nfc_key=nfc_key).first():
        return jsonify({"message": "NFC key already registered"}), 400

    new_user = User(username=username, nfc_key=nfc_key)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Key registered successfully"}), 200

@app.route('/unlock', methods=['POST'])
def unlock():
    nfc_key = request.form['nfc_key']
    user = User.query.filter_by(nfc_key=nfc_key).first()
    if user:
        # Логика разблокировки замка, например, отправка сигнала на GPIO
        return jsonify({"message": "Door unlocked"}), 200
    else:
        return jsonify({"message": "Access denied"}), 403
        # app.py (дополнение)
from flask import render_template

@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')

@app.route('/unlock', methods=['GET'])
def unlock_form():
    return render_template('unlock.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# nfc_reader.py
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests

reader = SimpleMFRC522()

try:
    print("Hold a tag near the reader")
    id, text = reader.read()
    print(f"ID: {id}\nText: {text}")

    # Отправка данных на сервер для проверки
    response = requests.post('http://your-server-address/unlock', data={'nfc_key': id})
    if response.status_code == 200:
        print("Door unlocked")
    else:
        print("Access denied")
finally:
    GPIO.cleanup()
  

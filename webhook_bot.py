import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7619193220:AAGAsJcpKoZDu0GrKTvCOD3FIzM1UUWo-e0")
ADMIN_ID = os.environ.get("ADMIN_ID", "437888858")  # строка или число

TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_to_telegram(text: str):
    payload = {
        "chat_id": ADMIN_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    r = requests.post(f"{TELEGRAM_API}/sendMessage", data=payload, timeout=10)
    return r.ok, r.text

@app.route("/send-booking", methods=["POST"])
def send_booking():
    data = request.form.to_dict() if request.form else request.get_json(silent=True) or {}
    # Пример expected fields: name, checkin, checkout, people, contact, comment
    name = data.get("name", "—")
    checkin = data.get("checkin", "—")
    checkout = data.get("checkout", "—")
    people = data.get("people", "—")
    contact = data.get("contact", "—")
    comment = data.get("comment", "")
    msg = (
        f"🆕 <b>Новая заявка с сайта</b>\n"
        f"Имя: {name}\n"
        f"Заезд: {checkin}\n"
        f"Выезд: {checkout}\n"
        f"Человек: {people}\n"
        f"Контакт: {contact}\n"
    )
    if comment:
        msg += f"Комментарий: {comment}\n"
    ok, resp = send_to_telegram(msg)
    if ok:
        return jsonify({"status": "sent"}), 200
    else:
        return jsonify({"status": "error", "detail": resp}), 500

if __name__ == "__main__":
    # Запуск: export BOT_TOKEN=...; export ADMIN_ID=...; python webhook_bot.py
    app.run(host="0.0.0.0", port=5005)

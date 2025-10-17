from app import app, render_template
from flask import request,redirect, url_for
import requests


@app.get('/contact')
def contact():
    return render_template("front/contact.html")


@app.post('/contact/submit')
def contact_submit():
    form = request.form
    name = form.get('name')
    email = form.get('email')
    message = form.get('message')

    print(f"Received form data: Name={name}, Email={email}, Message={message}")

    token = "8277635671:AAFk00SgNqkE34WNkst_GwlCprCZw3AQCcg"
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": "@teamsupport_channel",
        "text": (
            "<b>📩 New Contact Form Submission</b>\n\n"
            "Here’s a new inquiry from your website contact page:\n\n"
            f"👤 <b>Name:</b> {name}\n"
            f"📧 <b>Email:</b> {email}\n"
            f"💬 <b>Message:</b>\n{message}\n\n"
            "---------------------------------------\n"
            "<i>Sent automatically from your website contact form.</i>"
        ),
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }

    headers = {
        "accept": "application/json",
        "User-Agent": "Telegram Bot",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return redirect(url_for("contact"))
    else:
        return f"Failed to send message: {response.text}", 500

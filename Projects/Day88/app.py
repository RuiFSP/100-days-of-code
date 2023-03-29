import os

from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

mail_settings = {

    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.getenv('EMAIL'),
    "MAIL_PASSWORD": os.getenv('PASSWORD')
}

app.config.update(mail_settings)
mail = Mail(app)


class Contact:
    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        contact_form = Contact(
            request.form["name"],
            request.form["email"],
            request.form["message"]
        )

        msg = Message(
            subject=f'{contact_form.name} sent you a message',
            sender=app.config.get("MAIL_USERNAME"),
            recipients=['ruifspinto@gmail.com', app.config.get("MAIL_USERNAME")],
            body=f'''
                
            {contact_form.name} with email {contact_form.email}, sent you the following message
            
            {contact_form.message}
            '''
        )

        mail.send(msg)
        flash('Success , message was sent')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

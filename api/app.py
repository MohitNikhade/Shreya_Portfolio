from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

app = Flask(__name__, static_folder="../public/static", template_folder="../public")
app.secret_key = os.getenv('SECRET_KEY')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            subject = request.form['subject']
            message = request.form['message']
            
            msg = Message(
                subject=f"New message from {name}: {subject}",
                recipients=['shreyapawark7@gmail.com'],
                reply_to=email
            )
            msg.body = f"""
            Name: {name}
            Email: {email}
            Subject: {subject}
            
            Message:
            {message}
            """
            
            mail.send(msg)
            return "Message sent successfully!", 200
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return f"Error sending message: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
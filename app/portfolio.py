from flask import (
    Blueprint, render_template, request, redirect, url_for, current_app
)

import smtplib

bp = Blueprint('portfolio', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')


@bp.route('/mail', methods=['GET', 'POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    mesage = request.form.get('message')
    
    if request.method == 'POST':
        send(name, email, mesage)
        return render_template('portfolio/sent-mail.html')
    
    return redirect(url_for('portfolio.index'))

def send(name, email, message):
    from_email = current_app.config['FROM_MAIL']
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, current_app.config['MAIL_PASS'])
    msg = f"Mi nombre es: {name}\n\n" \
        f"Me puedes contactar al correo: {email}\n\n{message}" 
    server.sendmail(from_email, from_email, msg)
    server.quit()

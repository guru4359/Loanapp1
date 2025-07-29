from flask import Flask, render_template, request, session, redirect, url_for
from flask_babel import Babel, gettext as _
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'demo-secret')
babel = Babel(app)

# Configuration: available banks and languages
AVAILABLE_BANKS = {
    'sahyadri': {'name': 'Sahyadri Co-op Bank', 'logo': 'sahyadri_logo.png'},
    'krishi': {'name': 'Krishi Co-op Bank', 'logo': 'krishi_logo.png'},
    'jeevan': {'name': 'Jeevan Jyoti Co-op Bank', 'logo': 'jeevan_logo.png'}
}
LANGUAGES = ['en', 'hi', 'mr']

@app.route('/')
def choose_bank():
    return render_template('choose_bank.html', banks=AVAILABLE_BANKS)

@app.route('/<bank_id>/')
def home(bank_id):
    bank = AVAILABLE_BANKS.get(bank_id)
    if not bank:
        return redirect(url_for('choose_bank'))
    session['bank'] = bank_id
    return render_template('index.html', bank=bank)

@app.route('/<bank_id>/apply', methods=['GET', 'POST'])
def apply(bank_id):
    bank = AVAILABLE_BANKS.get(bank_id)
    if request.method == 'POST':
        applicant_name = request.form.get('name')
        email = request.form.get('email')
        amount = request.form.get('amount')
        # Placeholder: save to DB
        return render_template('confirmation.html', name=applicant_name, bank=bank)
    return render_template('apply.html', bank=bank)

@babel.localeselector
def get_locale():
    return request.args.get('lang') or 'en'

if __name__ == '__main__':
    app.run(debug=True)

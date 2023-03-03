# Import Flask
from flask import Flask
from flask import render_template

# Import for Bitcoin price
import datetime
from forex_python.bitcoin import BtcConverter


app = Flask(__name__)

b = BtcConverter()

@app.route('/')
def index():
    btc_rub = b.get_latest_price('RUB')
    btc_usd = b.get_latest_price('USD')
    btc_eur = b.get_latest_price('EUR')

    return render_template('index.html', btc_rub=btc_rub, btc_usd=btc_usd, btc_eur=btc_eur)

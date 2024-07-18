"""from flask import Flask, Blueprint, redirect, url_for, request, render_template
import requests
from ems.dbase import get_db



# create blueprint
pbp = Blueprint('paystack', __name__, url_prefix='/paystack')

@pbp.route('/fund_wallet', methods=('GET', 'POST'))
def fund_wallet():
    if request.method == 'GET':
        return render_template('paystack/fund_wallet.html')

"""

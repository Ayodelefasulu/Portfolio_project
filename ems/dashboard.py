from flask import (Blueprint, flash, g, jsonify, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from ems.auth import login_required
from ems.dbase import get_db
import requests

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# Paystack secret and public api keys
PAYSTACK_PUBLIC_KEY = 'pk_test_dc6aa3d710e6cbbc56cd6918f406c328cb179ada'
#PAYSTACK_SECRET_KEY = 'sk_test_DEFAULT'
PAYSTACK_SECRET_KEY = 'sk_test_8e37fbd0c795e4a2a5fb64a6b703222de9680856'

@bp.route('/')
@login_required
def index():
    db = get_db()
    # Fetch transaction history
    transactionss = db.execute(
        'SELECT id, transaction_type, amount, created FROM `transaction` WHERE user_id = ? ORDER BY created DESC',
        (g.user['id'],)
    ).fetchall()
    # Fetch user profile
    profile = db.execute(
        'SELECT id, firstname, lastname, email FROM profile WHERE user_id = ?',
        (g.user['id'],)
    ).fetchone()

    # Render the dashboard template with the user data
    return render_template('dashboard/index.html', transactionss=transactionss, profile=profile)

@bp.route('/fund_wallet_paystack')
@login_required
def fund_wallet_paystack():
    # Implement funding wallet with Paystack
    #if request.method == 'GET':
    return render_template('dashboard/fund_wallet_paystack.html')

@bp.route('/fund_wallet_paystack', methods=('GET', 'POST'))
@login_required
def post_fund_wallet_paystack():
    """ User enters email and amount to be fund in the form
        the header is submited in addtion to his data.
        User is redirected to paystack's payment page and upon
        successful/failed payment, paystack displays the status"""

    if request.method == 'POST':
        email = request.form['email']
        amount = int(request.form['amount']) * 100

    headers = {
        'Authorization': 'Bearer {}'.format(PAYSTACK_SECRET_KEY),
        'Content-Type': 'application/json',
    }

    data = {
        'email': email,
        'amount': amount,
    }

    response = requests.post('https://api.paystack.co/transaction/initialize', headers=headers, json=data)
    if response.status_code == 200:
        payment_data = response.json()
        payment_url = response.json()['data']['authorization_url']
        return redirect(payment_url)
    else:
        return jsonify(response.json()), 400

""" *********************************************************************** """
# Paystack webhook route
@bp.route('/payment/verify', methods=['POST'])
def paystack_webhook():
    """ This function handles payment verifcation by redirecting 
        to web server """
    data = request.get_json()

    if data['event'] == 'charge.success':
        reference = data['data']['reference']
        return verify_payment(reference)
    else:
        return 'Event not handled', 400

# Payment verification function
def verify_payment(reference):
    headers = {
        'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}'
    }
    response = requests.get(f'https://api.paystack.co/transaction/verify/{reference}', headers=headers)

    if response.status_code == 200:
        payment_data = response.json()

        if payment_data['data']['status'] == 'success':
            update_wallet(payment_data['data'])
            return redirect(url_for('payment_success'))
        else:
            return redirect(url_for('payment_failure'))
    else:
        return 'Verification failed', 400
""" ************************************************************************ """
# You have to update wallet
def update_wallet(payment_data):
    user_id = payment_data['metadata']['user_id']
    amount = payment_data['amount'] / 100  # Convert kobo to Naira

    db = get_db()
    db.execute(
        'UPDATE users SET wallet_balance = wallet_balance + ? WHERE id = ?',
        (amount, user_id)
    )
    db.commit()

@bp.route('/fund_wallet_atm')
@login_required
def fund_wallet_atm():
    # Implement funding wallet with ATM
    return render_template('dashboard/fund_wallet_atm.html')

@bp.route('/buy_data')
@login_required
def buy_data():
    # Implement buying data
    return render_template('dashboard/buy_data.html')

@bp.route('/buy_airtime')
@login_required
def buy_airtime():
    # Implement buying airtime
    return render_template('dashboard/buy_airtime.html')

@bp.route('/pay_utility')
@login_required
def pay_utility():
    # Implement utility payment
    return render_template('dashboard/pay_utility.html')

@bp.route('/cable_subscription')
@login_required
def cable_subscription():
    # Implement cable subscription
    return render_template('dashboard/cable_subscription.html')

@bp.route('/buy_sell_giftcards')
@login_required
def buy_sell_giftcards():
    # Implement buying and selling gift cards
    return render_template('dashboard/buy_sell_giftcards.html')


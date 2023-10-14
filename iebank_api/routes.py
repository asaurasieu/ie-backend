from flask import Flask, request
from iebank_api import db, app
from iebank_api.models import Account
import sys 


@app.route('/')
def hello_world():
    app.logger.debug('Route / called')
    return 'Hello, World!'

@app.route('/skull', methods=['GET'])
def skull():
    app.logger.debug('Route /skull GET called')
    return 'Hi! This is the BACKEND SKULL! 💀'


@app.route('/accounts', methods=['POST'])
def create_account():
    app.logger.debug('Route /accounts POST called')
    name = request.json['name']
    currency = request.json['currency']
    country = request.json['country']
    account = Account(name, currency, country)
    db.session.add(account)
    db.session.commit()
    return format_account(account)

@app.route('/accounts', methods=['GET'])
def get_accounts():
    app.logger.debug('Route /accounts GET')
    accounts = Account.query.all()
    return {'accounts': [format_account(account) for account in accounts]}

@app.route('/accounts/<int:id>', methods=['GET'])
def get_account(id):
    app.logger.debug('Route /accounts GET called with id: ' + str(id))
    account = Account.query.get(id)
    return format_account(account)

@app.route('/accounts/<int:id>', methods=['PUT'])
def update_account(id):
    app.logger.debug('Route /accounts PUT called with id: ' + str(id))
    account = Account.query.get(id)
    account.name = request.json['name']
    db.session.commit()
    return format_account(account)

@app.route('/accounts/<int:id>', methods=['DELETE'])
def delete_account(id):
    app.logger.debug('Route /accounts DELETE called with id: ' + str(id))
    account = Account.query.get(id)
    db.session.delete(account)
    db.session.commit()
    return format_account(account)

def format_account(account):
    return {
        'id': account.id,
        'name': account.name,
        'account_number': account.account_number,
        'balance': account.balance,
        'currency': account.currency,
        'country': account.country,
        'status': account.status,
        'created_at': account.created_at
    }
from app import db
from app.accounts import constants as ACCOUNTS
import datetime
# Account Model
#     Name
#     Start Balance
#     Type            Current/Savings/Credit Card/Loan
#     Interest
#     Overdraft INterest


class Account(db.Model):

    __tablename__ = 'accounts_account'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    type = db.Column(db.String(50), default=ACCOUNTS.DEFAULTTYPE)
    creditInterest = db.Column(db.SmallInteger(50), default=0)
    debitInterest = db.Column(db.SmallInteger(50), default=0)
    transactions = db.relationship('Transactions', backref='accounts', lazy='dynamic')
    # atsome point this needs to be varialble based upon type
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(50), unique=True)
    # email = db.Column(db.String(120), unique=True)
    # password = db.Column(db.String(20))
    # role = db.Column(db.SmallInteger, default=USER.USER)
    # status = db.Column(db.SmallInteger, default=USER.NEW)

    def __init__(self, name=None, type=ACCOUNTS.DEFAULTTYPE, creditInterest=0, debitInterest=0):
        self.name = name
        self.type = type
        self.creditInterest = creditInterest
        self.debitInterest = debitInterest

    def __repr__(self):
        return '<User %r>' % (self.name)


class Transactions(db.Model):
    __tablename__ = 'transactions_transaction'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts_account.id'))
    destination_id = db.Column(db.Integer, default=0)
    name = db.Column(db.String(50), unique=True)
    debit = db.Column(db.Float(3), unique=True)
    credit = db.Column(db.Float(3), unique=True)

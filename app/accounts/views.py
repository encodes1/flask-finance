from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.accounts.models import Account

mod = Blueprint('account', __name__, url_prefix='/accounts')


@mod.route('/account/', methods=['GET', 'POST'])
def login():
  Account(name="test")
  print Account

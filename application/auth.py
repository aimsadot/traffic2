from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html", page_type='login')


@auth.route('/logout')
def logout():
    pass


@auth.route('/add-new-user')
def sign_up():
    return render_template("sign-up.html", page_type='register')

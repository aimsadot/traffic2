from flask import Blueprint, render_template, flash

view = Blueprint('view', __name__)


@view.route('/')
def home():
    flash('Check Errror', category='error')
    flash('Check Succ', category='success')
    return render_template("home.html")


@view.route('/settings')
def settings():
    return render_template("settings.html")

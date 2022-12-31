from flask import Blueprint, render_template, request, flash
from flask_login import login_required

from . import FLASH_ERROR, FLASH_SUCCESS

view = Blueprint('view', __name__)


@view.route('/')
@login_required
def home():
    return render_template("home.html")


@view.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        mod = request.form.get('mod')
        if 'file' in request.form:
            print('Yes')
        add_dic = {}
        for item in request.form:
            add_dic['item'] = request.form.get(item)

        flash('mod is ' + request.form.get('mod'), category=FLASH_SUCCESS)
    return render_template("settings.html", areas=[])

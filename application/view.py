from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required

from . import FLASH_ERROR, FLASH_SUCCESS
from .businessLogic import *

view = Blueprint('view', __name__)


@view.route('/')
@login_required
def home():
    return render_template("home.html")


@view.route('/area-list')
@login_required
def area_list():
    return jsonify(list_area())


@view.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        mod = request.form.get('mod')
        if 'file' in request.form:
            print('Yes')
        add_dic = {}
        for item in request.form:
            add_dic[item] = request.form.get(item)
        error, msg = add_operations(mod, add_dic)
        return jsonify({
            'error': error,
            'msg': msg
        })
    return render_template("settings.html", areas=list_area())

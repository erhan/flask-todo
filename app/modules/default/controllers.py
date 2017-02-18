from flask import Blueprint, render_template

module = Blueprint('default', __name__)


@module.route('/')
def index():
    return render_template('default/index.html')
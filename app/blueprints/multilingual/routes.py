from flask import render_template, Blueprint
from app import app

multilingual = Blueprint('multilingual', __name__, template_folder='templates')

@multilingual.route('/')
@multilingual.route('/index')
def index():
    user = { 'name': 'Francisco'}
    return render_template('multilingual/index.html', user = user)
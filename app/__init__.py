from flask import Flask, request, g, redirect, url_for, jsonify
from flask_babel import Babel
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


from app.blueprints.multilingual import multilingual
app.register_blueprint(multilingual)


babel = Babel(app)

@babel.localeselector
def get_locale():
    if not g.get('lang_code', None):
        g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return g.lang_code

@app.route('/')
def home():
    g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return redirect(url_for('multilingual.index'))

@app.route('/validate', methods=["POST"])
def validate():
    
    code = request.form['code']

    f = open("./logic/code.bas", "w+")
    f.write(code)

    print(code)

    return jsonify(True)
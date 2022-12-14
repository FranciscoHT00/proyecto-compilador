from flask import Flask, request, g, redirect, url_for, jsonify
from flask_babel import Babel
from config import Config
from logic.compiler import logic

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

@app.route('/run', methods=["POST"])
def validate():
    
    code = request.form['code']

    logic.updateFile(code)

    result = logic.runCode()

    print(result)
    
    return jsonify(result)
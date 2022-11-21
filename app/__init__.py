from flask import Flask, request, g
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
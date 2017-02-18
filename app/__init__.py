from flask import Flask, render_template
from flask import session
from flask_sqlalchemy import SQLAlchemy
from config import configuration
from flask_bootstrap import Bootstrap
from flask import g
from app.helpers import filters

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(configuration.__dict__)
db = SQLAlchemy(app)
Bootstrap(app)

from app.models import User

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.filter(User.id == session["user_id"]).first()


@app.after_request
def after_request(response):
    return response


@app.errorhandler(Exception)
def server_error(error):
    print(error)
    return render_template('500.html'), 500


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.modules.default.controllers import module as default
from app.modules.user.controllers import module as user
from app.modules.todo.controllers import module as todo


app.register_blueprint(default)
app.register_blueprint(user)
app.register_blueprint(todo)
app.register_blueprint(filters.blueprint)

db.create_all()
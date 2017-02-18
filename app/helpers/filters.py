import flask
from flask import url_for
import jinja2
import urllib, hashlib

blueprint = flask.Blueprint('filters', __name__)


@jinja2.evalcontextfilter
def gravatar_filter(eval_ctx, value):
    '''Email alıp gravatardan o emaile ait profil resmini çeken eğer yoksa default profil resmi dönen custom jinja filter.'''
    email = value
    default = url_for('static', filename='img/profile.png', _external= True)
    size = 100
    gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower().encode('utf-8')).hexdigest() + "?"
    gravatar_url += urllib.parse.urlencode({'d': default, 's': str(size)})
    return gravatar_url


#oluşturduğumuz filtreleri blueprint ile ekliyoruz.
blueprint.add_app_template_filter(gravatar_filter)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    '''Todo ekleme formu'''
    description = StringField('Yapılacak iş', [DataRequired("Yapılacak iş alanı boş geçilemez")])
    submit = SubmitField('Kaydet')
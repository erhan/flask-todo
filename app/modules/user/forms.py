from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, HiddenField
from wtforms.validators import Email, DataRequired


class LoginForm(FlaskForm):
    '''Kullanıcı giriş formu'''
    email = StringField('E-posta', [Email("Hatalı e-posta formatı."), DataRequired("E-posta alanı boş geçilemez")])
    password = PasswordField('Şifre', [DataRequired("Şifre alanı boş geçilemez")])
    submit = SubmitField('Giriş')


class RegisterForm(FlaskForm):
    '''Kullanıcı kayıt formu'''
    full_name = StringField('Ad Soyad', [DataRequired("Ad Soyad alanı boş geçilemez")])
    email = StringField('E-posta', [Email("Hatalı e-posta formatı."), DataRequired("E-posta alanı boş geçilemez")])
    password = PasswordField('Şifre', [DataRequired("Şifre alanı boş geçilemez")])
    submit = SubmitField('Kayıt')


class EditForm(FlaskForm):
    '''Kullanıcı düzenleme formu'''
    full_name = StringField('Ad Soyad', [DataRequired("Ad Soyad alanı boş geçilemez")])
    password = PasswordField('Şifre', [DataRequired("Şifre alanı boş geçilemez")])
    submit = SubmitField('Düzenle')
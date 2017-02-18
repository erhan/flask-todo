from flask import Blueprint, render_template, request, redirect, url_for, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from app.helpers.decarators import login_required
from app.models import User
from app.modules.user.forms import LoginForm, RegisterForm, EditForm
from app import db

module = Blueprint('user', __name__, url_prefix='/kullanici')


@module.route('/kayit', methods=['GET', 'POST'])
def register():
    '''Email kontrolü yapıp daha önceden kayıt olmamış kullanıcıları kaydeder.'''
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter(User.email == form.email.data).first()
        if user:
            flash("Bu kullanıcı mevcut", 'error')
            return render_template('user/register.html', form=form)
        user = User(form.full_name.data, form.email.data, generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        flash('Kayıt Olduğunuz İçin Teşekkürler', 'success')
        return redirect(url_for('user.login'))
    return render_template('user/register.html', form=form)


@module.route('/giris', methods=['GET', 'POST'])
def login():
    '''Kullanıcı giriş methodu giriş başarılıysa giriş yapan kullanıcı sessionda tutar.'''
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter(User.email == form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Başarılı giriş', 'success')
            return redirect(url_for('todo.index'))
        flash("Email veya şifre hatası.", 'error')
    return render_template('user/login.html', form=form)


@module.route('/cikis')
@login_required
def logout():
    '''Sessioni silip kullanıcıyı logout eder.'''
    session.pop('user_id', None)
    return redirect(url_for('user.login'))


@module.route('/duzenle', methods=['GET', 'POST'])
@login_required
def edit():
    '''Giriş yapan kullanıcı bilgilerini düzenler.'''
    form = EditForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter(User.id == g.user.id).first()
        user.full_name = form.full_name.data
        user.password = generate_password_hash(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Bilgileriniz Düzenlendi.', 'success')
        return redirect(url_for('user.edit'))
    form.full_name.data = g.user.full_name
    return render_template('user/edit.html', form=form)
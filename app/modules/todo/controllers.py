from flask import Blueprint, render_template, g, request, redirect, url_for, flash
from sqlalchemy import and_
from app.helpers.decarators import login_required
from app.models import Todo
from app.modules.todo.forms import TodoForm
from app import db

module = Blueprint('todo', __name__, url_prefix='/todo')


@module.route('/', methods=['GET', 'POST'])
@login_required
def index():
    '''Kullanıcıya ait silinmemiş todoları listeleyip post methoduyla'da yeni todo eklenmesini sağlar.'''
    todos = Todo.query.filter(Todo.owner_id == g.user.id).filter(Todo.status >= 0). \
        order_by(Todo.status, Todo.date_created.desc()).all()
    form = TodoForm(request.form)
    if request.method == 'POST' and form.validate():
        todo = Todo(form.description.data, 0, g.user.id)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for("todo.index"))
    return render_template("todo/index.html", todos=todos, form=form)


@module.route('/change-status/<int:todo_id>/<int:status>', methods=['GET'])
@login_required
def change_status(todo_id = 0, status = 1):
    '''Parametre olarak gelen todo_id ve status ile kullanıcıya ait işin statu durumunu değiştirir.'''
    todo = Todo.query.filter(and_(Todo.owner_id == g.user.id, Todo.id == todo_id)).first_or_404()
    #TODO:Status kontolü yapılmalı.
    todo.status = status
    db.session.add(todo)
    db.session.commit()
    flash('Durum değiştirildi.', 'success')
    return redirect(url_for("todo.index"))



@module.route('/delete/<int:todo_id>', methods=['GET'])
@login_required
def delete(todo_id = 0):
    '''Kullanıcıya ait todo'yu siler.'''
    todo = Todo.query.filter(and_(Todo.owner_id == g.user.id, Todo.id == todo_id)).first_or_404()
    db.session.delete(todo)
    db.session.commit()
    flash('Kayıt Silindi.', 'success')
    return redirect(url_for("todo.index"))
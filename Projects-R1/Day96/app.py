import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    completed = db.Column(db.Boolean, default=False)


@app.route('/')
def index():
    todo_items = TodoItem.query.all()
    return render_template('base.html', todo_items=todo_items)


@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form['title']
    todo_item = TodoItem(title=title)
    db.session.add(todo_item)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/complete/<int:id>')
def complete_todo(id):
    todo_item = TodoItem.query.filter_by(id=id).first()
    todo_item.completed = True
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete_todo(id):
    todo_item = TodoItem.query.filter_by(id=id).first()
    db.session.delete(todo_item)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

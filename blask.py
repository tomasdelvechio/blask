from flask import Flask, render_template, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

from lib.config import version, fecha, author
from model import db, Post

app = Flask(__name__)
db.create_all()

@app.template_filter('datetimeformat')
def format_datetime(value, format='%H:%M / %d-%m-%Y'):
    val = datetime.strptime(value, '%Y-%m-%d')
    return val.strftime(format)

@app.route("/")
def index():
    #~ print url_for('static', filename='style.css')
    #~ @app.route('/', methods=['GET'])
    
    posts = Post.query.all()
    
    data = {'version': version(), 'date': fecha(), 'posts': posts, 'author': author()}
    return render_template('index.html',**data)

if __name__ == "__main__":
    app.debug = True
    app.run()


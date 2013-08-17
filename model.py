from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

# App config #
##############
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/blask.db'
db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, db.Sequence('post_id_seq'), primary_key=True)
    title = db.Column(db.String())
    article = db.Column(db.String())
    date = db.Column(db.String())

    def __init__(self, title, article):
        self.title = title
        self.article = article
        self.date = datetime.strftime(datetime.now())
        self.date = datetime.today().strftime('%Y-%M-%d')

    def __repr__(self):
        return "<Post('%s','%s', '%s')>" % (self.title, self.article, self.date)

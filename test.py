from datetime import datetime

import flask_sqlalchemy
import flask_whooshalchemy
from whoosh.analysis import StemmingAnalyzer

db = flask_sqlalchemy.SQLAlchemy()

class BlogPost(db.Model):
    __tablename__ = 'posts'
    __searchable__ = ['title', 'content', 'summary']  # indexed fields
    __analyzer__ = StemmingAnalyzer()
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    content = db.Column(db.Text(32*1024))
    summary = db.Column(db.String(1024))
    created = db.Column(db.DateTime, default=datetime.utcnow)

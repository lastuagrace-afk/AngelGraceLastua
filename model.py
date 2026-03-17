from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    section = db.Column(db.String(100), nullable=False)

class RepositoryLanguage(db.Model):
    __tablename__ = 'repository_languages'
    id = db.Column(db.Integer, primary_key=True)
    repo_name = db.Column(db.String(255), nullable=False)
    language_name = db.Column(db.String(100), nullable=False)
    percentage = db.Column(db.Float, nullable=False)

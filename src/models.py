from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_of_birth = db.Column(db.TIMESTAMP, nullable=False)
    job = db.Column(db.String(80), nullable=True)

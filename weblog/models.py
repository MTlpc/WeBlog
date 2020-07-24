from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# 角色表映射类
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role: {}>'.format(self.name)


# 用户表映射类
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User: {}>'.format(self.name)
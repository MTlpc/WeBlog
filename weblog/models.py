from flask_sqlalchemy import SQLAlchemy
# 导入密码散列包
from werkzeug.security import generate_password_hash, check_password_hash


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
    email = db.Column(db.String(64), unique=True, index=True)
    _password = db.Column('password', db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref=db.backref('users', lazy='dynamic'))
    
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        self._password = generate_password_hash(pwd)

    # 验证用户密码
    def verify_password(self, pwd):
        return check_password_hash(self._password, pwd)

    def __repr__(self):
        return '<User: {}>'.format(self.name)
from datetime import datetime
from flask import Blueprint, url_for, redirect, flash, abort, request, session
from flask import render_template, current_app, make_response
from flask_login import login_required, login_user, logout_user, current_user

from ..forms import RegisterForm, LoginForm
from ..models import db, User


# 创建蓝图
front = Blueprint('front', __name__)


# 创建首页视图函数
@front.route('/')
def index():
    date_time = datetime.utcnow()
    return render_template('index.html', date_time=date_time)


# 注册函数
@front.route('/register', methods=['POST', 'GET'])
def register():
    '''用户注册'''
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data,
                password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('你已经注册成功，请登录', 'success')
        # 重定向到登录页面
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)


# 登录函数
@front.route('/login', methods=['POST', 'GET'])
def login():
    '''用户登录'''
    if current_user.is_authenticated:
        flash('你已经处于登录状态。', 'info')
        return redirect(url_for('.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash('你已经登录成功，{}！'.format(user.name), 'success')
            return redirect(url_for('.index'))
        flash('邮箱或密码错误', 'warning')
    return render_template('login.html', form=form)


# 退出登录
@front.route('/logout')
def logout():
    '''退出登录'''
    logout_user()
    flash('你已经退出登录', 'info')
    return redirect(url_for('.index'))

# 这里使用的是 app_errorhandler ，它使得该函数对全应用中的视图函数均有效
@front.app_errorhandler(404)
def page_not_found(e):
    '''路由错误，不存在该页面'''
    return render_template('404.html'), 404


@front.app_errorhandler(500)
def inter_server_error(e):
    '''服务器内部错误'''
    return render_template('500.html'), 500
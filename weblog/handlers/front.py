from flask import Blueprint
from flask import render_template
from datetime import datetime


# 创建蓝图
front = Blueprint('front', __name__)


# 创建首页视图函数
@front.route('/')
def index():
    date_time = datetime.utcnow()
    return render_template('index.html', date_time=date_time)


# 这里使用的是 app_errorhandler ，它使得该函数对全应用中的视图函数均有效
@front.app_errorhandler(404)
def page_not_found(e):
    '''路由错误，不存在该页面'''
    return render_template('404.html'), 404


@front.app_errorhandler(500)
def inter_server_error(e):
    '''服务器内部错误'''
    return render_template('500.html'), 500
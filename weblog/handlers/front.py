from flask import Blueprint
from flask import render_template


# 创建蓝图
front = Blueprint('front', __name__)


# 创建首页视图函数
@front.route('/')
def index():
    return render_template('index.html')
#encoding=utf8
from flask import Flask
from flask_bootstrap import Bootstrap
# 时间日期本地化
from flask_moment import Moment

from .handlers import blueprint_list
from .configs import configs
# 数据库Model类
from .models import db, Role, User

def register_blueprints(app):
    for bp in blueprint_list:
        app.register_blueprint(bp)

# 创建flask入口
def create_app(config):
    app = Flask(__name__)

    Bootstrap(app) 
    register_blueprints(app)
    # 注册配置类
    app.config.from_object(configs.get(config))
    # 注册实体类
    db.init_app(app)

    return app
#encoding=utf8
from flask import Flask
from flask_bootstrap import Bootstrap
# 时间日期本地化
from flask_moment import Moment

from .handlers import blueprint_list
from .configs import configs
# 数据库Model类
from .models import db, Role, User
# 数据库迁移类
from flask_migrate import Migrate 
# 解决MySQL_DB不存在的问题
import pymysql
pymysql.install_as_MySQLdb()

# 注册蓝图
def register_blueprints(app):
    for bp in blueprint_list:
        app.register_blueprint(bp)


# 扩展flask
def register_extensions(app):
    # 添加Python-BootStrap
    Bootstrap(app)
    # 注册实体类
    db.init_app(app)
    # 时间日期本地化
    Moment(app)
    # 数据库迁移
    Migrate(app, db) 


# 创建flask入口
def create_app(config):
    app = Flask(__name__)
    # 注册配置类
    app.config.from_object(configs.get(config))
    register_extensions(app)
    # 注册蓝图
    register_blueprints(app)

    return app
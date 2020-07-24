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
# 登录功能
from flask_login import LoginManager
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
    # 登录功能
    login_manager = LoginManager() 
    login_manager.init_app(app)

    # 该方法会被动执行，查找用户将其设为已登录状态
    @login_manager.user_loader
    def user_loader(id):
        # 只有主键才可以使用 query.get 方法查询
        return User.query.get(id)

    # 未登录状态下访问需要登录后才能访问的页面时，自动跳转到此路由
    login_manager.login_view = 'front.login'
    # 提示信息的内容和类型
    login_manager.login_message = '你需要登录之后才能访问该页面'
    login_manager.login_message_category = 'warning'
    
# 创建flask入口
def create_app(config):
    app = Flask(__name__)
    # 注册配置类
    app.config.from_object(configs.get(config))
    register_extensions(app)
    # 注册蓝图
    register_blueprints(app)

    return app
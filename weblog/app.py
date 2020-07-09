#encoding=utf8
from flask import Flask
from flask_bootstrap import Bootstrap
from .handlers import blueprint_list

def register_blueprints(app):
    for bp in blueprint_list:
        app.register_blueprint(bp)

# 创建flask入口
def create_app():
    app = Flask(__name__)

    Bootstrap(app) 
    register_blueprints(app)

    return app
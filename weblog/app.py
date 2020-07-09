#encoding=utf8
from flask import Flask

# 创建flask入口
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello World'

    return app
import os


class BaseConfig:
    '''
    基础配置类，存储公共配置项
    '''

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asdfasdf'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    '''
    开发阶段使用的配置类
    '''

    # 这是设置连接数据库的配置项
    url = 'mysql://root{}@localhost/weblog?charset=utf8'
    pwd = os.environ.get('MYSQL_PWD')
    pwd = ':{}'.format(pwd) if pwd else ''
    SQLALCHEMY_DATABASE_URI = url.format(pwd)


class TestConfig(BaseConfig):
    '''
    测试阶段使用的配置类
    '''

    pass


# 配置类字典，便于 app.py 文件中的应用调用
configs = {
    'dev': DevConfig,
    'test': TestConfig
}
#coding:utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__)) #获取文件绝对路径

class Config:
    #配置类的基类，没有直接或间接地子类化一个对象，即定义的是经典类，config 实际上继承于字典，并且可以像修改字典一样修改它，来自于flask框架
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    #密匙，定义成环境设定或者使用此默认值‘hard to guess string’
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True#每次request自动提交db.session.commit()
    MAIL_SERVER = 'smtp.163.com'
    #电子邮件服务器的主机名或IP地址
    MAIL_PORT = 25
    #电子邮件服务器的端口
    MAIL_USE_TLS = True
    #启用传输层安全协议Transport Layer Security，网易推荐SSL
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    #从环境获取的邮件账户和密码
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flask]'
    #邮件主题的前缀
    FLASKY_MAIL_SENDER = 'b1a2b3c4d@163.com'
    #此变量在email.py里被send_email调用
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    #send_email的两个程序特定配置项分别定义邮件主题的前缀和发件人的地址
    @staticmethod
    def init_app(app):
    #名叫init_app的类方法执行对当前配置的初始化，参数为程序实例app现在方法为空
        pass
        
class DevelopmentConfig(Config):
    DEBUG = True   
    SQLALCHEMY_DATABASSE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASSE_URI = os.environ.get('TEST_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    
class ProductionCofig(Config):
    SQLALCHEMY_DATABASSE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'data.sqlte')
    #以上分别定义了三种配置环境下的数据库
    
config = {
    'development': DevelopmentConfig, 
    'testing': TestingConfig,
    'production': ProductionCofig,
    'default': DevelopmentConfig    }
    #注册了不同的配置环境，语法上不明白是怎么回事

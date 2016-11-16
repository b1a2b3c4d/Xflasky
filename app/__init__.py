<<<<<<< HEAD
#coding:utf-8
#__init__文件为构造文件
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
#提供不同的安全等级防止用户会话遭篡改
login_manager.login_view = 'auth.login'
#login_view 属性设置登录页面的端点

def create_app(config_name):#工厂函数，接受的参数是程序使用的配置名
    app = Flask(__name__)
    #创建程序
    app.config.from_object(config[config_name])
    #使用 Flask app.config 配置对象提供的 from_object() 方法直接将定义在cofing.py中的配置类导入程序
    config[config_name].init_app(app)
    #将程序配置好
    bootstrap.init_app(app)
    mail.init_app(app)    
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    #初始化扩展
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)#将蓝本main注册到程序上
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')#将蓝本auth注册到程序上，url_prefix是可选参数。使用了之后蓝本（blueprint）中定义的所有路由都会加上指定的前缀，即这个例子中的 /auth。
    
=======
#coding:utf-8
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_pagedown import PageDown

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    # 附加路由和自定义的错误页面

    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask.ext.sslify import SSLify
        sslify = SSLify(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

>>>>>>> banch17.4.3
    return app
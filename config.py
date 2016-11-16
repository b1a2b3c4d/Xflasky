<<<<<<< HEAD
#coding:utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__)) #��ȡ�ļ�����·��

class Config:
    #������Ļ��࣬û��ֱ�ӻ��ӵ����໯һ�����󣬼�������Ǿ����࣬config ʵ���ϼ̳����ֵ䣬���ҿ������޸��ֵ�һ���޸�����������flask���
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    #�ܳף�����ɻ����趨����ʹ�ô�Ĭ��ֵ��hard to guess string��
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True#ÿ��request�Զ��ύdb.session.commit()
    MAIL_SERVER = 'smtp.163.com'
    #�����ʼ�����������������IP��ַ
    MAIL_PORT = 25
    #�����ʼ��������Ķ˿�
    MAIL_USE_TLS = True
    #���ô���㰲ȫЭ��Transport Layer Security�������Ƽ�SSL
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    #�ӻ�����ȡ���ʼ��˻�������
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flask]'
    #�ʼ������ǰ׺
    FLASKY_MAIL_SENDER = 'b1a2b3c4d@163.com'
    #�˱�����email.py�ﱻsend_email����
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    #send_email�����������ض�������ֱ����ʼ������ǰ׺�ͷ����˵ĵ�ַ
    @staticmethod
    def init_app(app):
    #����init_app���෽��ִ�жԵ�ǰ���õĳ�ʼ��������Ϊ����ʵ��app���ڷ���Ϊ��
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
    #���Ϸֱ������������û����µ����ݿ�
    
config = {
    'development': DevelopmentConfig, 
    'testing': TestingConfig,
    'production': ProductionCofig,
    'default': DevelopmentConfig    }
    #ע���˲�ͬ�����û������﷨�ϲ���������ô����
=======
#coding:utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[XFlasky]'
    FLASKY_MAIL_SENDER = 'b1a2b3c4d@163.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 20
    FLASKY_COMMENTS_PER_PAGE = 20
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_DB_QUERY_TIMEOUT = 0.5
    SSL_DISABLE = True
    
    @staticmethod
    def init_app(app):
        pass
        
        
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email errors to the administrators
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.FLASKY_MAIL_SENDER,
            toaddrs=[cls.FLASKY_ADMIN],
            subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

class HerokuConfig(ProductionConfig):
    SSL_DISABLE = bool(os.environ.get('SSL_DISABLE'))

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # handle proxy server headers
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'default': DevelopmentConfig
}
>>>>>>> banch17.4.3

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

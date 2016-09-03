#coding:utf-8
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager


class Role(db.Model):
    __tablename__ = 'roles'#定义在数据库中使用的表名
    id = db.Column(db.Integer, primary_key=True)
    #db.Column类第一个参数是数据库列和模型属性的类型，其余是指定属性的配置选项
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role',lazy='dynamic')
    #对于Role实例，users属性将返回与角色相关的用户组成的列表，第一个参数表明这个关系的另一端是哪个模型，backref向User模型中添加了一个role属性，从而定义反向关系
    def __repr__(self):#返回一个可读的字符串表示模型
        return '<Role %r>' % self.name
    
        
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64),unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#role_id被定义为外键，建立起关系    
    password_hash = db.Column(db.String(128))
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):#计算密码散列值的函数通过名为 password 的只写属性实现
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):#verify_password方法接受一个参数（即密码），将其传给Werkzeug提供的check_password_hash()函数，和存储在User模型中的密码散列值进行比对。
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    #加载用户的回调函数接收以 Unicode 字符串形式表示的用户标识符。如果能找到用户，这个函数必须返回用户对象；否则应该返回 None
       
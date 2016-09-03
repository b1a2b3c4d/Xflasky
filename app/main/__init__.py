#coding:utf-8
from flask import Blueprint
#此子包main 用于保存和创建蓝本
main = Blueprint('main', __name__)
#两个参数，蓝本的名字和蓝本所在的包或模块
from . import views, errors
#蓝本中定义的路由和和错误处理程序
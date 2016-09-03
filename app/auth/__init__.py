#coding:utf-8
from flask import Blueprint
#创建认证蓝本
auth = Blueprint('auth', __name__)

from . import views

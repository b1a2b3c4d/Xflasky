#coding:utf-8
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)

#上下文处理器app_context_processor能让变量在所有模板中全局可访问。


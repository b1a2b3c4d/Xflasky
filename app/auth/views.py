#coding:utf-8
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth #引入认证蓝本
from ..models import User
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])#访问login的url，能够处理GET和POST请求
def login():
    form = LoginForm()
    if form.validate_on_submit():#POST请求中提交表单时验证表单数据
        user = User.query.filter_by(email=form.email.data).first()
        #首先使用email从数据库中加载用户
        if user is not None and user.verify_password(form.password.data):#判断用户是否存在和密码是否正确
            login_user(user, form.remember_me.data)
            #参数为用户和记住我的布尔值
            return redirect(request.args.get('next') or url_for('main.index'))
            #url含义<协议>://<域名>/<接口>?<键1>=<值1>&<键2>=<值2>

        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)#此模板文件应创建在app/templates中，为了避免与main或其他蓝本发生模板命名冲突应保存在单独的文件夹里


@auth.route('/logout')
@login_required#限制登陆用户才能访问
def logout():
    logout_user()
    #为了登出用户
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
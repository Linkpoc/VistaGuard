import os

from app.home import home
from flask import render_template, request, redirect, url_for, flash, session

# urllib 需要手动构建HTTP请求，flask.request 包含基本的请求信息
@home.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '1':
            return redirect(url_for('home.index'))
        else:
            user_id = username
            session['user_id'] = user_id
            # 不知道为什么这里用flash登录时会报错
            flash(user_id+'登陆失败，账号或密码错误！！！')
            return render_template('login.html')

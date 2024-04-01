from app.home import home
from flask import render_template, request, redirect, url_for, flash, session
from app.model.models import (
    Log,db,User
)

# urllib 需要手动构建HTTP请求，flask.request 包含基本的请求信息
def setcookie(name, value, expires):
    pass

def save_log(ip, username, passwd, boolcheck):
    log = Log(ip=ip, username=username, passwd=passwd, boolcheck=boolcheck)
    db.session.add(log)
    db.session.commit()

@home.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        passwd = request.form.get('passwd')

        user = User.query.filter(User.username == username).first()
        save_log(request.remote_addr, username, passwd, user.check_password(passwd) if user else False)
        # print(user.check_password(passwd))
        if user and user.check_password(passwd):
            session['user_id'] = user.id
            return redirect(url_for('home.index'))
        else:
            flash('登陆失败，账号或密码错误！！！')
            return render_template('login.html')

def test():
    print('hi')


if __name__ == '__main__':
    test()

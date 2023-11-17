import os

from flask import Flask, render_template, url_for, redirect
from app.home import home


app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
#调试模式，检测到模板变化时自动重新加载模板
app.config['SECRET_KEY'] = os.urandom(24)
#不可以在蓝图中定义，SECRET_KEY只会对当前应用实例生效，不会对整个应用生效。

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

app.register_blueprint(home)


@app.route('/')
def testinfo():
    return redirect(url_for('home.login'))

if __name__ == '__main__':
    app.run()
import os

from flask import Flask, render_template, url_for, redirect
from app.home import home
from app.plugin import plugin
from app.tasks import tasks
from app.vuls import vuls
from app.pocs import pocs

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
#调试模式，检测到模板变化时自动重新加载模板
app.config['SECRET_KEY'] = os.urandom(24)
#不可以在蓝图中定义，SECRET_KEY只会对当前应用实例生效，不会对整个应用生效。

from app.config import baseconfig
from flask_sqlalchemy import SQLAlchemy

app.config.from_object(baseconfig)

db = SQLAlchemy(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

app.register_blueprint(home)
app.register_blueprint(tasks)
app.register_blueprint(vuls)
app.register_blueprint(pocs)
app.register_blueprint(plugin)

# app.config.from_pyfile('.\\app\\config\\baseconfig.py')

@app.route('/')
def testinfo():
    return redirect(url_for('home.login'))

if __name__ == '__main__':
    app.run()

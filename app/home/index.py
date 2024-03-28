from flask import render_template

from app.home import home


@home.route('/index/')
def index():
    return render_template('index.html')

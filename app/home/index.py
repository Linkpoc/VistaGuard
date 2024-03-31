from flask import render_template

from app.home import home
from app.utils.decorators import login_required


@home.route('/index/')
@login_required
def index():
    return render_template('index.html')

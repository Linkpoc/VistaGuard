from app.home import home


@home.route('/index/')
def index():
    return 'index'

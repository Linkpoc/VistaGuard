
from app.home import home
from flask import (
    redirect, url_for, session
)
# from app.utils.decorators import login_required


@home.route('/logout/')
# @login_required
def logout():
    session.clear()
    return redirect(url_for('home.login'))

def test():
    print('hi')


if __name__ == '__main__':
    test()

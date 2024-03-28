from flask import Blueprint

home = Blueprint('home', __name__)

from . import index
from . import login
from . import logout

def test():
    print('hi')


if __name__ == '__main__':
    test()
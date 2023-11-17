from flask import Blueprint

home = Blueprint('home', __name__)

from . import index
from . import login

def test():
    print('hi')


if __name__ == '__main__':
    test()
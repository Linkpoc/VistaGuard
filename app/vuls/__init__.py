
from flask import (
    Blueprint
)

vuls = Blueprint('vuls', __name__)

from . import vullist

def test():
    print('hi')


if __name__ == '__main__':
    test()

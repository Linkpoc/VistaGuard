
from flask import (
    Blueprint
)

pocs = Blueprint('pocs', __name__)

from . import poclist
def test():
    print('hi')


if __name__ == '__main__':
    test()

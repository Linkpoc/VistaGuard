from flask import Blueprint

tasks = Blueprint('tasks', __name__)

from . import tasklist

def test():
    print('hi')


if __name__ == '__main__':
    test()

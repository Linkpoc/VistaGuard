
import logging
import os

from app.utils.decorators import login_required
from app.pocs import pocs
from flask import (
    render_template, redirect, url_for, flash, request
)
from werkzeug.utils import secure_filename
from app.model.models import (
    PocList
)
from app.model.exts import db
from init import app
from app.config import baseconfig


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in baseconfig.ALLOWED_EXTENSIONS



@pocs.route('/pocs/')
@pocs.route('/pocs/<int:page>', methods=['GET'])
@login_required
def poclist(page=1,msg=None):
    return render_template('poclist.html')


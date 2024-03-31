import logging
import os

from werkzeug.utils import secure_filename

from app.utils.decorators import login_required
from app.plugin import plugin
from flask import (
    render_template, redirect, url_for, flash, request
)
from app.model.models import (
    pluginList
)
from app.model.exts import db
from init import app
from app.config import baseconfig


@plugin.route('/plugin/')
@plugin.route('/plugin/<int:page>', methods=['GET'])
@login_required
def pluginlist(page=1,msg=None):

    return render_template('pluginlist.html')


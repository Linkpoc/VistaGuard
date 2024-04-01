from flask import request

from flask import render_template

from app.home import home
from app.model.models import BaseInfo, PocList, VulList, pluginList, Log
from app.utils.decorators import login_required


@home.route('/home/<int:page>', methods=['GET', 'POST'])
@home.route('/home/', methods=['GET', 'POST'])
@home.route('/', methods=['GET', 'POST'])
@login_required
def index(page=1):
    # if not request.args.get('page'):
    #     page=1
    # else:
    #     page = int(request.args.get('page'))
    if not page:
        page = 1
    paginate = Log.query.order_by(Log.date.desc()).paginate(page=page, per_page=10, error_out=False)
    logs = paginate.items

    result={
        'targets':len(BaseInfo.query.all()),
        'pocs':len(PocList.query.all()),
        'vuls':len(VulList.query.all()),
        'plugins':len(pluginList.query.all())
    }
    return render_template('index.html', pagination=paginate,result=result,logs=logs)
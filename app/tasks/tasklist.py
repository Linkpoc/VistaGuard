
from app.tasks import tasks
from flask import render_template

from app.utils.decorators import login_required


@tasks.route('/tasks/')
@tasks.route('/tasks/<int:page>', methods=['GET'])
@login_required
def tasklist(page=1,msg=None):
    # return render_template('tasklist.html')
    # 假设每页显示 10 条数据
    PER_PAGE = 10

    # 假设总共有 100 条数据
    total_items = 100

    # 假设当前页码为 1
    current_page = 1

    # 计算总页数
    total_pages = (total_items + PER_PAGE - 1) // PER_PAGE

    # 构造一个假的分页对象
    paginate = {
        'page': current_page,
        'total': total_items,
        'pages': total_pages,
        'has_prev': current_page > 1,
        'has_next': current_page < total_pages
    }
    vuls = 'test'
    return render_template('tasklist.html', pagination=paginate, vuls=vuls)


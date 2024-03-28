from app.vuls import vuls
from app.model.models import (
    VulList
)
from flask import (
    render_template
)
from app.utils.decorators import login_required
# 定义一个简单的数据列表，假设有 100 条数据
data = [f'Item {i+1}' for i in range(100)]
@vuls.route('/vuls/')
@vuls.route('/vuls/<int:page>', methods=['GET'])
@login_required
def vullist(page=1):
    PER_PAGE = 10  # 每页显示 10 条数据

    # 计算总页数
    total_pages = (len(data) + PER_PAGE - 1) // PER_PAGE

    # 构造分页对象
    pagination = {
        'page': page,
        'total': len(data),
        'pages': total_pages,
        'has_prev': page > 1,
        'has_next': page < total_pages
    }

    # 获取当前页数据
    start_index = (page - 1) * PER_PAGE
    end_index = start_index + PER_PAGE
    vuls = data[start_index:end_index]

    return render_template('vullist.html', pagination=pagination, vuls=vuls)
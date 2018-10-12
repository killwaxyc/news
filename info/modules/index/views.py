from info.modules.index import index_blu
from manage import app
from flask import render_template, current_app


@index_blu.route('/')
def index():
    return render_template('news/index.html')


@index_blu.route('/favicon.ico')
def favicon():
    # send_static_file 是系统访问静态文件所调用的方法
    return current_app.send_static_file('news/favicon.ico')

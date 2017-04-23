# -*- coding:utf-8 -*-
import os
import platform
import re

from flask import Flask, Response

from blueprints.admin import admin
from blueprints.user import user
from utils.config import get_config
from utils.db_connection import engine
from utils.errors.base_error import BaseError
from utils.serializer import obj_to_json

app = Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.register_blueprint(admin.routes, url_prefix='/admin')
app.register_blueprint(user.routes, url_prefix='/user')


@app.route('/')
def index():
    string = get_config()['database']['url']
    if string is None:
        db_path = "No Database configuration..."
    else:
        db_path = re.search('(?<=@).*', string).group(0)
    return """
        <h1>Server started...</h1>
        <h2>Python version: %s<h2>
        <h2>Database: %s</h2>
    """ % (platform.python_version(), db_path)


@app.route('/system')
def system():
    output = os.popen('cat /proc/cpuinfo')
    return output.read()


@app.route('/db')
def db_status():
    """
    Lei, HUANG: 11:53 16/04/2017
    :return:返回当前数据库连接池状态 
    """
    return engine.pool.status()


@app.errorhandler(BaseError)
def generic_error_handler(error):
    """
    Lei, HUANG: 15:47 23/04/2017
    负责处理所有BaseError的异常子类
    :param error: 
    :return: 
    """
    response = obj_to_json(error.to_dict())
    return Response(mimetype='application/json', status=error.status_code, response=response)


if __name__ == '__main__':
    app.secret_key = get_config()['app_secret']
    app.run(host='0.0.0.0', debug=True)

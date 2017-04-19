# -*- coding:utf-8 -*-
import os
import platform
import re

from flask import Flask

from blueprints.admin import admin
from blueprints.user import user_actions
from utils.config import get_config

app = Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.register_blueprint(admin.admin, url_prefix='/admin')
app.register_blueprint(user_actions.user_module, url_prefix='/user')


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


if __name__ == '__main__':
    app.secret_key = get_config()['app_secret']
    app.run(host='0.0.0.0')

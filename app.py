# -*- coding:utf-8 -*-

from flask import Flask
from flask import jsonify
from blueprints.user import user_actions
from blueprints.admin import admin
from utils.Config import get_config

app = Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.register_blueprint(admin.admin, url_prefix='/admin')
app.register_blueprint(user_actions.user_module, url_prefix='/user')

if __name__ == '__main__':
    app.secret_key = get_config()['app_secret']
    app.run(host='0.0.0.0')

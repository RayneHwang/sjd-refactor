# -*- coding:utf-8 -*-

from flask import Flask
from flask import jsonify

from blueprints.admin import admin

app = Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.register_blueprint(admin.admin, url_prefix='/admin')

if __name__ == '__main__':
    app.run()

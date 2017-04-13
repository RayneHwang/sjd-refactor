# -*- coding:utf-8 -*-

from flask import Flask
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from utils import Config
from flask_login import login_manager
import routes

config = Config.Config('config.json')
app = Flask(__name__)

engine = create_engine(config.database)
DBSession = sessionmaker(bind=engine)


@login_manager
def load_user():
    """
    
    :return: 
    """
    return


@app.route('/')
def index():
    return routes.index.index()


if __name__ == '__main__':
    app.run()

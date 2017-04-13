from flask import Blueprint, render_template
from sqlalchemy.orm import sessionmaker

from models.CUSTOMER import Customer
from utils import obj_to_json
from utils.db_connection import engine

admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/')
def index():
    return render_template('admin/index.html')


@admin.route('/<page>')
def show(page):
    return render_template('admin/%s.html' % page)


@admin.route('/json')
def jsonres():
    #TODO http://docs.sqlalchemy.org/en/latest/orm/session_basics.html#what-does-the-session-do
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    user = session.query(Customer).filter(Customer.id == '1').one()
    return obj_to_json.obj_to_json(user)

from flask import Blueprint, render_template, request

from models.SJD_USER import SjdUser
from utils.db_connection import DbSession
from utils.errors.parameter_errors import BadRequest
from utils.errors.success import succ_json

routes = Blueprint('admin', __name__, template_folder='templates')


@routes.route('/')
def index():
    return render_template('admin/index.html')


@routes.route('/<page>')
def show(page):
    return render_template('admin/%s.html' % page)


@routes.route('/json/')
def jsonres():
    userid = request.args.get('userid')

    with DbSession() as dbsession:
        print('\n\33[32m session object:%s\n\33[37m' % dbsession)
        if userid == '':
            user = dbsession.query(SjdUser).all()
        else:
            user = dbsession.query(SjdUser).filter(SjdUser.id == userid).scalar()
            if user is None:
                raise BadRequest(code=1, msg='no such user')
        return succ_json(user)

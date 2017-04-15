from flask import Blueprint, render_template, request
from sqlalchemy.orm.exc import NoResultFound

from models.SJD_UCENTER_MEMBER import SjdUcenterMember
from utils import error
from utils.db_connection import get_session
from utils.return_json import return_json

admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/')
def index():
    return render_template('admin/index.html')


@admin.route('/<page>')
def show(page):
    return render_template('admin/%s.html' % page)


@admin.route('/json/')
def jsonres():
    userid = request.args.get('userid')

    dbsession = get_session()

    print('\n\33[32m session object:%s\n\33[37m' % dbsession)
    try:
        if userid == '':
            user = dbsession.query(SjdUcenterMember).all()
        else:
            user = dbsession.query(SjdUcenterMember).filter(SjdUcenterMember.id == userid).one()

    except NoResultFound:
        return return_json(error.NoResErr().toDict())
    finally:
        # 一定要记得关闭session, 否则有会导致连接池溢出
        dbsession.close()
    return return_json(user)

from flask import Blueprint, session, request

from blueprints.user.services import register_service, login_service
from models.SJD_USER import SjdUser
from utils.db_connection import get_session
from utils.return_json import error_json, succ_json

# Lei, HUANG: 17:41 15/04/2017
# Flask defualt session implementation is client-side session
# which is encrypted with app-screte key in config file
# TODO Flask-Session uses multiple session-storafe interface


user_module = Blueprint('user', __name__, template_folder='templates')


@user_module.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        res = login_service.login(username, password)

        if res == 0:
            session['username'] = username
            return succ_json()
        else:
            return error_json(res[0], res[1])
    else:
        return '''
        <form action="" method="POST">
            <p><input type=text name=username>
            <p><input type=text name=password>
            <p><input type=submit value=Login>
        </form>
    '''


@user_module.route('/register', methods=['POST'])
def register():
    """
    用户注册接口
    :return: 注册成功返回
    """
    res = register_service.register(request.form)
    if res == 0:
        return succ_json()
    else:
        return error_json('', res)


@user_module.route('/status')
def status():
    if 'username' in session:
        db_session = get_session()
        user = db_session.query(SjdUser).filter(SjdUser.username == session['username']).one()
        db_session.close()
        print(user)
        return 'you are login in as %s' % user.realname
    else:
        return 'not login'

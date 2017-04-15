from flask import Blueprint, session, request

from models.SJD_USER import SjdUser
from utils.db_connection import get_session
from utils.password_encode import encode

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
        registered_user = get_session().query(SjdUser).filter(SjdUser.username == username,
                                                              SjdUser.password == encode(password)).first()

        if registered_user is None:
            return 'failed'
        else:
            session['username'] = username
            return 'login ok'
    else:
        return '''
        <form action="" method="POST">
            <p><input type=text name=username>
            <p><input type=text name=password>
            <p><input type=submit value=Login>
        </form>
    '''


@user_module.route('/status')
def status():
    if 'username' in session:
        user = get_session().query(SjdUser).filter(SjdUser.username == session['username']).one()

        return 'you are login in as %s' % user.realname
    else:
        return 'not login'

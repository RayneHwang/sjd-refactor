from flask import Flask, Blueprint, session, request
from models.SJD_USER import SjdUser
from utils.db_connection import get_session

# from flask.ext.session import Session
#
# from app import app
#
# SESSION_TYPE = 'filesystem'
# SESSION_FILE_DIR = './sess'
# Session(app)
#
# session = Session()

user_module = Blueprint('user', __name__, template_folder='templates')


@user_module.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mobile = request.form['mobile']
        registered_user = get_session().query(SjdUser).filter(SjdUser.username == username).first()

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
        return 'you are login in as %s' % session['username']
    else:
        return 'not login'

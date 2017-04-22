import logging
import random

from flask import Blueprint, session, request

from blueprints.user.services import login_service
from blueprints.user.services import register_service
from models.SJD_USER import SjdUser
from utils.db_connection import get_session, engine
from utils.return_json import error_json, succ_json

# Lei, HUANG: 17:41 15/04/2017
# Flask defualt session implementation is client-side session
# which is encrypted with app-screte key in config file
# TODO Flask-Session uses multiple session-storafe interface


routes = Blueprint('user', __name__, template_folder='templates')


@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        res = login_service.login(username, password)

        if res[0] == 0:
            session['username'] = username

            def mask_pass(i):
                i.password = 'xxx'
                return i

            return succ_json(mask_pass(res[1]))
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


@routes.route('/register', methods=['POST'])
def register():
    """
    Lei, HUANG: 09:44 16/04/2017
    用户注册接口
    :return: 注册成功返回
    """
    res = register_service.register(request.form)
    if res == 0:
        return succ_json()
    else:
        return error_json('', res)


@routes.route('/status')
def status():
    """
    Lei, HUANG: 11:55 16/04/2017
    :return: 查询当前登录用户 
    """
    if 'username' in session:
        db_session = get_session()
        user = db_session.query(SjdUser).filter(SjdUser.username == session['username']).one()
        db_session.close()
        print(user)
        return 'you are login in as %s' % user.realname
    else:
        return 'not login'


@routes.route('/bm')
def bm():
    """
    Lei, HUANG: 11:54 16/04/2017
    测试数据库并发查询
    """
    userid = random.randint(4000, 4379)
    db_session = get_session()
    try:
        user = db_session.query(SjdUser).filter(SjdUser.id == userid).one()
        print(user)
    except Exception as e:
        logging.exception(e)
    finally:
        pass
        db_session.close()
    return 'you are login in as'


@routes.route('/db')
def db_status():
    """
    Lei, HUANG: 11:53 16/04/2017
    :return:返回当前数据库连接池状态 
    """
    return engine.pool.status()


@routes.route('/send_verify', methods=['POST'])
def send_verify():
    """
    Lei, HUANG: 21:55 21/04/2017
    发送验证码
    :return: 
    """
    mobile = request.form.get('mobile')
    if mobile is None:
        return error_json(1, '手机号码不能为空')
    flag, msg = register_service.send_verify(mobile)
    if flag:
        return succ_json()
    else:
        return error_json(1, msg)


@routes.route('/check_verify', methods=['POST'])
def check_verify():
    """
    Lei, HUANG: 21:54 21/04/2017
    检验用户输入的验证码是否有效
    :return: 
    """
    mobile = request.form.get('mobile')
    verify_code = request.form.get('verify_code')
    if mobile is None or verify_code is None:
        return error_json(1, '手机号码或验证码不能为空')
    else:
        flag = register_service.check_verify(mobile, verify_code)
        if flag:
            return succ_json()
        else:
            return error_json(1, '验证码输入错误')

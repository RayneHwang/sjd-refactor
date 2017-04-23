import logging
import random

from flask import Blueprint, session, request
from sqlalchemy.orm.exc import NoResultFound

from blueprints.user.services import login_service, profile_service
from blueprints.user.services import register_service
from models.SJD_USER import SjdUser
from utils.db_connection import get_session, engine, DbSession

# Lei, HUANG: 17:41 15/04/2017
# Flask defualt session implementation is client-side session
# which is encrypted with app-screte key in config file
# TODO Flask-Session uses multiple session-storafe interface
from utils.errors.parameter_errors import BadRequest
from utils.errors.success import succ_json, return_json
from utils.object_attr_ops import mask_pass
from utils.require_login import require_login

routes = Blueprint('user', __name__, template_folder='templates')


@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        res = login_service.login(username, password)

        if res[0] == 0:
            session['username'] = username
            return succ_json(mask_pass(res[1])) # 从返回信息当中删除用户的密码
        else:
            raise BadRequest(code=res[0], msg=res[1])
    else:
        return '''
        <form action="" method="POST">
            <p><input type=text name=username>
            <p><input type=text name=password>
            <p><input type=submit value=Login>
        </form>
    '''


@routes.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return succ_json()


@routes.route('/register', methods=['POST'])
def register():
    """
    Lei, HUANG: 09:44 16/04/2017
    用户注册接口
    :return: 注册成功返回
    """
    res, msg = register_service.register(request.form.to_dict())
    if res:
        return succ_json()
    else:
        raise BadRequest(code=1, msg=msg)


@routes.route('/check_username')
def check_username():
    res = register_service.is_user_exists(username=request.args.get('username'))
    if res:
        return return_json(code=1)
    else:
        return succ_json()


@routes.route('/status')
def status():
    """
    Lei, HUANG: 11:55 16/04/2017
    :return: 查询当前登录用户 
    """
    if 'username' in session:
        with DbSession() as db_session:
            user = db_session.query(SjdUser).filter(SjdUser.username == session['username']).one()
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
    try:
        with DbSession() as db_session:
            user = db_session.query(SjdUser).filter(SjdUser.id == userid).one()
            print(user)
            return succ_json(user.id)
    except Exception as e:
        logging.exception(e)
        raise BadRequest(1, 'Ro result found')


@routes.route('/send_verify', methods=['POST'])
def send_verify():
    """
    Lei, HUANG: 21:55 21/04/2017
    发送验证码
    :return: 
    """
    mobile = request.form.get('mobile')
    if mobile is None:
        raise BadRequest(code=1, msg='手机号码不能为空')

    if register_service.is_user_exists(mobile):
        raise BadRequest(code=1, msg='该手机号码已经注册')

    flag, msg = register_service.send_verify(mobile)
    if flag:
        return succ_json()
    else:
        raise BadRequest(1, msg)


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
        raise BadRequest(1, '手机号码或验证码不能为空')
    else:
        flag = register_service.check_verify(mobile, verify_code)
        if flag:
            return succ_json()
        else:
            raise BadRequest(1, '验证码输入错误')


@routes.route('/update', methods=['POST'])
def update_user():
    """
    Lei, HUANG: 20:15 23/04/2017
    修改用户信息接口(除了修改密码/头像/微信ID/手机号码 需要另外单独写)
    :return: 
    """
    username = request.form.get('username')

    # 修改信息要求必须登录, 并且只能修改当前登录用户的信息
    require_login(username)
    fields_to_update = request.form.to_dict()

    for forbidden_attr in ['password', 'avatar', 'wx_id', 'mobile']:
        if forbidden_attr in request.form:
            raise BadRequest(1, '不能修改字段<%s>' % forbidden_attr)

    user = profile_service.update_user(username, fields_to_update)
    return succ_json(user)

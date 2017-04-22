import random

from models.SJD_USER import SjdUser
from utils.db_connection import get_session
from utils import password_utils
from utils.sms_gateway import send_sms
from utils.redis_conn import get_redis_conn
from utils.config import get_config
from  utils.password_utils import check_password
from utils.return_json import error_json, succ_json

_DEFAULT_AVATAR = get_config()['avatar_dir'] + '/default.jpg'

# 用户注册必填字段
_REGISTER_REQUIRE_FIELDS = ['mobile', 'password', 'reg_type']


def register(args):
    """
    用户注册服务
    :param args: 包含所有注册需要的信息的dict 
    :return: 成功注册返回0, 否则返回错误信息
    """
    if args.get('avatar') is None:
        args['avatar'] = _DEFAULT_AVATAR

    check_res, msg = check_reg_params(args)
    if not check_res:
        return False,msg

    user = SjdUser(username=args.get('mobile'),  # 用户名即手机号码
                   password=password_utils.encode(args.get('password')),
                   realname=args.get('realname'),
                   nickname=args.get('nickname'),
                   avatar=args.get('avatar'),
                   signature=args.get('signature'),
                   wx_id=args.get('wx_id'),
                   sex=args.get('sex'),
                   birthday=args.get('birthday'),
                   mobile=args.get('mobile'),
                   status=args.get('status'),
                   school=args.get('school'),
                   department=args.get('department'),
                   major=args.get('major'),
                   student_id=args.get('student_id')
                   )
    db_session = get_session()
    db_session.add(user)
    db_session.commit()
    db_session.close()
    return True,None


def check_reg_params(kwargs):
    for attr in ['mobile', 'password', 'reg_type']:
        if attr not in kwargs:
            return False, '<%s> cannot be null' % attr

    pwd_res, pwd_msg = check_password(kwargs.get('password'))
    if not pwd_res:
        return False, pwd_msg

    return True, None


def send_verify(mobile):
    """
    Lei, HUANG: 23:24 21/04/2017
    发送验证码的业务逻辑
    :param mobile: 
    :return: 
    """
    s = '%06d' % random.randint(0, 1000000)
    # insert into redis
    r = get_redis_conn()
    print("verify code is : %s" % s)
    r.set(name=mobile, value=s, ex=600)  # 验证码10分钟之后失效
    flag, msg = send_sms(mobile, s)  # 发送验证码短信
    return flag, msg


def check_verify(mobile, user_code):
    """
    Lei, HUANG: 21:51 21/04/2017
    校验用户输入验证码的业务逻辑
    :param mobile: 用户A手机号码
    :param user_code: 用户输入的验证码
    :return: 
    """
    r = get_redis_conn()
    code_in_redis = r.get(mobile).decode("utf-8")
    if code_in_redis == user_code:
        r.delete(mobile)
        return True
    else:
        return False

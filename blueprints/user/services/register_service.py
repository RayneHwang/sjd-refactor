import random

from models.SJD_USER import SjdUser
from utils.db_connection import get_session
from utils.password_encode import encode
from utils.sms_gateway import send_sms
from utils.redis_conn import get_redis_conn


def register(args):
    """
    用户注册服务
    :param args: 包含所有注册需要的信息的dict 
    :return: 成功注册返回0, 否则返回错误信息
    """
    for attr in ['username', 'password', 'mobile', 'type', 'major', 'department', 'student_id', 'reg_ip',
                 'last_login_ip', 'school']:
        if attr not in args:
            return '<%s> cannot be null' % attr

    user = SjdUser(username=args['username'],
                   password=encode(args['password']),
                   mobile=args['mobile'],
                   type=args['type'],
                   major=args['major'],
                   department=args['department'],
                   student_id=args['student_id'],
                   reg_ip=args['reg_ip'],
                   last_login_ip=args['last_login_ip'],
                   school=args['school']
                   )
    db_session = get_session()
    db_session.add(user)
    db_session.commit()
    db_session.close()
    return 0


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
    :param mobile: 用户手机号码
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

from models.SJD_USER import SjdUser
from utils.db_connection import get_session
from utils.password_encode import encode


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
    return True

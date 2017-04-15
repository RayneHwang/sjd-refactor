from models.SJD_USER import SjdUser
from utils.db_connection import get_session


def register(args):
    """
    用户注册服务
    :param args: 包含所有注册需要的信息的dict 
    :return: 
    """
    for attr in ['username', 'password', 'mobile', 'type', 'major', 'department', 'student_id', 'reg_ip',
                 'last_login_ip', 'school']:
        if attr not in args:
            return '<%s> cannot be null' % attr

    user = SjdUser(username=args['username'],
                   password=args['password'],
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
    return 0

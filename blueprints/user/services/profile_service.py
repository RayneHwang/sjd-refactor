import logging

from models.SJD_USER import SjdUser
from utils.db_connection import DbSession
from utils.errors.internal_errors import InternalError
from utils.object_attr_ops import update_obj_attr, get_ordinary_fields


def update_user(username, kwargs):
    with DbSession() as db_session:
        try:
            user = db_session.query(SjdUser).filter_by(username=username).first()
            update_obj_attr(user, kwargs)
            db_session.commit()
            # 不能直接使用SjdUser对象, 因为这个对象和一个session绑定
            # 需要手动取出所有的key和value,转换成dict
            res = get_ordinary_fields(user)
            if 'password' in res:
                res['password'] = 'xxxxxxx'
            return res
        except Exception as e:
            db_session.rollback()
            logging.error(e)
            raise InternalError(code=1, msg='服务器故障')

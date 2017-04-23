from models.SJD_USER import SjdUser
from utils.db_connection import DbSession
from utils.password_utils import encode

# 返回的错误代码
ERR_NO_SUCH_USER = 10
ERR_PASSWORD = 11


def login(username, password):
    with DbSession() as db_session:
        registered_user = db_session.query(SjdUser).filter(SjdUser.username == username).first()

    if registered_user is None:
        return ERR_NO_SUCH_USER, 'No Such User'
    else:
        if registered_user.password != encode(password):
            return ERR_PASSWORD, 'Password Error'
        else:
            return 0, registered_user

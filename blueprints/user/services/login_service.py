from models.SJD_USER import SjdUser
from utils.db_connection import get_session
from utils.password_encode import encode

# 返回的错误代码
ERR_NO_SUCH_USER = 10
ERR_PASSWORD = 11


def login(username, password):
    db_session = get_session()
    registered_user = db_session.query(SjdUser).filter(SjdUser.username == username).first()
    db_session.close()

    if registered_user is None:
        return ERR_NO_SUCH_USER, 'No Such User'
    else:
        if registered_user.password != encode(password):
            return ERR_PASSWORD, 'Password Error'
        else:
            return 0

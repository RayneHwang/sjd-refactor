from models.SJD_USER import SjdUser
from utils.db_connection import get_session
from utils.password_encode import encode


def login(username, password):
    registered_user = get_session().query(SjdUser).filter(SjdUser.username == username,
                                                          SjdUser.password == encode(password)).first()
    if registered_user is None:
        return 'error'
    else:
        return 0

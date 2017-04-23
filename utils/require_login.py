from flask import session
from utils.errors.parameter_errors import UnauthorizedError


def require_login(username=None):
    if 'username' in session:
        if username is None:
            return True
        if session.get('username') == username:
            return True
    raise UnauthorizedError(code=1, msg='必须先登录')



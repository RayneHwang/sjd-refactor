from utils.errors.base_error import BaseError


class InternalError(BaseError):
    """
    Lei, HUANG: 16:23 23/04/2017
    当检查到用户输入参数缺失/有误的时候抛出BadRequest异常, 
    由app.py当中的generic_error_handler负责处理
    所有的自定义异常必须继承BaseError
    """
    status_code = 200

    def __init__(self, code, msg='服务器错误', status_code=None, payload=None):
        Exception.__init__(self)
        self.code = code
        self.msg = msg
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = {'code': self.code, 'msg': self.msg}
        if self.payload is not None:
            rv['data'] = self.payload
        return rv

import hashlib
import re

# 密码长度限制
_PWD_MAX_LEN = 32
_PWD_MIN_LEN = 6


def encode(string):
    """
        Encode user input password using rules inherit from legacy code
        :arg string input password
        :return encrypted password
    """
    res = hashlib.md5(string.encode()).hexdigest()
    return res[8:24]


def check_password(password):
    """
    Lei, HUANG: 00:41 23/04/2017
    校验密码合法性
    1. 长度在6~32位之间
    2. 必须包含数字/大写字母/小写字母/符号之间至少两种
    :param password: 
    :return:
     合法: True,''
     非法: Flase: '<错误信息>'
    """

    # calculating the length
    length_error = (len(password) > _PWD_MAX_LEN) or (
        len(password) < _PWD_MIN_LEN)

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"\W", password) is None

    # overall result
    password_ok = not (
        length_error or digit_error or uppercase_error or lowercase_error or symbol_error)

    if length_error:
        return False, '密码长度必须在6~32位之间'

    arr = [digit_error, uppercase_error, lowercase_error, symbol_error]
    # print(arr)
    err_num = len([x for x in arr if x == True])

    if err_num > 2:
        return False, '必须包含数字/大写字母/小写字母/特殊字符中至少两种'
    return True, None


if __name__ == '__main__':
    assert '49ba59abbe56e057' == encode('123456')

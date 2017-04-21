from utils.config import get_config
from urllib import request, parse
import simplejson

_SMS_CONFIG = get_config()['sms']

_HEADER = {
    'Content-Type': 'application/x-www-form-urlencoded'
}


def send_sms(mobile, verifyCode):
    """
    Lei, HUANG: 17:06 21/04/2017
    向短信网关发送短信
    :param mobile: 接收验证码的手机号码
    :param verifyCode: 验证码
    :return:    若发送成功, 返回的第一个值为True, 第二个值为空字符串
                若发送失败,则第一个值为False,第二个值为失败的具体信息
    """
    form = {
        'account': _SMS_CONFIG['username'],
        'password': _SMS_CONFIG['pwd'],
        'mobile': mobile,
        'content': '您的验证码是：{code}。请不要把验证码泄露给其他人。'.format(code=verifyCode),
        'format': 'json'
    }
    req = request.Request(
        url=_SMS_CONFIG['url'],
        method='POST',
        headers=_HEADER,
        data=parse.urlencode(form).encode()  # 注意编码, urllib的data字段接收的是byte类型, 需要手动把str转成byte
    )
    response = request.urlopen(req)
    res_dict = simplejson.loads(response.read().decode())
    if 'code' in res_dict and res_dict['code'] == 2:
        return True, verifyCode
    else:
        return False, res_dict['msg']


if __name__ == '__main__':
    res, msg = send_sms('18664940898', '1233')
    print(res)
    print(msg)

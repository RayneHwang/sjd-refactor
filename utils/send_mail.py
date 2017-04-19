import logging
import smtplib
from email.mime.text import MIMEText

from utils.config import get_config

mail_config = get_config()['mail']

mail_params = ['MAIL_USER', 'MAIL_PWD', 'MAIL_SERVER', 'MAIL_FROM']
for attr in mail_params:
    if mail_params not in mail_config:
        raise ValueError('Mail configuration field <%s> not found' % attr)

MAIL_USER = mail_config['MAIL_USER']
MAIL_PWD = mail_config['MAIL_PWD']
MAIL_SERVER = mail_config['MAIL_SERVER']
MAIL_FROM = mail_config['MAIL_FROM']


def send_mail(to_list, sub, content):
    me = "" + MAIL_FROM + "<" + MAIL_USER
    msg = MIMEText(content, _subtype='plain', _charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(MAIL_SERVER)
        server.login(MAIL_USER, MAIL_PWD)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        logging.exception(e)
        # print(traceback.format_exc())
        return False


if __name__ == '__main__':
    send_mail(['714582494@qq.com'], 'vim 8.0', 'This is a test email sent by python smtp client')

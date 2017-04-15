import datetime

from models.BASE import BASE
from sqlalchemy import String, Integer, Column


class SjdUser(BASE):
    __tablename__ = "SJD_USER"
    id = Column(Integer, primary_key=True)
    username = Column(String(32))
    password = Column(String(32))
    realname = Column(String(32))
    email = Column(String(32))
    mobile = Column(String(15))
    reg_time = Column(Integer)
    reg_ip = Column(Integer)
    last_login_time = Column(Integer)
    last_login_ip = Column(Integer)
    update_time = Column(Integer)
    status = Column(Integer)
    type = Column(Integer)
    school = Column(String(50))
    department = Column(String(50))
    major = Column(String(50))
    student_id = Column(String(15))

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.reg_time = datetime.datetime.utcnow()

    def __repr__(self):
        return '<SJD_USER %s>' % self.id

import datetime

from models.BASE import BASE
from sqlalchemy import String, Integer, Column, Text, Date

SJD_USER_REG_BY_STUID = 1
SJD_USER_REG_BY_PHONE = 2
SJD_USER_REG_BY_EMAIL = 3


class SjdUser(BASE):
    __tablename__ = "SJD_USER"
    id = Column('ID', Integer, primary_key=True)
    username = Column('USERNAME', String(32))
    password = Column('PASSWORD', String(32))
    realname = Column('REALNAME', String(32))
    nickname = Column('NICKNAME', String(32))
    signature = Column('SIGNATURE', Text)
    sex = Column('SEX', Integer)
    birthday = Column('BIRTHDAY', Date)
    mobile = Column('MOBILE', String(15))
    status = Column('STATUS', Integer)
    reg_type = Column('TYPE', Integer)
    school = Column('SCHOOL', String(50))
    department = Column('DEPARTMENT', String(50))
    student_id = Column('STUDENT_ID', String(15))

    def __init__(self, username, password, **kwargs):
        self.username = username
        self.password = password
        self.realname = kwargs.get('realname')
        self.nickname = kwargs.get('nickname')
        self.signature = kwargs.get('signature')
        self.sex = kwargs.get('sex')
        self.birthday = kwargs.get('birthday')
        self.mobile = kwargs.get('mobile')
        self.status = kwargs.get('status')
        self.reg_type = kwargs.get('reg_type')
        self.school = kwargs.get('school')
        self.department = kwargs.get('department')
        self.student_id = kwargs.get('student_id ')

    def __repr__(self):
        return '<SJD_USER %s>' % self.id

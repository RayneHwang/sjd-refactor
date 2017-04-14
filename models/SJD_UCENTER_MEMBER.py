from models.BASE import BASE
from sqlalchemy import String, Integer, Column


class SjdUcenterMember(BASE):
    __tablename__ = "sjd_ucenter_member"
    id = Column(Integer, primary_key=True)
    username = Column(String(32))
    password = Column(String(32))
    realname = Column(String(32))
    email = Column(String(32))
    mobile = Column(String(15))
    email_checked = Column(Integer)
    mobile_checked = Column(Integer)
    full_level = Column(Integer)
    trust_score = Column(Integer)
    reg_time = Column(Integer)
    reg_ip = Column(Integer)
    last_login_time = Column(Integer)
    last_login_ip = Column(Integer)
    update_time = Column(Integer)
    status = Column(Integer)
    type = Column(Integer)
    stu_school = Column(String(50))
    department = Column(String(50))
    major = Column(String(50))
    identification = Column(Integer)
    is_upload = Column(Integer)
    random_num = Column(Integer)
    student_id = Column(String(15))

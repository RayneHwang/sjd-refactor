from sqlalchemy import Column, String

from models.BASE import BASE


class Customer(BASE):
    __tablename__ = 'customer'
    id = Column(String(11), primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))

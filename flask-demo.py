from flask import Flask
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from utils import Config

config = Config.Config('config.json')
app = Flask(__name__)

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(String(11), primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))


engine = create_engine(config.database)
DBSession = sessionmaker(bind=engine)


@app.route('/')
def hello():
    session = DBSession()
    user = session.query(Customer).filter(Customer.id == '1').one()
    return "<h1>" + user.firstname + "</h1><br>" + "<h1>" + user.lastname + "</h1><br>"


if __name__ == '__main__':
    app.run()

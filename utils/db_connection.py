from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import SingletonThreadPool

from utils.Config import Config

databaseconfig = Config('./config.json').database
engine = create_engine(databaseconfig['url'],
                       pool_size=2,
                       max_overflow=0,
                       echo=True,
                       echo_pool=True,
                       pool_timeout=3,
                       pool_recycle=200
                       # pool_pre_ping=True
                       )

db_session_factory = sessionmaker(bind=engine)


def get_session():
    session = db_session_factory()
    return session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.Config import get_config

databaseconfig = get_config()['database']

engine = create_engine(databaseconfig['url'],
                       pool_size=databaseconfig['pool_size'],
                       max_overflow=databaseconfig['max_overflow'],
                       echo=True,
                       echo_pool=True,
                       pool_timeout=3,
                       pool_recycle=200
                       # pool_pre_ping=True
                       )

db_session_factory = sessionmaker(bind=engine)


def get_session():
    """获取一个session实例, 完成操作后务必关闭"""
    session = db_session_factory()
    return session

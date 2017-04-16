from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from utils.Config import get_config

databaseconfig = get_config()['database']

engine = create_engine(databaseconfig['url'],
                       pool_size=databaseconfig['pool_size'],
                       max_overflow=databaseconfig['max_overflow'],
                       echo=False,
                       echo_pool=True,
                       pool_timeout=3,
                       pool_recycle=2
                       # pool_pre_ping=True
                       )

db_session_factory = sessionmaker(bind=engine)


def on_checkout(dbapi_conn, connection_rec, connection_proxy):
    print("checkout", dbapi_conn)
    print("Status: %s" % engine.pool.status())
    print()


def on_checkin(dbapi_conn, connection_rec):
    print("checkin", dbapi_conn)
    print("Status: %s" % engine.pool.status())


event.listen(engine, 'checkout', on_checkout)
event.listen(engine, 'checkin', on_checkin)


def get_session():
    """获取一个session实例, 完成操作后务必关闭"""
    session = db_session_factory()
    return session

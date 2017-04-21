from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from utils.config import get_config

_DATABASE_CONFIG = get_config()['database']

_DB_PARAMS = ['pool_size', 'echo', 'echo_pool', 'max_overflow', 'pool_timeout', 'pool_recycle']

# 检查是否缺少数据库配置参数
for attr in _DB_PARAMS:
    if attr not in _DATABASE_CONFIG:
        raise ValueError("Database configuration field <%s> not found" % attr)

engine = create_engine(_DATABASE_CONFIG['url'],
                       pool_size=_DATABASE_CONFIG['pool_size'],
                       max_overflow=_DATABASE_CONFIG['max_overflow'],
                       echo=_DATABASE_CONFIG['echo'],
                       echo_pool=_DATABASE_CONFIG['echo_pool'],
                       pool_timeout=_DATABASE_CONFIG['pool_timeout'],
                       pool_recycle=_DATABASE_CONFIG['pool_recycle']
                       # pool_pre_ping=True
                       )

_DB_SESSION_FACTORY = sessionmaker(bind=engine)


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
    session = _DB_SESSION_FACTORY()
    return session

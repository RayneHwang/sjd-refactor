import redis
from utils import config

_REDIS_CONFIG = config.get_config()['redis']
_POOL = redis.BlockingConnectionPool(host=_REDIS_CONFIG['url'],
                                     port=_REDIS_CONFIG['port'],
                                     password=_REDIS_CONFIG['pwd'],
                                     max_connections=10
                                     )


def get_redis_conn():
    return redis.Redis(connection_pool=_POOL)


if __name__ == '__main__':
    for i in range(0, 100):
        r = get_redis_conn()
        r.delete('k' + str(i))

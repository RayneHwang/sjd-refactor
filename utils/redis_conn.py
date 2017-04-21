import redis
from utils import config

redis_config = config.get_config()['redis']
POOL = redis.BlockingConnectionPool(host=redis_config['url'],
                                    port=redis_config['port'],
                                    password=redis_config['pwd'],
                                    max_connections=10
                                    )


def get_redis_conn():
    return redis.Redis(connection_pool=POOL)


if __name__ == '__main__':
    for i in range(0, 100):
        r = get_redis_conn()
        r.delete('k' + str(i))

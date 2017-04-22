import redis

_POOL = redis.BlockingConnectionPool(host='119.29.116.114',
                                     port=6379,
                                     password='@:wjk?\";76,2',
                                     max_connections=10
                                     )


def get_redis_conn():
    return redis.Redis(connection_pool=_POOL)


if __name__ == '__main__':
    r = get_redis_conn()
    list = r.keys('OID_UID*')
    for keys in list:
        print(keys)
        print(r.get(keys.decode('utf8')))

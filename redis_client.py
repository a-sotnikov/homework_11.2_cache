import redis

redis_host = '192.168.56.103'
redis_port = 6379

r = redis.Redis(redis_host, redis_port)

r.set('hw_num', '11,2')
r.set('hw_name', 'Redis/memcached')
r.set('year', 2023)

r.set('key5', 5)

r.incrby('key5', 5)

r.get('key5')

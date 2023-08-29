import redis

host = "localhost"
port = 6739


class RedisDB:
    def __init__(self):
        self.dbInstance = redis.Redis(host=host, port=port, decode_responses=True)

    def __init__(self, host_addr: str, port_num: int):
        self.dbInstance = redis.Redis(host=host_addr, port=port_num, decode_responses=True)

    def addData(self, key: str, value: int):
        self.dbInstance.set(key, value)

    def getValueFromKey(self, key: str):
        return self.dbInstance.get(key)

    def flush(self):
        self.dbInstance.flushall()

    def getKeys(self):
        return self.dbInstance.keys()

import time

class SimpleCache:
    """
    Simple in-memory cache with expiration.
    """
    def __init__(self, expire_seconds=600):
        self.expire_seconds = expire_seconds
        self.cache = {}

    def get(self, key):
        entry = self.cache.get(key, None)
        if entry:
            value, timestamp = entry
            if time.time() - timestamp < self.expire_seconds:
                return value
            else:
                del self.cache[key]
        return None

    def set(self, key, value):
        self.cache[key] = (value, time.time())
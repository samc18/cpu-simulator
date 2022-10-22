import collections

cache_size = 16

class Cache:
    def __init(self):
        self.cache = collections.deque(maxlen = cache_size)
        self.flush_cache()

    def flush_cache(self):
        for i in range(cache_size):
            self.cache.append(('',''))

    def search_cache(self, address):
        for i in range(cache_size):
            if self.cache[i][0] == address:
                return self.cache[i][1]
        return None

    def write_cache(self, address, value):
        self.cache.append((address, value))
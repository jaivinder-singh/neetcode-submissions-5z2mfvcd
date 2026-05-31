class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lRUCache = collections.OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.lRUCache:
            return -1
        self.lRUCache.move_to_end(key)
        return self.lRUCache[key]

        

    def put(self, key: int, value: int) -> None:
        if key in self.lRUCache:
            self.lRUCache.move_to_end(key)
        self.lRUCache[key] = value
        if len(self.lRUCache) > self.capacity:
            self.lRUCache.popitem(last=False)
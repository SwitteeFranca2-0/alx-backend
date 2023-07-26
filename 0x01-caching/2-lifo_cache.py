#!/usr/bin/env python3
"""lifo cache"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Class implementing a caching system"""
    __last_item = []
    __key = ""

    def __init__(self):
        """initialising the baseic cache class"""
        super().__init__()

    def put(self, key, item):
        """Assings a key-value to the dictionary"""
        if key is not None and item is not None:
            if key in LIFOCache.__last_item:
                LIFOCache.__last_item.remove(key)
            LIFOCache.__last_item.append(key)
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            LIFOCache.__key = list(reversed(LIFOCache.__last_item))[1]
            LIFOCache.__last_item.remove(LIFOCache.__key)
            discard = LIFOCache.__key
            print("DISCARD: {}".format(discard))
            del self.cache_data[LIFOCache.__key]

    def get(self, key):
        """Get ky value from the cache dictionery"""
        if key is not None:
            return self.cache_data.get(key)
        return None

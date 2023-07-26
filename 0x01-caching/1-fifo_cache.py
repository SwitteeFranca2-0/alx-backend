#!/usr/bin/env python3
"""lifo cache"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Class implementing a caching system"""

    def __init__(self):
        """initialising the baseic cache class"""
        super().__init__()

    def put(self, key, item):
        """Assings a key-value to the dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = list(self.cache_data.keys())[0]
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]

    def get(self, key):
        """Get ky value from the cache dictionery"""
        if key is not None:
            return self.cache_data.get(key)
        return None

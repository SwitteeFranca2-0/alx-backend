#!/usr/bin/env python3
"""lifo cache"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Class implementing a caching system"""
    __last_item = []

    def __init__(self):
        """initialising the baseic cache class"""
        super().__init__()

    def put(self, key, item):
        """Assings a key-value to the dictionary"""
        if key is not None and item is not None:
            if key in MRUCache.__last_item:
                MRUCache.__last_item.remove(key)
            MRUCache.__last_item.append(key)
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = list(reversed(MRUCache.__last_item))[1]
            MRUCache.__last_item.remove(discard)
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]

    def get(self, key):
        """Get ky value from the cache dictionery"""
        if key is not None:
            if key in MRUCache.__last_item:
                MRUCache.__last_item.remove(key)
            if key in self.cache_data.keys():
                MRUCache.__last_item.append(key)
            return self.cache_data.get(key)
        return None

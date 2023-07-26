#!/usr/bin/env python3
"""lifo cache"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Class implementing a caching system"""

    def put(self, key, item):
        """Assings a key-value to the dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get ky value from the cache dictionery"""
        if key is not None:
            return self.cache_data.get(key)
        return None

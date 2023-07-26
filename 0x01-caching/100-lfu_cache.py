#!/usr/bin/env python3
"""lifo cache"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Class implementing a caching system"""
    __key_list = []
    __keys = {}

    def __init__(self):
        """initialising the baseic cache class"""
        super().__init__()

    def put(self, key, item):
        """Assings a key-value to the dictionary"""
        if key is not None and item is not None:
            if key in LFUCache.__key_list:
                LFUCache.__key_list.remove(key)
            if key in LFUCache.__keys:
                LFUCache.__keys[key] += 1
            else:
                LFUCache.__keys[key] = 1
            LFUCache.__key_list.append(key)
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key_out = [k for k in LFUCache.__keys.keys() if k not in
                       LFUCache.__key_list]
            for k in key_out:
                del LFUCache.__keys[k]
            num = min(list(LFUCache.__keys.values())[:-1])
            key_num = [k for k, v in LFUCache.__keys.items() if v == num]
            if len(key_num) == 1:
                discard = key_num[0]
            else:
                new_list = [k for k in LFUCache.__key_list if k in key_num]
                discard = new_list[0]
            LFUCache.__key_list.remove(discard)
            del LFUCache.__keys[discard]
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]

    def get(self, key):
        """Get ky value from the cache dictionery"""
        if key is not None:
            if key in LFUCache.__keys:
                LFUCache.__keys[key] += 1
            else:
                LFUCache.__keys[key] = 1
            if key in LFUCache.__key_list:
                LFUCache.__key_list.remove(key)
            if key in self.cache_data.keys():
                LFUCache.__key_list.append(key)
            return self.cache_data.get(key)
        return None

#!/usr/bin/env python3
"""Basic caching"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching system that inherits from BaseCaching.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key to store the item.
            item: The item to store in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The value in the cache associated with the key,
            or None if the key doesn't exist.
        """
        return self.cache_data.get(key, None)

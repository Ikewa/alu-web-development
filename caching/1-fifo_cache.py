#!/usr/bin/env python3
"""FIFO Caching"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Cache class that inherits from BaseCaching.

    Implements a First-In-First-Out (FIFO) caching mechanism.
    """

    def __init__(self):
        """
        Initialize the FIFOCache class by calling the parent class initializer.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.
        If the cache exceeds MAX_ITEMS, discard the first item added (FIFO).

        Args:
            key: The key for the item to add.
            item: The value of the item to add.
        """
        if key is not None and item is not None:
            # If the cache is at or above max capacity, remove the oldest item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]

            # Add the new key-value pair
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

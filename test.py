"""
Author: Angela Zhang
Date: April 1, 2025
Testing LRU Cache Implementation. For details, see `README.md`.
"""

import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_put_and_list_elements(self):
        # Test adding elements and listing them in order
        cache = LRUCache(max_size=3)
        cache.put(1)
        cache.put(2)
        cache.put(3)
        self.assertEqual(cache.list_elements(), [1, 2, 3])

    def test_pop(self):
        # Test popping elements from the cache
        cache = LRUCache(max_size=3)
        cache.put(1)
        cache.put(2)
        cache.put(3)
        self.assertEqual(cache.pop(), 1)
        self.assertEqual(cache.list_elements(), [2, 3])

    def test_lru_eviction(self):
        # Test that the least recently used element is removed when max_size is exceeded
        cache = LRUCache(max_size=3)
        cache.put(1)
        cache.put(2)
        cache.put(3)
        cache.put(4)                # 1 should be removed here!
        self.assertEqual(cache.list_elements(), [2, 3, 4])

    def test_update_max_size_smaller(self):
        # Test reducing max_size and ensuring elements are evicted properly
        cache = LRUCache(max_size=4)
        cache.put(1)
        cache.put(2)
        cache.put(3)
        cache.put(4)
        cache.update_max_size(2)     # only [3, 4] should be left
        self.assertEqual(cache.list_elements(), [3, 4])

    def test_update_max_size_larger(self):
        # Test increasing max_size and ensuring new elements can be added
        cache = LRUCache(max_size=2)
        cache.put(1)
        cache.put(2)
        cache.update_max_size(4)
        cache.put(3)
        cache.put(4)
        self.assertEqual(cache.list_elements(), [1, 2, 3, 4])

    def test_is_empty(self):
        # Test the is_empty method
        cache = LRUCache(max_size=2)
        self.assertTrue(cache.is_empty())
        cache.put(1)
        self.assertFalse(cache.is_empty())

    def test_pop_empty(self):
        # Test popping from an empty cache should raise an exception
        cache = LRUCache(max_size=2)
        with self.assertRaises(Exception):
            cache.pop()

    def test_thread_safety(self):
        # Test thread-safety with multiple threads accessing the cache
        import threading
        cache = LRUCache(max_size=5)

        def add_elements():
            for i in range(10):
                cache.put(i)

        # creating 5 threads, each adding 10 elements
        threads = [threading.Thread(target=add_elements) for _ in range(5)]

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        # multithreading should not make us exceed the limit size of 5
        self.assertEqual(len(cache.list_elements()), 5)

    def test_max_size_zero(self):
        # Test that no items can be added when max_size is set to 0
        cache = LRUCache(max_size=0)
        cache.put(1)
        self.assertEqual(cache.list_elements(), [])

    def test_pop_from_empty_cache_after_eviction(self):
        # Test that popping from an empty cache raises an exception after eviction
        cache = LRUCache(max_size=3)
        cache.put(1)
        cache.put(2)
        cache.put(3)
        cache.pop()
        cache.pop()
        cache.pop()
        with self.assertRaises(IndexError):
            cache.pop()

    def test_lru_eviction_order(self):
        # Test that the least recently used element is evicted first
        cache = LRUCache(max_size=3)
        cache.put(1)
        cache.put(2)
        cache.put(3)
        cache.put(4)  # Evicts 1
        self.assertEqual(cache.list_elements(), [2, 3, 4])
        cache.put(5)  # Evicts 2
        self.assertEqual(cache.list_elements(), [3, 4, 5])
        cache.put(6)  # Evicts 3
        self.assertEqual(cache.list_elements(), [4, 5, 6])

    def test_update_max_size(self):
        # Test that the max_size can be updated and old items are evicted if necessary
        cache = LRUCache(max_size=5)
        cache.put(1)
        cache.put(2)
        cache.put(3)
        cache.put(4)
        cache.put(5)
        cache.update_max_size(3)  # Should evict 1 and 2
        self.assertEqual(cache.list_elements(), [3, 4, 5])

    def test_is_empty(self):
        # Test that is_empty() correctly reflects the state of the cache
        cache = LRUCache(max_size=3)
        self.assertTrue(cache.is_empty())   # Initially empty
        cache.put(1)
        self.assertFalse(cache.is_empty())  # After adding an item
        cache.pop()
        self.assertTrue(cache.is_empty())   # After removing the only item

    def test_non_comparable_items(self):
        # Test the cache with non-comparable items
        cache = LRUCache(max_size=3)
        cache.put({"key": "value1"})
        cache.put({"key": "value2"})
        cache.put({"key": "value3"})
        cache.put({"key": "value4"})        # Evicts the least recently used dictionary
        self.assertEqual(cache.list_elements(), [{"key": "value2"}, {"key": "value3"}, {"key": "value4"}])


if __name__ == '__main__':
    unittest.main()

"""
Author: Angela Zhang
Date: April 1, 2025
LRU Cache Implementation. For details, see `README.md`.
"""

from typing import TypeVar, Generic, Optional, List

T = TypeVar("T")                       # A generic type variable for function parameters


class Node(Generic[T]):                # Used by LRU Cache for linked list implementation
    def __init__(self, val: T, next: Optional["Node[T]"] = None, prev: Optional["Node[T]"] = None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache(Generic[T]):
    def __init__(self, max_size: int = -1) -> None:
        self.max_size = max_size        # -1 <=> no max size limit
        self.curr_size = 0
        self.head = Node(None)          # Empty node that points to most recent item
        self.tail = self.head           # The least recently used item

    def put(self, item: T) -> None:
        # should not put anything in cache if max size is 0
        if self.max_size != 0:
            # evict item if over capacity
            if -1 != self.max_size == self.curr_size:
                self._remove_lru_item()

            # insert item at "beginning" head
            second_item = self.head.next
            self.head.next = Node(item, second_item, self.head)

            if second_item is not None:
                second_item.prev = self.head.next
            else:
                # the item after head is None <=> there was nothing in cache before
                self.tail = self.tail.next

            self.curr_size += 1

    def pop(self) -> Optional[T]:
        # edge case: no items in our cache
        if self.curr_size == 0:
            raise IndexError("You tried to pop from an empty cache.")

        return self._remove_lru_item()

    def list_elements(self) -> List[T]:
        oldest_to_newest = [None for _ in range(self.curr_size)]
        pointer = self.head.next        # Keeps position of linked list
        i = self.curr_size - 1          # Keeps position of our list to return
        while pointer is not None:
            oldest_to_newest[i] = pointer.val
            i -= 1
            pointer = pointer.next

        return oldest_to_newest

    def max_size(self) -> int:
        return self.max_size

    def update_max_size(self, size_to_update_to: int) -> None:
        # not possible to update to negative sized cache
        if size_to_update_to >= 0:
            self.max_size = size_to_update_to

            # check for any items to delete
            while self.curr_size > self.max_size:
                self._remove_lru_item()

    def is_empty(self) -> bool:
        return self.curr_size == 0

    def _remove_lru_item(self) -> T:   # Should only be called if there is > 0 items in cache
        lru_item = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        self.curr_size -= 1
        return lru_item

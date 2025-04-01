# Cohere Take-Home: Thread-Safe Least Recently Used (LRU) Cache

## Author
**Angela Zhang**  
Created on: April 1, 2025

## Overview
This project implements a **thread-safe Least Recently Used (LRU) cache** in Python. The implementation adheres to the specified constraints, avoiding built-in queue classes while utilizing only the Python standard library.

## Instructions Given & Followed
- Do not use built-in queue classes from the Python standard library.
- The implementation must be **thread-safe**.
- The code should be **original** and should not rely on AI-generated solutions.
- This implementation is expected to be completed within **one hour**.

## Features
- **Thread-Safety:** Ensures safe access in a multi-threaded environment.
- **LRU Caching:** Maintains a queue where the least recently used items are removed when the cache reaches `max_size`.
- **Customizable `max_size`:** Allows dynamic updates to the maximum number of elements in the queue.
- **Queue Operations:** Supports adding, removing, and listing elements in order.

## File Structure
This project consists of two files:

- `lru_cache.py`: Contains the implementation of the LRU cache class.

- `test.py`: Contains unit tests to verify the functionality of the LRU cache.

## Usage
### Class Methods
The LRU cache class provides the following methods:

#### `put(item) -> None`
Adds an element to the queue. If the cache exceeds `max_size`, the oldest element is removed.

#### `pop() -> Any`
Removes and returns the oldest element from the queue.

#### `list_elements() -> List[Any]`
Returns all elements in the queue, ordered from oldest to newest.

#### `max_size() -> int`
Returns the current maximum size of the queue.

#### `update_max_size(new_size: int) -> None`
Updates the `max_size` for the queue. If `new_size` is smaller than the current number of elements, the oldest elements are removed accordingly.

#### `is_empty() -> bool`
Checks whether the queue is empty.

## Features Tested

### 1. **Basic Functionality**

- Adding elements and listing them in order (`put` and `list_elements` methods).
- Popping elements from the cache (`pop` method).

### 2. **LRU Eviction**

- Ensuring the least recently used element is removed when the cache exceeds its `max_size`.
- Checking that eviction order is maintained correctly as new elements are inserted.

### 3. **Dynamic Max Size Updates**

- Reducing `max_size` and verifying that excess elements are evicted.
- Increasing `max_size` and ensuring new elements can be added.

### 4. **Edge Cases**

- **Empty Cache Operations**: Ensuring that popping from an empty cache raises an exception.
- **Zero Max Size**: Validating that no elements can be added when `max_size=0`.
- **Eviction After Consecutive Pops**: Confirming that popping all elements and then attempting another pop raises an exception.
- **Handling Non-Comparable Items**: Storing objects like dictionaries and ensuring proper eviction.

### 5. **Concurrency and Thread Safety**

- Running multiple threads that add elements simultaneously and ensuring that the cache does not exceed its capacity.

### 6. **Helper Methods Validation**

- Ensuring `is_empty()` correctly reflects whether the cache has elements or not.

## Running Tests

To execute the test suite, run the following command:

```sh
python -m unittest discover
```

This will run all 13 test cases and validate the correctness of the LRU cache implementation.

## Runtime Complexity

The LRU Cache implementation provides efficient operations using a combination of a hash map and a doubly linked list. The runtime complexities for key operations are:

- **`put(item)`**: \( O(1) \) – Insertion and updates are constant time using a hash map for quick lookups and a doubly linked list for efficient reordering.
- **`pop()`**: \( O(1) \) – The least recently used item is removed in constant time by updating pointers in the linked list and hash map.
- **`list_elements()`**: \( O(n) \) – Retrieving all elements requires traversing the linked list.
- **`update_max_size(new_size)`**: \( O(k) \) – If the size is reduced, at most \( k \) items (difference between old and new max size) are removed in linear time.
- **`is_empty()`**: \( O(1) \) – Checking the cache size is a simple comparison.

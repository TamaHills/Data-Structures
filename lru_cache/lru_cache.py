from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.cache = DoublyLinkedList()
        self.size = 0
        self.store = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        value = None
        # retrieve refernce to node from store
        node = self.store.get(key)
        if node:
            # unpack key, value pair
            # move node to head of cache
            key, value = node.value
            self.cache.move_to_front(node)
        return value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # retrieve reference to node if exists
        node = self.store.get(key)

        # check if node reference exists
        if node:
            # delete existing node from cache
            self.cache.delete(node)
        
        # add key, value pair to cache
        # save refrence into the store
        self.cache.add_to_head((key, value))
        self.store[key] = self.cache.head
        
        # if new cache length is greater than limit
        if len(self.cache) > self.limit:
            # unpack key, value pair from tail
            expr_key, value = self.cache.tail.value
            # remove tail node 
            # overwrite store value to None
            self.cache.remove_from_tail()
            del self.store[expr_key]

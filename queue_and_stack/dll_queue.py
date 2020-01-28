import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #   O(1) access to first and last elements
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        value = None
        if self.storage.tail:
            self.size -= 1
            value = self.storage.tail.value
            self.storage.remove_from_tail()
        return value

    def len(self):
        return self.size

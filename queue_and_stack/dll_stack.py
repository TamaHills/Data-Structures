import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #    Doubly linked lists are faster for 
        #    accessing and modifying the last item
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size = len(self.storage)        

    def pop(self):
        value = None
        if self.storage.tail:
            value = self.storage.remove_from_tail()
        self.size = len(self.storage)
        return value

    def len(self):
        return self.size
    
    def __len__(self):
        return self.size

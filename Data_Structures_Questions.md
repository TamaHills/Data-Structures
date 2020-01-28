Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

    `add_to_front` is constant, so it will run in O(1)

2. What is the runtime complexity of `dequeue`?

    `remove_from_tail` is constant, so it will run in O(1)

3. What is the runtime complexity of `len`?

    it just returns an attribute, so it will run in O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

    constant time

2. What is the runtime complexity of `ListNode.insert_before`?

    constant time

3. What is the runtime complexity of `ListNode.delete`?

    constant time

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

    constant time

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

    constant time

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

    constant time

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

    constant time

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

    constant time

9.  What is the runtime complexity of `DoublyLinkedList.move_to_end`?

    constant time

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    constant time

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
        delete wil run in constant time where as js splice runs in 
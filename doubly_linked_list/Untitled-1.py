from doubly_linked_list import DoublyLinkedList
def rerverse(list):
    prev = None 
    temp = None
    current = list.head # a

    while current.next:
        temp = current.next # b c d
        current.next = prev # none a b
        prev = current # a b c
        current = temp
    
    current.next = prev
        
    
    return current

sll = DoublyLinkedList()

sll.add_to_head(10)
sll.add_to_head(20)
sll.add_to_head(5)
sll.add_to_head(2)

curr = sll.head
while curr:
    print(curr.value)
    curr = curr.next 

 

curr = rerverse(sll)
while curr:
    print(curr.value)
    curr = curr.next 

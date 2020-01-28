prev = None 
temp = None
current = list.head # a

while current.next:
    temp = current.next # b c d
    current.next = prev # none a b
    prev = current # a b c
    current = temp # b c d
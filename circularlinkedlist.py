#Circular linkedlist

class Node:
    def __init__(self, value):

        self.value = value
        self.next = None

class  circularLinkedList:
    def __init__(self):
        
        self.head = None
        self.tail = None
    def append(self,value):
        ''' add a node at the end of the list'''
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return None
        cur_node = self.head
        while cur_node:
            if cur_node.next == None:
               cur_node.next = new_node
               self.tail = cur_node.next
               self.tail.next = self.head
               break
            cur_node = cur_node.next


c = circularLinkedList()
c.append(10)
c.append(20)
print(c.head.next.next.next.next.value)

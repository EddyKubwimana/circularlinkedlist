#Circular linkedlist

class Node:
    def __init__(self, value):

        self.value = value
        self.next = None

class  circularLinkedList:
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.size = 0
    def append(self,value):
        ''' add a node at the end of the list'''
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.size = 1
            return None
        cur_node = self.head
        while cur_node:
            self.size+=1
            if cur_node.next == None:
               cur_node.next = new_node
               self.tail = cur_node.next
               self.tail.next = self.head
               break
            cur_node = cur_node.next


    def insert(self,value, position):
        if position == 0:
            self.size +=1
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        cur_node = self.head
        counter = 0
        
            
    def len_list(self):
           if self.head==0:
               return 0
           return self.size



c = circularLinkedList()
c.append(10)
c.append(20)
c.insert(25,0)
c.insert(100,0)
c.insert(200,0)
print(c.head.next.next.next.value)
print(c.len_list())


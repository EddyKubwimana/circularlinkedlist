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
            self.tail = self.head
        elif self.head.next == None:
            self.size+=1
            self.tail = new_node
            self.head.next = self.tail
        else:
            self.size +=1
            self.tail.next = new_node
            self.tail= self.tail.next
            self.tail.next = self.head
            
    def insert(self,value, position):
        '''insert a node at a given positio. The first argument is the value you insert, the second position the position'''
        if position == 0:
            self.size +=1
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            return None
        cur_node = self.head
        counter = 0
        while cur_node.next:
            counter+=1
            if counter == position and counter != self.size-1:
                self.size+=1
                new_node = Node(value)
                next_list = cur_node.next
                new_node.next =next_list
                cur_node.next = new_node
                break
            elif counter == self.size-1:
                self.size+=1
                new_node = Node(value)
                next_nodes = cur_node.next
                cur_node = new_node
                cur_node.next = next_nodes
                
                
                break
            cur_node = cur_node.next      

    def __str__(self):
        '''print the the linkedlist object'''
        number = []
        cur_node = self.head
        counter = 0
        while cur_node:
            counter+= 1
            if self.size>=counter:
               number.append(cur_node.value)
            else:
               return f"{number}"
            cur_node = cur_node.next
    def __add__(self, other):
        ''' add the linked list object'''
        if self.size == other.size:
            number = []
            cur_node = self.head
            s_node = other.head
            counter = 0
            while cur_node :
                counter+= 1
                if self.size>=counter:
                   number.append(cur_node.value+s_node.value)
                else:
                   return number
                cur_node = cur_node.next
                s_node = s_node.next
        else:
            raise IndexError('the two list do not have the same lenght')
    @property
    def reverse(self):
        '''reverse the circular linkedlist'''
        if self.head  is None:
            raise KeyError('The list is empty')
        prev = None
        cur_node = self.head
        cur_tail = self.tail
        while cur_node is not None:
            next_nodes = cur_node.next
            cur_node.next = prev
            prev= cur_node
            cur_node = next_nodes
        self.head = prev.next
        self.tail = prev

        
              
        

chain = circularLinkedList()
chain.append(10)
chain.append(20)
chain.append(30)
chain.append(50)
chain.append(70)
chain.append(80)
chain.append(70)
print(chain)
chain.reverse()
print(chain)










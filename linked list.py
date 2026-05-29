##defination of linked lists##

'''
A Linked List is a linear data structure where elements are stored in separate objects called nodes.

Each node contains:

Data → the value stored in the node
Pointer/Link → the address of the next node

Unlike arrays, linked list elements are not stored in continuous memory locations. Nodes are connected using links.
'''


##----creating node----##
class Node:
    def __init__(self,value):
        self.value= value
        self.address= None
new_node= Node(10)
print(new_node)



##----creating linked lists----##
class linkedlist:
    def __init__(self,value):
        new_node=Node(value)
        self.head= new_node #it is pointing towards the new node
        self.tail= new_node #it will also point towards the new node
        self.length= 1 #since it is a single node



##----appending element at the end in the linked list----##
def append(self, value):
    new_node= Node(value)
    if self.head is None: #when the list is empty
        self.head= new_node
        self.tail= new_node
    else:#when list already has some data 
        self.tail.next= new_node
        self.tail= new_node
    self.length +=1
new_linked_list= linkedlist()
new_linked_list.append(10)
new_linked_list.append(20)
print(new_linked_list.length)



##----appending element at the beginning of linkedlist----##
def prepend(self,value):
    new_node= Node(value)
    if self.head is None:
        self.head= new_node
        self.tail = new_node
    else:
        new_node.next= self.head
        self.head= new_node
    self.length +=1



##----traversal through single linked list----##
def traverse(self):
    current= self.head
    while current is not None:
        print(current.value)
        current= current.next 
print(new_linked_list.traverse())



##----searching element in single linked list----##
def search(self, target):
    current= self.head
    while current:
        if current.value== target:
            return True
        else:
            return False 
print(new_linked_list.search())



##----get method (we will give index no. and get the value which is in it)----##
def get(self, index):
    if index<0 or index>=self.length:
        return None
    current = self.head
    for _ in range(index):
        current= current.next
    return current.value



##----set method in linked list, it takes the index and value in which we are changing it to----##
def set_value(self,index,value):
    temp= self.get(index)
    if temp: 
        temp.value= value
        return True
    return False



##----poping the head node and making the next node as head node----##
def pop_first(self):
    popped_node= self.head
    self.head= self.head.next
    popped_node.next= None
    self.length-= 1
    return popped_node



##----popping the tail and making the previous one as tail----##
def pop(self):
    popped_node= self.tail
    temp= self.head
    while temp.next is not self.tail:
        temp=temp.next
    self.tail= temp
    temp.next= None



##----remove any specific node of my choice----##
def remove(self, index):
    prev_node = self.get(index - 1)
    popped_node = prev_node.next
    prev_node.next = popped_node.next
    self.length -= 1
    return popped_node



##----delete all nodes----##
def delete_all(self):
    self.head= None
    self.tail= None
    self.length= 0 
    
class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def initialize_empty_node(self,node):
        '''Initializing head and tail node'''
        self.head = node
        self.tail = node
        self.tail.next = node
        return
    
    def insert_at_beginning(self,data):
        node = Node(data)
        if self.head is None:
            return self.initialize_empty_node(node)
        node.next = self.head
        self.head = node
        self.tail.next = self.head

    def insert_at_end(self,data):
        node = Node(data)
        if self.tail is None:
            return self.initialize_empty_node(node)
        self.tail.next = node
        self.tail = node
        self.tail.next = self.head
    
    def display_node(self):
        head = self.head
        value = ''
        while head:
            value += str(head.data)+"------>"
            head = head.next
            if head == self.tail.next:
                break
        print(value)
    
    def delete_from_front(self):
        if self.head is None:
            print("Empty linked list")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            print("Deletion successful and list is empty")
            return
        self.tail.next = self.head.next
        self.head = self.head.next
    
    def delete_from_end(self):
        if self.head is None:
            print("Empty linked list")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            print("Deletion successful and list is empty")
            return
        node = self.head
        while node:
            node = node.next
            if node != self.tail.next:
                break
        node.next = self.head
        self.tail = node
        
circ_ll = CircularLinkedList()
circ_ll.insert_at_beginning(10)
circ_ll.insert_at_beginning(20)
circ_ll.insert_at_beginning(30)
print(circ_ll.display_node())
circ_ll.insert_at_end(40)
print(circ_ll.display_node())
circ_ll.delete_from_front()
print(circ_ll.display_node())
circ_ll.delete_from_end()
print(circ_ll.display_node())
circ_ll.insert_at_beginning(100)
circ_ll.insert_at_end(200)
print(circ_ll.display_node())
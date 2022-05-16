from telnetlib import SE


class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_start(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        if self.head.prev is None and self.head.next is None:
            self.head.prev = node
            self.head.next = node
            node.next = self.head
            node.prev = self.head
            self.head = node
            return 
        self.head.prev = node
        node.next = self.head
        node.prev = self.tail
        self.tail.next = node
        self.head = node


    def insert_at_end(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        if self.tail.prev is None and self.tail.next is None:
            # self.head.prev = node
            self.tail.next = node
            node.prev = self.tail
            node.next = self.head
            self.tail.prev = node
            self.tail = node
            return 
        node.prev = self.tail
        self.tail.next = node
        node.next = self.head
        self.head.prev = node
        self.tail = node

    def display(self):
        print(self.head.prev.data)
        if self.head is None:
            print("LInked list is empty")
            return
        node = self.head
        val = ""
        while node:
            val += str(node.data)+"------->"
            node = node.next
            if node.next == self.head:
                val += str(node.data)+"------->"
                break
        print(val)
    
    def delete_from_start(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.next is None or self.head.prev is None:
            self.head = None
            self.tail = None
            print("successful deletion")
            return
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head
    
    def delete_from_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.next is None or self.head.prev is None:
            self.head = None
            self.tail = None
            print("successful deletion")
            return
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
dcll = CircularDublyLinkedList()
dcll.insert_at_start(1)
dcll.insert_at_start(2)
dcll.insert_at_start(3)
dcll.display()
dcll.insert_at_end(4040)
dcll.insert_at_start(202020)
dcll.insert_at_end(401)
dcll.display()
dcll.delete_from_start()
dcll.display()
dcll.delete_from_end()
dcll.display()



class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        '''call whenever class is initialized and set value to head and tail.'''
        self.head = None
        self.tail = None

    def initialize_empty_node(self,node):
        '''Initializing head and tail node'''
        self.head = node
        self.tail = node
        return
    def insert_at_beginning(self,data):
        '''Insert data at beginning of linked list'''
        node = Node(data)
        if self.head is None:
            return self.initialize_empty_node(node)
        # node.prev = node
        node.next = self.head
        self.head.prev = node
        self.head = node
        return

    def insert_at_end(self,data):
        '''Insert data at end of linked list'''
        node = Node(data)
        if self.head is None:
            return self.initialize_empty_node(node)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        return

    def get_data(self):
        '''return all the data available in linked list'''
        node = self.head
        if node is None:
            print("Node is empty ---> ")
            return
        node_val = ''
        while node:
            node_val+=str(node.data)+"-->"
            node = node.next
        print(node_val)
        return

    def get_data_reverse(self):
        '''display data from backward position.'''
        node = self.tail
        if node is None:
            print("Node is empty ---> ")
            return
        node_val = ''
        while node:
            node_val += str(node.data) + "-->"
            node = node.prev
        print(node_val)
        return

    def search(self,data):
        '''Search for given data in linked and return true or false.'''
        head = self.head
        if head is None:
            return 'Empty Linked List'
        if head.next is None and data!=head.data:
            return 'Data not found'
        temp = head
        while temp!=None:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def delete_from_front(self):
        '''
            delete node from first of linked list
        '''
        node = self.head
        if node is None:
            return 'Linked list is empty'
        if node.next is None and node.prev is None:
            self.head = None
            self.tail = None
            return 'Deletion successful'
        node.next.prev = None
        self.head = node.next
        return 'Deletion successful'
    
    def delete_from_last(self):
        '''
            delete node from last of linked list
        '''
        node = self.tail
        if node is None:
            return 'Linked list is empty'
        if node.next is None and node.prev is None:
            self.head = None
            self.tail = None
            return 'Deletion successful'
        node.prev.next = None
        self.tail = node.prev
        return 'Deletion successful'

dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_beginning(30)
dll.insert_at_beginning(40)
dll.insert_at_end(9)
dll.insert_at_end(8)
dll.get_data()
dll.get_data_reverse()
print(dll.search(2000))
dll.get_data()
print(dll.delete_from_front())
dll.get_data()
dll.delete_from_last()
print("Deleted from last..")
dll.get_data()
dll.insert_at_beginning(200)
dll.get_data()
dll.insert_at_end(4000)
dll.get_data()
 
class Node:
    '''
        Node initialization for linklist
    '''
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    '''Linked list with head and tail initialization to null at first'''
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_start(self,data):
        '''insert data at beginning of linked list'''
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insert_at_end(self,data):
        '''Insert data at last of linked list'''
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insert_at(self,index,data):
        '''insert data at any position of linked list'''
        node = Node(data)
        count = 0
        temp = self.head
        if index == 0 or temp is None:
            # call insert at beginning
            self.insert_at_start(data)
            return
        if temp.next is None:
            self.insert_at_end(data)
            return
        while count < index-1:
            if temp.next is None:
                print("Index out of range")
                return
            temp = temp.next
            count+=1
        node.next = temp.next
        temp.next = node

    def delete_from_start(self):
        self.head = self.head.next
    def show(self):
        '''to display all linked list'''
        node_val = ''
        head = self.head
        while head:
            node_val+=str(head.data)+"-->"
            head = head.next
        return node_val
    def peek(self):
        '''to get top most node of linkedlist'''
        if self.head is None:
            return 'No data'
        return self.head.data

ll = LinkList()
ll.insert_at_start(10)
ll.insert_at_end(30)
ll.insert_at(1,8)
ll.insert_at_start(60)
print(ll.show())
print(ll.peek())

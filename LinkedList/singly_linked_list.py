class Node:
    '''
        Node initialization for linklist
    '''
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    '''Linked list implementation as linked listg '''
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_start(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insert_at_end(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def insert_at_anywhere(self,data,position):
        newNode = Node(data)
        headNode = self.head
        if (position < 0):
            print("Invalid position!")
        if position == 0:
            newNode = Node(data)
            newNode.next = headNode
            self.head = newNode
        else:
            # Keep looping until the position is zero
            while (position != 0):
                position -= 1
                if (position == 1):
                    # Making the new Node to point to
                    # the old Node at the same position
                    newNode.next = headNode.next
                    # Replacing headNode with new Node
                    # to the old Node to point to the new Node
                    headNode.next = newNode
                    break
                headNode = headNode.next
                if headNode == None:
                    break
            if position != 1:
                print("position out of range")
        return self.head

    def show(self):
        node_val = ''
        head = self.head
        while head:
            node_val+=str(head.data)+"-->"
            head = head.next
        return node_val
    def peek(self):
        if self.head is None:
            return 'No data'
        return self.head.data

ll = LinkList()
ll.insert_at_start(10)
ll.insert_at_start(20)
ll.insert_at_start(30)
ll.insert_at_anywhere(21,3)
ll.insert_at_start(200)
ll.insert_at_start(300)
ll.insert_at_end(40)
print(ll.show())
ll.peek()

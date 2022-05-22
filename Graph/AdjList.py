from queue import Queue

class Node:
    def __init__(self, val) -> None:
        self.key = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def insert(self, val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        return self
    
    def iterate(self, src):
        temp = self.head

        print(src, end="::")
        while temp != None:
            print(temp.key, end="-->")
            temp = temp.next

        print(None)
    
    def delete(self, val):

        temp = self.head
        prev = None

        if temp.key == val:
            self.head = temp.next
        else:
            while temp.key != val:
                prev = temp
                temp = temp.next
            
            prev.next = temp.next


# ll = LinkedList()
# ll.insert(5)
# ll.insert(6)
# ll.insert(7)
# ll.insert(8)
# ll.insert(9)
# ll.iterate()
# ll.delete(5)
# ll.iterate()


class AdjList:
    def __init__(self) -> None:
        self.adjList = {}
        self.ll = None

    def insert(self, src, dest):
        if src not in self.adjList:
            self.ll = LinkedList()
        
        self.adjList[src] = self.ll.insert(dest)
    
    def iterate(self):
        for adj_keys in self.adjList:
            self.adjList[adj_keys].iterate(adj_keys)

    def deleteEdge(self, src, dest):
        if src in self.adjList:
            self.adjList[src].delete(dest)

    def bfs(self, start):

        visited = []
        queue = Queue()
        queue.put(start)

        while not queue.empty():
            vertex = queue.get()

            if vertex not in visited and vertex != None:
                visited.append(vertex)
                
                temp = self.adjList[vertex].head

                while temp != None:
                    if temp.key not in visited:
                        queue.put(temp.key)
                    temp = temp.next
                    
        return visited

adjLst = AdjList()
adjLst.insert('A', 'C')
adjLst.insert('A', 'E')

adjLst.insert('B', None)

adjLst.insert('C', 'B')
adjLst.insert('C', 'G')

adjLst.insert('D', None)

adjLst.insert('E', 'H')

adjLst.insert('H', 'D')

adjLst.insert('G', None)


adjLst.iterate()

print(adjLst.bfs('A'))


# print("##############")
# adjLst.deleteEdge(0, 1)
# adjLst.iterate()

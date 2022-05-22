class AdjMatrix:
    """
        Class for creating, searching and deleting edges and vertices using graph representation 
        i.e. adjacency matrix 
    """
    def __init__(self, size) -> None:
        self.adjMatrix = []
        for _ in range(size):
            # initializing n x n matrix
            self.adjMatrix.append([0 for _ in range(size)])
        self.size = size

    def addEdge(self, src, dest):
        """
        Add an edge between two vertices

        Args:
            src (int): origin of the edge.
            dest (int): destination of the edge.
        """
        self.adjMatrix[src][dest] = 1

    def hasEdge(self, src, dest):
        """
        Check if an edge exists between two vertices

        Args:
            src (int): origin of the edge.
            dest (int): destination of the edge.

        Returns:
            boolean: True if an edge exists else False
        """

        if self.adjMatrix[src][dest]:
            return True
        return False

    def deleteEdge(self, src, dest):
        """
        Delete an edge betwwwn vertices

        Args:
            src (int): origin of the edge.
            dest (int): destination of the edge.
        """

        self.adjMatrix[src][dest] = 0

    def showMatrix(self):
        """
        Displaying adjacency matrix of n x n. 
        """
        for i in range(self.size):
            for j in range(self.size):
                print(self.adjMatrix[i][j], end=" ")
            print()


adj = AdjMatrix(5)
adj.addEdge(0,1)
adj.addEdge(0,2)
adj.addEdge(0,3)
adj.addEdge(1,4)
adj.showMatrix()
adj.deleteEdge(0,3)
# adj.deleteEdge(6,3)


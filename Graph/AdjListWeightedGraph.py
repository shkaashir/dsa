from queue import Queue
from math import inf

class GraphAdjList:
    """
        Class for initializing graph adjaceny list
    """
    def __init__(self, num_nodes, edges) -> None:
        """
        Constructor for the class which initializes the given edges

        Args:
            num_nodes (int): _description_
            edges (_type_): _description_
        """
        self.num_nodes = num_nodes
        self.data = {k:{} for k, _, _ in edges}
        for source, destination, weight in edges:
            self.data[source][destination] = weight
        
    def __repr__(self):
        """
        Representaion for the class object.

        Returns:
            str: The detailed format of the initialized data
        """
        return "\n".join([f"{k}: {v}" for k, v in self.data.items()])
    
    def __str__(self):
        """
        String representation of an object.

        Returns:
            str: The detailed format of the initialized data
        """
        return self.__repr__()
    
    def bfs(self, start):
        """

        Breadth First Search Algorithm for the given graph

        Args:
            start (str or int): The starting vertex for the bfs algorithm 

        Returns:
            tuple: The bfs nodes, distance of each node from starting node and the parent of each nodes before visiting the 
                   particular node.
        """

        visited = {k: False for k in self.data} # Keeping track of all the visited node so that it does not visit the nodes which are visited again.

        visited[start] = True # Initializing the souce nodea as visited

        queue = Queue() 

        queue.put(start)

        discovered = [start] # The nodes which have been discoverd starting from the given start node

        distance = {k:0 for k in self.data} # Keeps track of the distance from starting node. 

        parent = {k:None for k in self.data} # Keeps track of the parent node which was visited before the current node.

        while not queue.empty():

            vertex = queue.get()

            for ver in self.data[vertex]:
                if visited[ver] == False:
                    visited[ver] = True
                    distance[ver] = 1 + distance[vertex]
                    discovered.append(ver)
                    parent[ver] = vertex
                    queue.put(ver)
        
        return discovered, distance, parent

    
    def dijkstra_algorithm(self, source, destination):
        """
        Dijkstra Algorithm for find the shortest path from the given source node to its destination. 
        This algorithm is widely used when the given graph is a weighted graph however it can work on 
        unweighted graph as well.

        Args:
            source (str): Where we are starting from.
            destination (str): Where we want to reach.
        """

        shortest_distance = {k:inf for k in self.data} # Initially, we are unknown of the shortest distance from the source nodes to all the other nodes 
                                                       # so we initiaize the distance to infinity for now. However we do know the distance of 
                                                       # starting node which is 0 because we are already there to begin with.

        shortest_distance[source] = 0 # Initializing the starting node distance to 0

        visited = {k: False for k in self.data} # Keeping track of visited nodes.

        visited[source] = True

        queue = Queue()

        queue.put(source)

        previous_node = {k: None for k in self.data} # Keeping track of the predecessars for backtracking from the destination to the source
                                                     # after the algorithm has determined the lowest cost for all the other nodes.

        path = []

        try:
            
            while not queue.empty():
                
                vertex = queue.get()
                
                # update the estimates
                for child_node, weight in self.data[vertex].items():
                    if weight + shortest_distance[vertex] < shortest_distance[child_node]:
                        shortest_distance[child_node] = weight + shortest_distance[vertex]
                        previous_node[child_node] = vertex

                # decide the minimun next vertex
                min_node = None
                for node, v in visited.items():
                    if v == False:
                        if min_node is None:
                            min_node = node
                        elif shortest_distance[node] < shortest_distance[min_node]:
                            min_node = node
                
                if min_node != None:
                    visited[min_node] = True
                    queue.put(min_node)
            
            current_node = destination

            while current_node != source:
                path[:0] = [current_node]
                current_node = previous_node[current_node]
            
            path[:0] = [source]


            if shortest_distance[destination] != inf:
                print(f"The least-cost path between {source} and {destination} is {'-->'.join(path)} having cost {shortest_distance[destination]}")
        
        except KeyError as e:
            print(f"{e} does not exist.")


if __name__ == "__main__":
    num_nodes = 7
    edges = [('a','c',3), ('a','f',2), ('b','d',1), ('b','e',2), ('b','f',6), ('b','g',2), ('c','a',3),
             ('c','d',4), ('c','e',1), ('c','f',2), ('d','b',1), ('d','c',4), ('e','b',2), ('e','c',1),
             ('e','f',3), ('f','a',2), ('f','b',6), ('f','c',2), ('f','e',3), ('f','g',5), ('g','b',2),
             ('g','f',5)]

    num_nodes1 = 5
    edges1  = [('a','b',7), ('a','c',3), ('b','a',7), ('b','c',1), ('b','d',2), ('b','e',6), ('c','a',3),
               ('c','b',1), ('c','d',2), ('d','c',2), ('d','b',2), ('d','e',4), ('e','b',6), ('e','d',4)]

    num_nodes2 = 5
    edges2 = [('Tokyo', 'Portland', 4816), ('Tokyo', 'Rome', 6161), ('Tokyo', 'Auckland', 35497),
              ('Portland', 'Tokyo', 4816), ('Portland', 'Rome', 5795), ('Portland', 'Buenos Aires', 6849),
              ('Rome', 'Tokyo', 6161), ('Rome', 'Portland', 5795), ('Rome', 'Auckland', 11462),
              ('Buenos Aires', 'Portland', 6849), ('Buenos Aires', 'Auckland', 6415),
              ('Auckland', 'Buenos Aires', 6415), ('Auckland', 'Rome', 11462), ('Auckland', 'Tokyo', 35497)]


    graph1 = GraphAdjList(num_nodes, edges)
    # print(graph1.bfs('a'))
    graph1.dijkstra_algorithm('a','b')

    graph2 = GraphAdjList(num_nodes1, edges1)
    # print(graph1.bfs('a'))
    graph2.dijkstra_algorithm('a','e')

    graph3 = GraphAdjList(num_nodes2, edges2)
    # print(graph1.bfs('a'))
    graph3.dijkstra_algorithm('Rome', 'Buenos Aires')




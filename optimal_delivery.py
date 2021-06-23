"""
Author: Ng Wei Han
"""

class Heap():
    """
    Class representing MinHeap data structure.
    """
    def __init__(self, max_size):
        """
        Initialization of Heap object.

        :param max_size: An integer representing the maximum size of the heap

        Best/Worst Time Complexity: O(1)
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        self.length = 0
        self.the_array = [None for _ in range(max_size+1)]

    def __len__(self):
        """
        Return the total length of heap. 

        :return: An integer representing length of heap

        Best/Worst Time Complexity: O(1)
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        return self.length

    def is_full(self):
        """
        Check if the heap is full. 

        :return: True if heap is full; else False

        Best/Worst Time Complexity: O(1)
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        return self.length + 1 == len(self.the_array)

    def rise(self, element):
        """
        Rise element at index k to its correct position
        
        :param element: A vertex object
        :return: Integer representing index of vertex

        Best Time Complexity: O(1) - When element is at correct position
        Worst Time Complexity: O(log V) - When element is the smallest and at last position
        V - Number of vertices in the heap
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        k = element.index
        while k > 1 and self.the_array[k].distance < self.the_array[k // 2].distance:
            self.swap(k, k // 2)
            k = k // 2
        return element.index
        
    def add(self, element):
        """
        Swaps elements while rising

        :param element: A vertex object
        :return: Integer representing index of vertex

        Best Time Complexity: O(1) - When element is at correct position
        Worst Time Complexity: O(log V) - When element is the smallest and at last position
        V - Number of vertices in the heap
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        has_space_left = not self.is_full()

        if has_space_left:
            self.length += 1
            self.the_array[self.length] = element
            self.rise(element)

        return element.index

    def smallest_child(self, k):
        """
        Returns the index of the largest child of k.
        
        :param k: An integer representing index of vertex
        :return: An integer representing index of smallest child

        Best/Worst Time Complexity: O(1)
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        if 2 * k == self.length or self.the_array[2 * k].distance < self.the_array[2 * k + 1].distance:
            return 2*k
        else:
            return 2*k+1

    def sink(self, element):
        """ 
        Make the element at index k sink to the correct position 
        
        :param element: A vertex object
        :return: Integer representing index of vertex

        Best Time Complexity: O(1) - When element is at correct position
        Worst Time Complexity: O(log V) - When element is the biggest and at first position
        V - Number of vertices in the heap
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        k = element.index
        while 2*k <= self.length:
            child = self.smallest_child(k)
            if self.the_array[k].distance <= self.the_array[child].distance:
                break
            self.swap(child, k)
            k = child

        return element.index

    def swap(self,a,b):
        """
        Swapping the position of two elements in an array.

        :param a: First element to be swapped
        :param b: Second element to be swapped 

        Best/Worst Time Complexity: O(1)
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        self.the_array[a],self.the_array[b] = self.the_array[b],self.the_array[a]
        self.the_array[a].index,self.the_array[b].index = self.the_array[b].index,self.the_array[a].index

    def replace(self,index,new_distance):
        """
        Replacing the value of a vertex and rise/sink to correct position.

        :param index: An integer representing index of vertex
        :param new_distance: An integer representing the updated distance
        :return: An integer representing the new index of vertex

        Best Time Complexity: O(1)
        Worst Time Complexity: O(log V)
        V - Number of vertices in the heap
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        # Set new distance
        self.the_array[index].distance = new_distance
        self.the_array[index].replaced = True

        # Rise
        new_index = self.rise(self.the_array[index]) 

        # Sink
        if new_index == index:
            new_index = self.sink(self.the_array[index])

        return new_index

    def serve(self):
        """
        Serving the vertex which is the root.

        :return: The vertex which is served

        Best Time Complexity: O(1) - When element is at correct position
        Worst Time Complexity: O(log V) - When element is the biggest and at first position
        V - Number of vertices in the heap
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        # Swap root and last element
        self.swap(1,self.length)

        item = self.the_array[self.length]
        item.served = True
        self.length -= 1

        # Perform sink
        self.sink(self.the_array[1])

        return item

#%%
class Graph:
    def __init__(self,V):
        """
        Initialization of Graph object

        :param V: Number of vertices

        Best/Worst Time Complexity: O(V)
        V - Number of vertices
        Total Space Complexity: O(V)
        Auxiliary Space Complexity: O(V)
        """
        # array
        self.vertices = [None]*2*V
        self.heap = Heap(2*V)
        self.V = V

        # 1st graph
        for i in range(V):
            vertex = Vertex(i,i+1)
            self.vertices[i] = vertex
            self.heap.add(vertex)
        
        # Fake graph 
        for i in range(V,2*V):
            vertex = Vertex(i,i+1)
            self.vertices[i] = vertex
            self.heap.add(vertex)

    def add_edges(self,argv_edges):
        """
        Add edges for each vertex.

        :param argv_edges: Array which contains tuple representing predecessor,successor and weight

        Best/Worst Time Complexity: O(n)
        n - Number of elements in argv_edges
        Total Space Complexity: O(n)
        Auxiliary Space: O(1)
        """
        for edge in argv_edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]

            # Add front edge
            current_edge = Edge(u,v,w)
            current_vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)

            # Add back edge
            current_edge = Edge(v,u,w)
            current_vertex = self.vertices[v]
            current_vertex.add_edge(current_edge)

    def dijkstra(self,source,delivery):
        """
        Find the shortest distance from source vertex to every other vertices using Dijkstra algorithm.

        :param source: An integer representing the starting vertex
        :param delivery: Tuple of 3 values, where first value is the pickup city, second value is the delivery city
        
        Best/Worst Time Complexity: O(Rlog(N))
        R - Total number of roads
        N - Total number of cities
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        
        """
        # Set source distance to 0
        distance = 0
        self.heap.replace(source+1,distance)

        delivered = False

        # While not all vertices are served
        while len(self.heap) > 0:
            source = self.heap.serve()
            for edge in source.edges:
                current_weight = source.distance
                v = self.vertices[edge.v]
                w = edge.w

                new_distance = current_weight + w

                # Check for delivery
                if not delivered and delivery[0] == source.id and delivery[1] == v.id:
                    new_distance -= delivery[2]
                    delivered = True

                # Update shortest distance
                if new_distance < v.distance and not v.served:
                    self.heap.replace(v.index,new_distance)
                    v.previous = source
                    
    def get_ans(self,end):
        """
        Find the final cost and its path to obtain the value.

        :param end: Integer in the range of [0,n-1],representing city
        :return: Tuple containing 2 elements which are cost of travelling from start city to end city and
        profit made from delivery.

        Best/Worst Time Complexity: O(Rlog(N))
        R - Total number of roads
        N - Total number of cities
        Total Space Complexity: O(Rlog(N))
        Auxiliary Space Complexity: O(Rlog(N))
        """

        # Compare between end vertex of two graphs
        ans = None
        if self.vertices[end].distance <= self.vertices[end+self.V].distance:
            ans = self.vertices[end]
            is_second_graph = False
            
        else: 
            ans = self.vertices[end+self.V]
            is_second_graph = True

        cost = ans.distance

        # Perform backtracking
        res = []
        if is_second_graph: 
            res.append(ans.id - self.V)
        else:
            res.append(ans.id)
        
        while True:
            prev = ans.previous
            if prev is None: 
                break
            elif ans.id-self.V == prev.id or ans.id+self.V == prev.id:
                ans = prev
                continue
            else:
                if self.V > prev.id:
                    res.append(prev.id)
                else: 
                    res.append(prev.id-self.V)
                ans = prev

        # Reverse list
        res.reverse()

        return (cost,res)
#%%

class Vertex:
    def __init__(self,id,index,distance=float('inf')):
        """
        Initialization of Vertex object.

        :param id: Unique identification of each object
        :param index: Current position of vertex
        :param distance: Current distance of vertex

        Best/Worst Time Complexity: O(1)
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        self.id = id
        self.index = index
        self.edges = []
        self.distance = distance
        self.served = False
        self.previous = None

    def add_edge(self,edge):
        """
        Add edges of a Vertex object

        Best/Worst Time Complexity: O(1)
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        self.edges.append(edge)

class Edge:
    """
    An edge class representing the connection between vertices.
    """
    def __init__(self,u,v,w):
        """
        Initialization of Edge object.

        :param u: An integer representing ID of predecessor
        :param v: An integer representing ID of successor
        :param w: An integer representing the weight

        
        Best/Worst Time Complexity: O(1)
        Total Space Complexity: O(1)
        Auxiliary Space Complexity: O(1)
        """
        self.u = u
        self.v = v
        self.w = w

#%%
def opt_delivery(n,roads,start,end,delivery):
    """
    A function which minimizes the cost of travelling and maximizes the profit from delivery

    :param n: The number of cities, numbered from 0 to n-1
    :param roads: List of tuples in form of (u,v,w)
    u,v - Road between the cities
    w - Cost of travelling along the road
    :param start: Integer in the range of [0,n-1],representing city
    :param end: Integer in the range of [0,n-1],representing city
    :param delivery: Tuple of 3 values, where first value is the pickup city, second value is the delivery city
    and third value is the amount of money to be made from pickup city to delivery city. 
    :return: Tuple containing 2 elements which are cost of travelling from start city to end city and
    profit made from delivery. 

    Best/Worst Time Complexity: O(Rlog(N))
    R - Total number of roads
    N - Total number of cities
    Total Space Complexity: O(Rlog(N))
    Auxiliary Space Complexity: O(Rlog(N))
    """
    # Preprocess
    temp = []
    for edge in roads:
        u,v,w = edge
        new_edge = (u+n,v+n,w)
        temp.append(new_edge)

    roads = roads+temp
    
    # Preprocess - Connection between 2 graphs
    first_conn = (delivery[0],delivery[0]+n,0)
    second_conn = (delivery[1],delivery[1]+n,0)
    roads.append(first_conn)
    roads.append(second_conn)

    my_graph = Graph(n)
    my_graph.add_edges(roads)
    my_graph.dijkstra(start, delivery)
    ans = my_graph.get_ans(end)
    return ans
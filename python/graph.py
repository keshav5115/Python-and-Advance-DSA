'''

A graph is a data structure used to represent relationships between pairs of objects. 
It consists of a set of vertices (also called nodes) and 
a set of edges (connections between pairs of vertices). 

Graphs are widely used to model various real-world systems such as networks, maps, and social interactions.

Components of a Graph:

    Vertices (Nodes): These are the fundamental units of a graph. 
                    They represent entities such as locations, people, or devices.
    Edges (Arcs/Links): These are the connections between the vertices, 
                    representing relationships or pathways. An edge connects two vertices.

'''



from collections import defaultdict,deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Using defaultdict to automatically initialize empty lists for each vertex
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Add the reverse direction for undirected graphs


    def dfs(self, start, visited):
        visited=set()
        queue= [start]
        result=[]
        while queue:
            node = queue.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result
    
    def bfs(self, start, visited):
        visited=set()
        queue= deque([start])
        result=[]
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result
    
    def find_shortest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            return []
        
        visited = set()
        queue = deque([(start, [start])])
        while queue:
            node, path = queue.popleft()
            if node == end:
                return path
            
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        
        return path
    def find_longest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            return []
        
        visited = set()
        queue = deque([(start, [start])])
        max_path = []
        
        while queue:
            node, path = queue.popleft()
            if node == end:
                if len(path) > len(max_path):
                    max_path = path
            
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        
        return max_path
    def find_shortest_distance(self,start,end):
        if start not in self.graph or end not in self.graph:
            return -1
        
        visited = set()
        queue = deque([(start, 0)])
        distance = -1
        
        while queue:
            node, curr_distance = queue.popleft()
            if node == end:
                distance = curr_distance
                break
            
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, curr_distance + 1))
        
        return distance
    

# Test the Graph class

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2,3)

print("Adjacency list representation:")

for vertex in g.graph:
    print(f"{vertex} -> {g.graph[vertex]}")

print("Graph representation")

for vertex in g.graph:
    for neighbor in g.graph[vertex]:
        print(f"{vertex} -> {neighbor}")
    print()

print("Adjacency matrix representation")

matrix = [[0]*len(g.graph) for _ in range(len(g.graph))]

for i, vertex in enumerate(g.graph):
    for neighbor in g.graph[vertex]:
        matrix[i][neighbor] = 1
        matrix[neighbor][i] = 1

for row in matrix:
    print(row)
    print()



print("DFS traversal from node 0:", g.dfs(1, set()))

print("BFS traversal from node 0:", g.bfs(1, set()))

print("Shortest path from node 0 to node 3:", g.find_shortest_path(0, 3))


    
# 1.) DEF: Graphs are those types of non-linear data structures which consist of a definite
# quantity of vertices/nodes and edges. The vertices or the nodes are involved in storing data and
# the edges show the vertices relationship.
# nodes are data elements of graph
# 3.)  Diff between Tree and Graph
# Every tree is a graph, but every graph is not tree


# 2.) graphs used in:
# a.) GPS
# b.)Google Maps
# c.)Google search
# d.)Ecommerce for recommendations
# e.)To show the connection between the users
# f.)Frends suggestions.


# 4.)
# a.) Graph does not have root node here all nodes are equal
# b.) We have multiple path to join two or more nodes

# Types of graphs
# 1.)directed Graph(Edges are unidirectional)
# 2.)undirected Graph(All edges are bidirectional)

# 1.)weighted graph --> each edge is assigned with value or cost or weight
# 2.)un weighted graph --> edge does not have any value

# 1.)cyclic graph --> if there is a path which starts with a vertex and ends with same vertex. -> (all vertices have to be distinct)
# 2.)Acyclic graph --> There wont be any path which starts with a vertex and ends with same vertex(eg:tree)


# 5.) Adjesent node / Neignbour node
# If node x is adjacent to node y, if there is an edge from node x to y
#               EG: A ------>---- B  --> Here A is adjacent to B, but B is not adjacent to A

# 6.)Path
# path is a sequence of vertices(nodes), in which pair of some nodes is connected by edges
# length of path  =  number of edges along that path

# a.)simple path --> If all vertices are distinct(unique)
# b.)closed  path --> if 1st and last node of path is same but vertices can be repeated

# 7.)In undircted graph
#  Connected Graph --> if there is a path between every pair of node in a graph
# NOTE: mostly connected graph term is used in undircted graph

# 8.)
# Degree of a node
# it is num of edges connected to the node

# Indegree --> num of edges comming towards that node
# outdegree ---> num of edges going apart from that node
# 9.)
# complete graph --> if there is an edge between every pair of node in a graph

# A -> B
# A -> C
# B -> C
# B -> D
# C -> D
# D -> C
# E -> F
# F -> C


graph = {'A':['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

from collections import defaultdict,deque
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


print(find_path(graph, 'A', "C"))

def find_shortest_distance(graph,start,end):
        if start not in graph or end not in graph:
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
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, curr_distance + 1))
        
        return distance
def find_shortest_path(graph, start, end):
        if start not in graph or end not in graph:
            return []
        
        visited = set()
        queue = deque([(start, [start])])
        while queue:
            node, path = queue.popleft()
            if node == end:
                return path
            
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        
        return path
print(find_shortest_path(graph, 'A', 'C'))
print(find_shortest_distance(graph, 'A', 'C'))


# https://www.python.org/doc/essays/graphs/

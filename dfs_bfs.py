# DFS // BFS

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()

def BFS(startingNode):
    
    # implementing BFS
    # assume all nodes are marked as not visited
    queue = []
    queue.append(startingNode)
    startingNode.visited = True

    while len(queue) != 0:
        # Remove the first node
        queue.pop(0)

        for n in graph(s):
            if (n.visited == False):
                queue.append(n)
                n.visisted = True

def DFS(n, graph, visited:set):
    if (n not in visited):
        print (n)
        visited.add(n)
        # Iterate the adjacency list and call DFS
        for neighborNode in graph[n]:
            DFS(neighborNode, graph, visited)

# Call the function with a starting node
DFS("A",graph,visited)






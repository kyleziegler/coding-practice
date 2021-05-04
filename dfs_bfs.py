# DFS // BFS

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = ()

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

def DFS(n:Node, graph, visited:set):
    visited.add(n)
    
    if (n not in visited):
        DFS(n.firstUnvisitedNode, visistedArr)
        print(n)

DFS(n,graph,visited)






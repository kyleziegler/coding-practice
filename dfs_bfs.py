from os import listdir
from os import walk
from os.path import isfile, join



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
# DFS("A",graph,visited)


class Tree():
    def __init__(self, root):
        self.root = root
        self.children = []
    def addNode(self , obj):
        self.children.append(obj)

class Node():
    def __init__(self, data):
        self.data = data
        self.children = []
    def addNode (self, obj):
        self.children.append(obj)


def reformat(string_list):
    folders = string_list.split('/')
    tree = node = {}

    # for i,j in enumerate(folders):
    #     if (node[folders[i]] is not None):
    #         node[folders[i]] = {level: i, children:{}}



    for s in string_list:
        # start pulling off files - str.split('/')
        string = ""
        for i,j in enumerate(s.split('/')):
            if (j == ""):
                continue
            if (i == 1):
               tree = Tree(j)
               continue
            tree.addNode(j)
            string += "-- " + j
            string += "\n" + "\t"*i
        print(string)

print(reformat(["/Users/kyleziegler/Desktop/repos/coding_practice"]))






















def expandDir(d):
    working_list = []
    for (dirpath, dirnames, filenames) in walk(d):
        working_list.extend(filenames)
    return working_list

def print_file_dir(file_strings:list):
    tree = []

    for s in file_strings:
        # listdir will give you files and directories
        # We need to keep going with folders, as they can still have files
        tree.append([s,expandDir(s)])

        # Just for files
        # tree.append([f for f in listdir(s) if isfile(join(s, f))])

    return tree

# print(print_file_dir(["/Users/kyleziegler/Desktop/repos/coding_practice"]))
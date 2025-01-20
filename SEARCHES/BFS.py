def  BFS(graph,start_node):
    #initialize a queue and add the start_node.
    #this queue contains nodes that should be expanded.
    queue=[start_node]
    #initialize a set to keep the visited nodes
    visited=[]
    #add the start_node to the visited
    visited.append(start_node)
    #while the queue is not empty, remove the node in the first position.
    while queue:
        currentnode=queue.pop(0)
        #process the current node
        print(currentnode)
        #iterate over the neighbours of the current node
        for neighbour in graph[currentnode]:
            #if the neighbour has not been visited before
            if neighbour not in visited:
                #add to list of visited
                visited.append(neighbour)
                #and add to the queue
                queue.append(neighbour)
               

graph={
    5:[3,7],
    3:[2,4],
    7:[8],
    2:[],
    4:[8],
    8:[]
}
print("BFS Traversal:")
BFS(graph,3)
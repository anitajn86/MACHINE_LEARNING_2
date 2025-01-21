def DFS_Iterative(graph,start_node):
    #create a stack and and a set of visited nodes.
    visited=[]
    stack=[]
    #add the start_node to the stack
    stack.append(start_node)
    #create a loop to visit the nodes
    while stack:
        current_node=stack.pop()
        if current_node not in visited:
            #process the current node
            print(current_node)
            #add to the visited list and then extend the graph (/add neighbours)
            visited.append(current_node)
            stack.extend(graph[current_node])

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

DFS_Iterative(graph,'A')

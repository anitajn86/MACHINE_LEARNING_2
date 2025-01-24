import heapq
def UCS(graph,start,goal):
    #create a priority queue to store nodes with their cummulative costs
    pq=[]
    #start with the starting node at cost 0
    heapq.heappush(pq,(0,start))
    #create a dictionary to store the final minimum cost for reaching each node.
    cost_sofar={start:0}
    #to reconstruct the path if needed
    parent={start:None}

    while pq:  #or while not pq.isempty():
        #get the node with the minimum cost
        current_cost,current_node=heapq.heappop(pq)
        #if the goal is reached, reconstruct and return the path
        if current_node==goal:
            path=[]
            while current_node is not None: #i think this is while the current node is not 
                #the starting node
                path.append(current_node) #add the current node/goal to the path
                current_node=parent[current_node] #update current node to its parent
                #the while loop starts from the goal and traces back through its parents
                #until we reach the start node whose parent is None
                path.reverse() #reverse the path to get start to goal order
            return current_cost,path
        
        #explore the neighbours
        for neighbour,cost in graph[current_node]:
            new_cost=current_cost+cost
            #if it is cheaper way to the neighbour, update cost and parent
            if neighbour not in cost_sofar or new_cost<cost_sofar[neighbour]: #or if neighbour not in visited
                cost_sofar[neighbour]=new_cost
                parent[neighbour]=current_node
                heapq.heappush(pq,(new_cost,neighbour))

    #if goal is not reachable,
    return "Goal is not reachable",[]

graph={
    'A':[('B',1),('C',4)],
    'B':[('A',1),('D',2),('E',5)],
    'C':[('D',1),('F',1)],
    'D':[('B',2)],
    'E':[('B',5),('F',3)],
    'F':[('C',1),('E',3)],
}
start='A'
goal='F'

cost,path=UCS(graph,start,goal)
print("Cost:",cost)
print("Path:",path)
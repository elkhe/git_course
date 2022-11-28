root_sample = 0
edges_sample = [[1,2], [3,4,5], [6,7], [], [8, 9], [], [10], [], [], [], []]

visited = [0]*len(edges_sample)
order = []

def dfs(root, edges):
    order.append(root)
    visited[root] = 1
    for node in edges[root]:
        if not visited[node]:
            dfs(node, edges) 
    return  order


#Not the best code. Remake required
def bfs(root, edges, next_level_nodes = []):
    this_level_nodes = next_level_nodes
    next_level_nodes = []

    if not visited[root]:
        visited[root] = 1
        order.append(root)
        this_level_nodes = edges[root]
    
    for node in this_level_nodes:
        visited[node] = 1
        order.append(node)
        next_level_nodes += edges[node]

    if len(next_level_nodes) != 0:
        bfs(root, edges, next_level_nodes)

    return order
    

print(dfs(root_sample, edges_sample))

visited = [0]*11
order.clear()

print(bfs(root_sample, edges_sample))


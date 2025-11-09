from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    visited.add(start)
    
    while queue:
        current=queue.popleft()
        print(current,end=' ')
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS Traversal:")
bfs(graph, 'A')


# from collections import deque
# def bfs(graph,start,target):
#     visited=set()
#     queue=deque([start])
#     visited.add(start)
    
#     while queue:
#         current=queue.popleft()
#         if current==target:
#             print(True)
#             return 
        
#         for neighbor in graph[current]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)
#     print(False)           
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

# print("BFS Traversal:")
# bfs(graph, 'A','F')
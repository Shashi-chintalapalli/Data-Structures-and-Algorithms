import heapq  # we use this for the priority queue

def dijkstra(graph, start):
    # Step 1: Initialize distances
    distances = {node: float('inf') for node in graph}  # infinity for all
    distances[start] = 0  # distance to start node = 0
    
    # Step 2: Initialize previous nodes (for path reconstruction)
    previous = {node: None for node in graph}
    
    # Step 3: Priority queue -> (distance, node)
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Step 4: Skip if we already found a shorter path
        if current_distance > distances[current_node]:
            continue
        
        # Step 5: Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight  # possible new path distance
            
            # Step 6: Relaxation — if new path is shorter, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous


# Run the algorithm
distances, previous = dijkstra(graph, 'A')

print("Shortest distances:", distances)
print("Previous nodes:", previous)

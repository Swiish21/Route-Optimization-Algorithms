import heapq

def dijkstra(graph, start):
    # priority queue to store (cost, node)
    pq = [(0, start)]
    distances = {start: 0}
    distances[start] = 0
    
    while pq:
        current_distance, current_node = heapq.headpop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances


graph = {
    'Nairobi': {'Mombasa': 485, 'Nakuru': 160},
    'Nairobi': {'Kisumu': 355, 'Eldoret': 310},
    'Nairobi': {'Garissa': 355, 'Nakuru': 160},
    'Nakuru': {'Kisumu': 180, 'Eldoret': 140},
    'Mombasa': {'Malindi': 120, 'Garissa':470}
}

#finding shortest paths from 'A'
shortest_routes = dijkstra(graph, 'Nakuru')
print(shortest_routes)
import heapq

def dijkstra(graph, start):
    # Priority queue to store (cost, node)
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)  # Fix: Correct function name

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Corrected Graph with Proper Structure
graph = {
    'Nairobi': {'Mombasa': 485, 'Nakuru': 160, 'Kisumu': 355, 'Eldoret': 310, 'Garissa': 370},
    'Nakuru': {'Nairobi': 160, 'Kisumu': 180, 'Eldoret': 140},
    'Kisumu': {'Nairobi': 355, 'Nakuru': 180, 'Eldoret': 120},
    'Eldoret': {'Nairobi': 310, 'Nakuru': 140, 'Kisumu': 120},
    'Mombasa': {'Nairobi': 485, 'Malindi': 120, 'Garissa': 470},
    'Garissa': {'Nairobi': 370, 'Mombasa': 470},
    'Malindi': {'Mombasa': 120}
}

# Finding shortest paths from 'Nakuru'
shortest_routes = dijkstra(graph, 'Nakuru')
print(shortest_routes)

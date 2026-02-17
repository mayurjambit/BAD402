import heapq

# Graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 0
}

def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    closed = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        closed.add(current)

        for neighbor, cost in graph[current]:
            if neighbor in closed:
                continue

            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current

    return None


path = astar('A', 'F')
print("Optimal Path:", path)
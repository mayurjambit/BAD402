# AO* Algorithm Implementation

class AOStar:
    def __init__(self, graph, heuristic, start):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.solution = {}

    def ao_star(self, node):
        print("Expanding Node:", node)

        # If node is not in graph, it's terminal
        if node not in self.graph:
            return self.heuristic[node]

        min_cost = float('inf')
        best_path = None

        # For each possible AND/OR combination
        for option in self.graph[node]:
            cost = 0
            sub_path = []

            for child, weight in option:
                cost += weight + self.ao_star(child)
                sub_path.append(child)

            if cost < min_cost:
                min_cost = cost
                best_path = sub_path

        self.heuristic[node] = min_cost
        self.solution[node] = best_path
        return min_cost

    def get_solution(self):
        self.ao_star(self.start)
        return self.solution


# Example AND-OR graph
graph = {
    'A': [[('B', 1), ('C', 1)],   # AND node (B AND C)
          [('D', 1)]],           # OR node (D)
    'B': [[('E', 1)], [('F', 1)]],
    'C': [[('G', 1)]]
}

heuristic = {
    'A': 1,
    'B': 6,
    'C': 2,
    'D': 12,
    'E': 2,
    'F': 3,
    'G': 2
}

ao = AOStar(graph, heuristic, 'A')
solution = ao.get_solution()

print("\nOptimal Solution Graph:")
for node in solution:
    print(node, "->", solution[node])
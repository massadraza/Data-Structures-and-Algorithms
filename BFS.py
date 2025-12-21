from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

# Testing
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [6, 7],
    4: [8],
    5: [9],
    6: [10],
    7: [],
    8: [],
    9: [],
    10: []
}

print(bfs(graph, 1))
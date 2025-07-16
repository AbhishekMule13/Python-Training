from collections import deque

# BFS function
def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print("Visited:", node)

        if node == goal:
            print("Goal found:", node)
            return

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    print("Goal not found")

# Take graph input from user
graph = {}
n = int(input("How many nodes? "))

for i in range(n):
    node = input(f"Enter node name {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

# Take start and goal input
start = input("Enter start node: ")
goal = input("Enter goal node: ")

# Run BFS
bfs(graph, start, goal)

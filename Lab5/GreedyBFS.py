from heapq import heappush, heappop

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = []
    heappush(pq, (heuristic(start, goal), start))

    visited = set()
    came_from = {}

    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    while pq:
        _, current = heappop(pq)

        if current == goal:
            # reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1] + [goal]

        visited.add(current)

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue
                if neighbor in visited:
                    continue

                came_from[neighbor] = current
                heappush(pq, (heuristic(neighbor, goal), neighbor))

    return None
grid = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

print(greedy_bfs(grid, start, goal))
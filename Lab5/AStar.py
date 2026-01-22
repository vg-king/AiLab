from heapq import heappush, heappop

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heappush(open_set, (0, start))  # (f_score, node)
    
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    came_from = {}

    directions = [(0,1), (0,-1), (1,0), (-1,0)]  # R, L, D, U

    while open_set:
        current_f, current = heappop(open_set)

        if current == goal:
            # reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1] + [goal]

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            # Check boundaries
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue  # obstacle

                tentative_g = g_score[current] + 1

                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heappush(open_set, (f_score[neighbor], neighbor))

    return None  # no path found


# Example grid
# 0 = free, 1 = obstacle
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
]

start = (0, 0)
goal = (3, 4)

path = a_star(grid, start, goal)
print("Path:", path)

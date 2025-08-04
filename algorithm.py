from collections import deque

def bfs(maze, start, end):
    frontier = deque([(start, [start])])
    visited = {start}
    while frontier:
        current, path = frontier.popleft()
        yield visited  # Yield visited cells at each step

        if current == end:
            yield visited  # Final visited cells
            yield path     # Yield the chosen path
            return

        for y, x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_y, next_x = current[0] + y, current[1] + x
            if 0 <= next_y < len(maze) and 0 <= next_x < len(maze[0]):
                if maze[next_y][next_x] != '#' and (next_y, next_x) not in visited:
                    visited.add((next_y, next_x))
                    frontier.append(((next_y, next_x), path + [(next_y, next_x)]))
    yield visited
    yield None

def dfs(maze, start, end):
    stack = [(start, [start])]
    visited = {start}
    while stack:
        current, path = stack.pop()
        yield visited  # Yield visited cells at each step

        if current == end:
            yield visited  # Final visited cells
            yield path     # Yield the chosen path
            return

        for y, x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_y, next_x = current[0] + y, current[1] + x
            if 0 <= next_y < len(maze) and 0 <= next_x < len(maze[0]):
                if maze[next_y][next_x] != '#' and (next_y, next_x) not in visited:
                    visited.add((next_y, next_x))
                    stack.append(((next_y, next_x), path + [(next_y, next_x)]))
    yield visited
    yield None

def gbfs(maze, start, end):
    from queue import PriorityQueue

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    frontier = PriorityQueue()
    frontier.put((0, start))
    visited = {start}
    came_from = {start: None}

    while not frontier.empty():
        current = frontier.get()[1]
        yield visited  # Yield visited cells at each step

        if current == end:
            yield visited  # Final visited cells
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            yield path[::-1]  # Yield the chosen path
            return

        for y, x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_y, next_x = current[0] + y, current[1] + x
            next_pos = (next_y, next_x)
            if 0 <= next_y < len(maze) and 0 <= next_x < len(maze[0]):
                if maze[next_y][next_x] != '#' and next_pos not in visited:
                    visited.add(next_pos)
                    priority = heuristic(end, next_pos)
                    frontier.put((priority, next_pos))
                    came_from[next_pos] = current
    yield visited
    yield None

def a_star(maze, start, end):
    from queue import PriorityQueue

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    frontier = PriorityQueue()
    frontier.put((0, start))
    visited = {start}
    g_score = {start: 0}
    h_score = {start: heuristic(start, end)}
    came_from = {start: None}

    while not frontier.empty():
        current = frontier.get()[1]
        yield visited  # Yield visited cells at each step

        if current == end:
            yield visited  # Final visited cells
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            yield path[::-1]  # Yield the chosen path
            return

        for y, x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_y, next_x = current[0] + y, current[1] + x
            next_pos = (next_y, next_x)
            if 0 <= next_y < len(maze) and 0 <= next_x < len(maze[0]):
                if maze[next_y][next_x] != '#':
                    tentative_g_score = g_score[current] + 1
                    if next_pos not in g_score or tentative_g_score < g_score[next_pos]:
                        came_from[next_pos] = current
                        g_score[next_pos] = tentative_g_score
                        h_score[next_pos] = tentative_g_score + heuristic(next_pos, end)
                        if next_pos not in visited:
                            visited.add(next_pos)
                            frontier.put((h_score[next_pos], next_pos))
    yield visited
    yield None
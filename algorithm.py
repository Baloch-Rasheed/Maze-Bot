from collections import deque
#Best-First Search Algorithm
def bfs(maze, start, end):
    """
    the Maze is a text of #'s refered as walls and spaces as paths.
    the start and end are tuples representing the coordinates in the maze.
    """

    frontier = deque([(start, [start])])
    visited = {start}
    while frontier:
        current, path = frontier.popleft()

        if current == end:
            return path

        for y, x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_y, next_x = current[0] + y, current[1] + x

            if 0 <= next_y < len(maze) and 0 <= next_x < len(maze[0]):
                if maze[next_y][next_x] != '#' and (next_y, next_x) not in visited:
                    visited.add((next_y, next_x))
                    frontier.append(((next_y, next_x), path + [(next_y, next_x)]))
    return None
# Depth-First Search (DFS) algorithm to find a path in the maze.
def dfs(maze, start, end):
    """
    Depth-First Search algorithm to find a path in the maze.
    """
    stack = [(start, [start])]
    visited = {start}

    while stack:
        current, path = stack.pop()

        if current == end:
            return path

        for y, x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_y, next_x = current[0] + y, current[1] + x

            if 0 <= next_y < len(maze) and 0 <= next_x < len(maze[0]):
                if maze[next_y][next_x] != '#' and (next_y, next_x) not in visited:
                    visited.add((next_y, next_x))
                    stack.append(((next_y, next_x), path + [(next_y, next_x)]))
    return None

#Greedy Best-First Search (GBFS) algorithm to find a path in the maze.
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

        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for y, x in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_y, next_x = current[0] + y, current[1] + x
            next_pos = (next_y, next_x)

            if 0 <= next_y < len(maze) and 0 <= next_x < len(maze[0]):
                if maze[next_y][next_x] != '#' and next_pos not in visited:
                    visited.add(next_pos)
                    priority = heuristic(end, next_pos)
                    frontier.put((priority, next_pos))
                    came_from[next_pos] = current
    return None

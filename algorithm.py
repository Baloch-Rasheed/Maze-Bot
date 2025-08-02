from collections import deque

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

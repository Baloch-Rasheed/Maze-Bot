
# Load the maze from a text file and find the start and end positions.
def load_maze(file_path):
    with open(file_path, 'r') as file:
        maze = [line.strip() for line in file.readlines()]
    start = None
    end = None
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if start is None or end is None:
                if maze[y][x] == 'A':
                    start = (y, x)
                elif maze[y][x] == 'B':
                    end = (y, x)
            else:
                return maze, start, end
    raise ValueError("Start or end point not found in the maze.")

# The BFS algorithm will be implemented here later.
def bfs(maze, start, end):
    # Initialize pygame
    import pygame
    pygame.init()
    
    # Colors
    WALL = (40, 40, 40)        # Dark gray walls
    PATH = (255, 255, 255)     # White paths
    START = (50, 200, 50)      # Green start
    END = (200, 50, 50)        # Red end
    CURRENT = (255, 255, 100)  # Yellow current position
    VISITED = (200, 230, 255)  # Light blue visited
    SOLUTION = (100, 100, 255) # Blue solution path
    
    # Calculate cell size based on maze dimensions
    cell_size = min(800 // len(maze[0]), 600 // len(maze))
    screen = pygame.display.set_mode((len(maze[0]) * cell_size, len(maze) * cell_size))
    pygame.display.set_caption("BFS Maze Solver")
    clock = pygame.time.Clock()
    
    # Draw the initial maze state
    def draw_maze():
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                color = PATH
                if maze[y][x] == '#': color = WALL
                elif (y, x) == start: color = START
                elif (y, x) == end: color = END
                pygame.draw.rect(screen, color, (x*cell_size, y*cell_size, cell_size, cell_size))
        pygame.display.flip()
    
    draw_maze()
    
    # BFS implementation with visualization
    frontier = [(start, [start])]
    visited = set()
    visited.add(start)
    
    running = True
    while running and frontier:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        current, path = frontier.pop(0)
        y, x = current
        
        # Highlight current cell being processed
        if (y, x) not in (start, end):
            pygame.draw.rect(screen, CURRENT, (x*cell_size, y*cell_size, cell_size, cell_size))
            pygame.display.update((x*cell_size, y*cell_size, cell_size, cell_size))
            pygame.time.delay(50)
        
        if current == end:
            # Draw the solution path
            for (py, px) in path:
                if (py, px) not in (start, end):
                    pygame.draw.rect(screen, SOLUTION, (px*cell_size, py*cell_size, cell_size, cell_size))
            pygame.display.flip()
            pygame.time.delay(2000)  # Show solution for 2 seconds
            running = False
            continue
        
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_y, next_x = y + dy, x + dx
            if (0 <= next_y < len(maze)) and 0 <= next_x < len(maze[next_y]) and \
               maze[next_y][next_x] != '#' and (next_y, next_x) not in visited:
                
                visited.add((next_y, next_x))
                frontier.append(((next_y, next_x), path + [(next_y, next_x)]))
                
                # Visualize visited cells
                if (next_y, next_x) not in (start, end):
                    pygame.draw.rect(screen, VISITED, (next_x*cell_size, next_y*cell_size, cell_size, cell_size))
                    pygame.display.update((next_x*cell_size, next_y*cell_size, cell_size, cell_size))
                    pygame.time.delay(20)
        
        clock.tick(30)  # Limit to 30 FPS
    
    pygame.quit()
    return path if current == end else None
                
# 
                

def main():
    print("Loading maze...")
    maze, start, end = load_maze('maze-1.txt')
    print("Maze loaded successfully.")
    bfs_path = bfs(maze, start, end)
    
if __name__ == "__main__":
    main()
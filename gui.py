import pygame

class MazeGUI:
    """
    A class to handle the graphical user interface for the maze solver.
    """
    # Define colors for different elements of the maze
    WALL = (40, 40, 40)
    PATH = (255, 255, 255)
    START = (50, 200, 50)
    END = (200, 50, 50)
    SOLUTION = (100, 100, 255)

    def __init__(self, maze, start, end):
        """
        Initializes the MazeGUI.

        Args:
            maze (list of str): The maze layout.
            start (tuple): The starting coordinates (row, col).
            end (tuple): The ending coordinates (row, col).
        """
        self.maze = maze
        self.start = start
        self.end = end
        
        # Determine the size of each cell based on the maze dimensions
        self.cell_size = min(800 // len(maze[0]), 600 // len(maze))
        
        # Calculate the screen dimensions
        self.screen_width = len(maze[0]) * self.cell_size
        self.screen_height = len(maze) * self.cell_size
        
        # Initialize Pygame and set up the display
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("BFS Maze Solver")

    def draw_maze(self):
        """
        Draws the initial state of the maze.
        """
        # Iterate over each cell in the maze
        for r, row in enumerate(self.maze):
            for c, cell in enumerate(row):
                # Determine the color of the cell based on its type
                color = self.PATH
                if cell == '#':
                    color = self.WALL
                elif (r, c) == self.start:
                    color = self.START
                elif (r, c) == self.end:
                    color = self.END
                
                # Draw the rectangle for the cell
                pygame.draw.rect(self.screen, color, (c * self.cell_size, r * self.cell_size, self.cell_size, self.cell_size))

    def draw_solution(self, path):
        """
        Draws the solution path on the maze.

        Args:
            path (list of tuples): The path from start to end.
        """
        # If a path is found, draw it on the screen
        if path:
            for r, c in path:
                # Skip drawing over the start and end points
                if (r, c) != self.start and (r, c) != self.end:
                    # Draw a rectangle for each cell in the solution path
                    pygame.draw.rect(self.screen, self.SOLUTION, (c * self.cell_size, r * self.cell_size, self.cell_size, self.cell_size))
                    pygame.display.flip()
                    pygame.time.delay(50)  # Add a small delay for visualization

    def run(self, path):
        """
        Runs the main event loop for the GUI.

        Args:
            path (list of tuples): The path to be displayed.
        """
        running = True
        self.draw_maze()
        self.draw_solution(path)

        # Keep the window open until the user closes it
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            pygame.display.flip()

        # Quit Pygame when the loop ends
        pygame.quit()

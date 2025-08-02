import pygame
from maze_loader import load_maze
from algorithm import bfs, dfs
from gui import MazeGUI

def main():
    try:
        # Load the maze from the specified file
        maze, start, end = load_maze('maze-2.txt')
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")
        return

    # Initialize the MazeGUI
    gui = MazeGUI(maze, start, end)

    # Run the BFS algorithm to find the path
    # path = bfs(maze, start, end)
    path = dfs(maze, start, end)

    # Run the main event loop to display the maze and the solution
    gui.run(path)

if __name__ == "__main__":
    main()

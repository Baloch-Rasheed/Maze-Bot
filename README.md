# Maze Bot | Maze Solver

This project is a Python application for visualizing and solving mazes using three different search algorithms: **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **Greedy Best-First Search (GBFS)**. The maze is loaded from a text file and displayed using a graphical interface built with Pygame.

## Features

- **Maze Loading:** Load mazes from text files using `#` for walls, spaces for paths, `A` for the start point, and `B` for the end point.
- **Multiple Algorithms:** Solve the maze using BFS, DFS, or GBFS.
- **Visualization:** See the maze and the solution path animated in a Pygame window.
- **Error Handling:** Handles missing files and invalid maze formats gracefully.

## Maze Format

A maze should be a plain text file, for example:

```
##########
#A   #   #
# ## # # #
# #### #B#
#      # #
# #####  #
#       ##
```

- `#` = Wall
- Space = Path
- `A` = Start point
- `B` = End point

## How It Works

1. **Load Maze:** The maze is loaded from a file using `maze_loader.py`.
2. **Choose Algorithm:** In `main.py`, select which algorithm to use by uncommenting the desired line:
    - `path = bfs(maze, start, end)`
    - `path = dfs(maze, start, end)`
    - `path = gbfs(maze, start, end)`
3. **Visualize Solution:** The solution path is displayed step-by-step in the GUI.

## Files

- `main.py` — Entry point; loads the maze, runs the algorithm, and starts the GUI.
- `maze_loader.py` — Loads the maze from a text file and finds the start/end points.
- `algorithm.py` — Contains BFS, DFS, and GBFS implementations.
- `gui.py` — Handles maze visualization and solution animation using Pygame.

## Requirements

- Python 3.x
- Pygame (`pip install pygame`)

## Usage

1. Place your maze text file in the project directory (e.g., `maze-3.txt`).
2. Edit `main.py` to specify the maze file and desired algorithm.
3. Run the project:

   ```
   python main.py
   ```

4. The GUI window will open, showing the maze and the solution path.

## Custom Mazes

Create your own maze files using the format described above. Make sure there is one `A` and one `B` in the maze.

## License

This project is for educational

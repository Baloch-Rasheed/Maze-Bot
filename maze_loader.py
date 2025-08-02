def load_maze(file_path):

    try:
        # Open and read the maze file
        with open(file_path, 'r') as file:
            maze = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # Raise an error if the file does not exist
        raise FileNotFoundError(f"The maze file was not found at: {file_path}")

    start, end = None, None
    # Iterate through the maze to find the start ('A') and end ('B') points
    for x, row in enumerate(maze):
        for y, col in enumerate(row):
            if col == 'A':
                start = (x, y)
            elif col == 'B':
                end = (x, y)

    # If both start and end points are found, return the maze data
    if start and end:
        return maze, start, end
    else:
        # Raise an error if the start or end point is missing
        raise ValueError("there is an error of finding any start or end point.")

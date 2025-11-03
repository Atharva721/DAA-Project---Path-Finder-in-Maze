from maze_design import generate_maze
from path_finder import solve_maze
from maze_ui import show_maze

if __name__ == "__main__":
    maze = generate_maze(10)
    path = []
    temp_maze = [row[:] for row in maze]  # Copy for solving
    solved = solve_maze(temp_maze, 0, 0, path)

    if solved:
        print("✅ Path Found!")
    else:
        print("❌ No Path Found")

    show_maze(maze, path)

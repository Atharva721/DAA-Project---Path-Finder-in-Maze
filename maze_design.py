# Task 1: Maze Design
import random

def generate_maze(size=10):
    maze = [[1 if random.random() > 0.3 else 0 for _ in range(size)] for _ in range(size)]
    maze[0][0] = 1
    maze[size-1][size-1] = 1
    return maze

if __name__ == "__main__":
    for row in generate_maze():
        print(row)

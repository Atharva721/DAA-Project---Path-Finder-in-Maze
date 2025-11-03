# Task 2: Backtracking Path Finder
def solve_maze(maze, x=0, y=0, path=[]):
    n = len(maze)
    if x == n-1 and y == n-1:
        path.append((x, y))
        return True
    
    if x < 0 or y < 0 or x >= n or y >= n or maze[x][y] == 0:
        return False
    
    maze[x][y] = 0
    path.append((x, y))

    if (solve_maze(maze, x+1, y, path) or
        solve_maze(maze, x, y+1, path) or
        solve_maze(maze, x-1, y, path) or
        solve_maze(maze, x, y-1, path)):
        return True

    path.pop()
    return False

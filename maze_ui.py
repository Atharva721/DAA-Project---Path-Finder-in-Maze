# Task 3: UI & Animation (Tkinter)
import tkinter as tk
import time

def show_maze(maze, path=[]):
    size = len(maze)
    cell = 30

    win = tk.Tk()
    win.title("Path Finder in Maze")

    canvas = tk.Canvas(win, width=size*cell, height=size*cell)
    canvas.pack()

    for i in range(size):
        for j in range(size):
            color = "white" if maze[i][j] == 1 else "black"
            canvas.create_rectangle(j*cell, i*cell, (j+1)*cell, (i+1)*cell, fill=color, outline="gray")

    for (x, y) in path:
        canvas.create_rectangle(y*cell, x*cell, (y+1)*cell, (x+1)*cell, fill="green")
        win.update()
        time.sleep(0.1)

    win.mainloop()

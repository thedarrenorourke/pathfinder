import curses
from curses import wrapper
import time
import queue

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    blue = curses.color_pair(1)
    red = curses.color_pair(2)
    for idx, row in enumerate(maze):
        for jdx, value in enumerate(row):
            # Multiply by 2 for spacing
            if (idx, jdx) in path:
                stdscr.addstr(idx, jdx*2, "X", red)
            else:
                stdscr.addstr(idx, jdx*2, value, blue)

def find_start(maze, start_symbol):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start_symbol:
                return i, j
    return None



def find_path(maze, stdscr):
    start_symbol = 'O'
    end_symbol = 'X'
    start_position = find_start(maze=maze, start_symbol=start_symbol)
    q = queue.Queue()
    # Store the position + the path used to get there
    q.put((start_position, [start_position]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.5)
        stdscr.refresh()

        if maze[row][col] == end_symbol:
            return path

        neighbours = find_neighbours(maze, row, col)
        for neighbour in neighbours:
            if neighbour in visited:
                # Have already checked
                continue
            r, c = neighbour
            if maze[r][c] == '#':
                # This is a blocked node
                continue

            new_path = path + [neighbour]
            q.put((neighbour, new_path))
            visited.add(neighbour)

def find_neighbours(maze, row, col):
    neighbours = []

    if row > 0: #Above
        neighbours.append((row - 1, col))
    if row + 1 < len(maze): #Below
        neighbours.append((row + 1, col))
    if col > 0: #Left
        neighbours.append((row, col - 1))
    if col + 1 < len(maze[0]): #Right
        neighbours.append((row, col + 1))

    return neighbours

def main(stdscr):
    # Id of 1, foreground color, background colour
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)
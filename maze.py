import random

# Constants
WALL = '#'
PATH = ' '
VISITED = '.'
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

def generate_maze(width=20, height=20):
    maze = [[WALL for _ in range(width)] for _ in range(height)]

    def carve_passages(x, y):
        dirs = DIRS[:]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx * 2, y + dy * 2
            if 1 <= nx < width - 1 and 1 <= ny < height - 1:
                if maze[ny][nx] == WALL:
                    maze[y + dy][x + dx] = PATH
                    maze[ny][nx] = PATH
                    carve_passages(nx, ny)

    maze[1][1] = PATH
    carve_passages(1, 1)
    maze[0][1] = PATH  # Entry
    maze[height - 1][width - 2] = PATH  # Exit
    return maze

def find_path(maze, x, y, end_x, end_y, path):
    if (x, y) == (end_x, end_y):
        path.append((x, y))
        return True
    if maze[y][x] != PATH:
        return False

    maze[y][x] = VISITED
    path.append((x, y))

    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
            if find_path(maze, nx, ny, end_x, end_y, path):
                return True

    path.pop()
    return False

def display_maze(maze):
    for row in maze:
        print(''.join(row))

if __name__ == '__main__':
    width, height = 20, 20
    maze = generate_maze(width, height)
    path = []
    start_x, start_y = 1, 0
    end_x, end_y = width - 2, height - 1

    find_path(maze, start_x, start_y, end_x, end_y, path)

    for x, y in path:
        maze[y][x] = '.'

    maze[start_y][start_x] = 'S'  # Mark Start
    maze[end_y][end_x] = 'E'      # Mark End

    display_maze(maze)

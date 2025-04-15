import random

WALL = '#'
PATH = ' '
VISITED = '.'
START = 'S'
END = 'E'

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def generate_maze(width=20, height=20):
    maze = [[WALL for _ in range(width)] for _ in range(height)]

    def carve(x, y):
        dirs = DIRS[:]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx*2, y + dy*2
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny][nx] == WALL:
                maze[ny][nx] = PATH
                maze[y + dy][x + dx] = PATH
                carve(nx, ny)

    # стартовая точка и генерация
    maze[1][1] = PATH
    carve(1, 1)
    maze[1][1] = START
    maze[height - 2][width - 2] = END
    return maze

def find_path(maze, x, y, end_x, end_y, path):
    if (x, y) == (end_x, end_y):
        path.append((x, y))
        return True
    if maze[y][x] not in (PATH, END):
        return False

    maze[y][x] = VISITED
    path.append((x, y))

    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if find_path(maze, nx, ny, end_x, end_y, path):
            return True

    path.pop()
    return False

def display_maze(maze):
    for row in maze:
        print(''.join(row))

if __name__ == '__main__':
    width, height = 21, 21  # обязательно нечётные размеры
    maze = generate_maze(width, height)
    path = []
    find_path(maze, 1, 1, width - 2, height - 2, path)

    # Отметим путь точками, кроме S и E
    for x, y in path:
        if maze[y][x] == PATH:
            maze[y][x] = '.'

    display_maze(maze)
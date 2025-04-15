
WALL = '#'
PATH = ' '
VISITED = '.'
START = 'S'
END = 'E'


DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def generate_maze(width=20, height=20):
    maze = [[WALL for _ in range(width)] for _ in range(height)]
    return maze

def display_maze(maze):
    for row in maze:
        print(''.join(row))

def find_path(maze, x, y, end_x, end_y, path):
    return False

if __name__ == '__main__':
    maze = generate_maze()
    display_maze(maze)
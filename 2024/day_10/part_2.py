
DIRECTIONS = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0),
}

def find_paths(t_map, cell, x, y, rows, cols):
    valid_path = 0

    if t_map[y][x] == '9':
        return 1

    for direction in DIRECTIONS:
        new_x = x + DIRECTIONS[direction][0]
        new_y = y + DIRECTIONS[direction][1]

        if new_x < 0 or new_x >= cols or new_y < 0 or new_y >= rows:
            continue

        if t_map[new_y][new_x] == '.' or t_map[y][x] == '.':
            continue

        if int(t_map[new_y][new_x]) == int(t_map[y][x]) + 1:
            valid_path += find_paths(t_map, t_map[new_y][new_x], new_x, new_y, rows, cols)

    return valid_path

def main():
    file = open('input_test.txt')

    t_map = [list(line.strip()) for line in file]
    rows, cols = len(t_map), len(t_map[0])
    sum = 0

    for y, row in enumerate(t_map):
        for x, cell in enumerate(row):
            if cell == '.':
                continue
            if cell == '0':
                paths = find_paths(t_map, cell, x, y, rows, cols)
                sum += paths

    print(sum)

if __name__ == '__main__':
    main()


# Solution: 1655

STEP_DIRECTIONS = [
    (0, -1), # up
    (1, 0), # right
    (0, 1), # down
    (-1, 0), # left
]

def get_starting_position(array):
    for j in range(len(array)):
        for i in range(len(array[j])):
            if array[j][i] == "^":
                return (i, j)
    return None

def is_path_infinite(start_pos, new_obstruction_pos, array):
    rows, columns = len(array), len(array[0])
    current_pos = start_pos
    direction_idx = 0
    visited_positions = set()

    while True:
        next_pos_x = current_pos[0] + STEP_DIRECTIONS[direction_idx][0]
        next_pos_y = current_pos[1] + STEP_DIRECTIONS[direction_idx][1]

        if not (0 <= next_pos_x < rows and 0 <= next_pos_y < columns):
            return False

        char = array[next_pos_y][next_pos_x]

        if char == "#" or new_obstruction_pos == (next_pos_x, next_pos_y):
            direction_idx = (direction_idx + 1) % 4

        elif char == "." or char == "^":
            current_pos = (next_pos_x, next_pos_y)

            state = (current_pos, direction_idx)
            if state in visited_positions:
                return True

            visited_positions.add(state)

def get_distinct_positions_set(array):
    rows, columns = len(array), len(array[0])

    distinct_positions_set = set()
    start_pos = get_starting_position(array)

    current_pos = start_pos
    direction_idx = 0

    while True:
        next_pos_x = current_pos[0] + STEP_DIRECTIONS[direction_idx][0]
        next_pos_y = current_pos[1] + STEP_DIRECTIONS[direction_idx][1]

        if not (0 <= next_pos_x < rows and 0 <= next_pos_y < columns):
            break

        char = array[next_pos_y][next_pos_x]

        if char == "." or char == "^":
            current_pos = (next_pos_x, next_pos_y)
            distinct_positions_set.add(current_pos)
        elif char == "#":
            direction_idx = (direction_idx + 1) % 4

    return distinct_positions_set

def get_distinct_obstruction_positions(distinct_positions, array):
    start_pos = get_starting_position(array)

    if start_pos in distinct_positions:
        distinct_positions.remove(start_pos)

    infinite_paths = 0

    for distinct_position in distinct_positions:
        new_obstruction_pos = distinct_position
        if is_path_infinite(start_pos, new_obstruction_pos, array):
            infinite_paths += 1

    return infinite_paths

def main():
    file = open("./input.txt")

    array = [list(line.strip()) for line in file]

    distinct_positions = get_distinct_positions_set(array)

    distinct_obstruction_positions = get_distinct_obstruction_positions(distinct_positions, array)
    print(distinct_obstruction_positions)

if __name__ == "__main__":
    main()

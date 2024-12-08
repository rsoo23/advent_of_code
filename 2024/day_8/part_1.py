
# Solution: 426

def get_antenna_pos_map(arr):
    map = {}
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '.':
                continue
            if arr[i][j] not in map:
                map[arr[i][j]] = []
            map[arr[i][j]].append((i, j))

    return map

def get_antinode_locations_num(arr, antenna_pos_map):
    rows, columns = len(arr), len(arr[0])
    antinode_set = set()

    for key in antenna_pos_map:
        for pos1 in antenna_pos_map[key]:
            for pos2 in antenna_pos_map[key]:
                if pos1 == pos2:
                    continue
                antinode_pos = (2 * pos2[0] - pos1[0], 2 * pos2[1] - pos1[1])
                if (0 <= antinode_pos[0] < rows) and \
                   (0 <= antinode_pos[1] < columns) and \
                   antinode_pos not in antinode_set:
                    antinode_set.add(antinode_pos)

    return len(antinode_set)

def main():
    file = open('./input.txt')

    arr = [list(line.strip()) for line in file]

    antenna_pos_map = get_antenna_pos_map(arr)

    antinode_locations_num = get_antinode_locations_num(arr, antenna_pos_map)
    print(antinode_locations_num)

if __name__ == '__main__':
    main()

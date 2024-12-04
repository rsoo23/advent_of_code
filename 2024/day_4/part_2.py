
# 1. load the input file into a 2D array
# 2. find As in the array
# 3. check all diagonals for the MAS pattern
# 4. sum the number valid patterns found

# Solution: 1921

DIRECTIONS = {
    'UL': (-1, -1),
    'UR': (1, -1),
    'DL': (-1, 1),
    'DR': (1, 1),
}

def check_xmas(direction, letter, arr, i, j):
    dx, dy = DIRECTIONS[direction]

    j += dx
    i += dy
    if not (0 <= i < len(arr) and 0 <= j < len(arr[0])):
        return False
    if arr[i][j] != letter:
        return False
    return True

def find_xmas(arr, i, j):
    xmas_num = 0

    if (((check_xmas('UL', 'M', arr, i, j) and check_xmas('DR', 'S', arr, i, j)) or
       (check_xmas('UL', 'S', arr, i, j) and check_xmas('DR', 'M', arr, i, j))) and \
       ((check_xmas('UR', 'M', arr, i, j) and check_xmas('DL', 'S', arr, i, j)) or
       (check_xmas('UR', 'S', arr, i, j) and check_xmas('DL', 'M', arr, i, j)))):
        xmas_num += 1

    return xmas_num

def get_xmas_num(array):
    xmas_num = 0

    for i, row in enumerate(array):
        for j, cell in enumerate(row):
            if cell == "A":
                xmas_num += find_xmas(array, i, j)

    return xmas_num

def main():
    file = open("./input.txt")

    array = [list(line.strip()) for line in file]

    xmas_num = get_xmas_num(array)
    print('xmas_num:', xmas_num)

if __name__ == "__main__":
    main()

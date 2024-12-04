
# 1. load the input file into a 2D array
# 2. find Xs in the array
# 3. check all directions for the MAS pattern
# 4. sum the number valid patterns found

# Solution: 2530

DIRECTIONS = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, -1),
    'D': (0, 1),
    'UL': (-1, -1),
    'UR': (1, -1),
    'DL': (-1, 1),
    'DR': (1, 1),
}

def check_xmas(direction, arr, i, j):
    dx, dy = DIRECTIONS[direction]
    pattern = "MAS"

    for idx, letter in enumerate(pattern):
        j += dx
        i += dy

        if not (0 <= i < len(arr) and 0 <= j < len(arr[0])):
            return False
        if arr[i][j] != letter:
            return False

    return True

def find_xmas(arr, i, j):
    xmas_num = 0

    for direction in DIRECTIONS.keys():
        if check_xmas(direction, arr, i, j):
            xmas_num += 1

    return xmas_num

def get_xmas_num(array):
    xmas_num = 0

    for i, row in enumerate(array):
        for j, cell in enumerate(row):
            if cell == "X":
                xmas_num += find_xmas(array, i, j)

    return xmas_num

def main():
    file = open("./input.txt")

    array = [list(line.strip()) for line in file]

    xmas_num = get_xmas_num(array)
    print('xmas_num:', xmas_num)

if __name__ == "__main__":
    main()

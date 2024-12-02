
# 1. reads the input file and places the first number and second number in the first_numbers array and second_numbers array respectively
# 2. iterates through second_numbers array to find the frequency of each number
# 3. iterates through first_numbers array to calculate the product, adding it to the variable similiarity_score cumulatively

# Solution: 25574739

first_numbers = []
second_numbers = []

with open("./input.txt") as file:
    lines = file.readlines()

    for line in lines:
        numbers = line.split()
        first_numbers.append(int(numbers[0]))
        second_numbers.append(int(numbers[1]))

def main():
    map = dict()
    similiarity_score = 0

    for second_num in second_numbers:
        if second_num in map:
            map[second_num] += 1
        else:
            map[second_num] = 1

    for first_num in first_numbers:
        if first_num in map:
            product = first_num * map[first_num]
        else:
            product = 0
        similiarity_score += product

    print(similiarity_score)

if __name__ == "__main__":
    main()

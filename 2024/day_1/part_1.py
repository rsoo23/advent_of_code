
# 1. reads the input file and places the first number and second number in the first_numbers array and second_numbers array respectively
# 2. iterates through both of the arrays to find the absolute difference
# 3. adds it to the variable sum

# Solution: 1603498

first_numbers = []
second_numbers = []

with open("./input.txt") as file:
    lines = file.readlines()

    for line in lines:
        numbers = line.split()
        first_numbers.append(int(numbers[0]))
        second_numbers.append(int(numbers[1]))

def main():
    first_numbers.sort()
    second_numbers.sort()
    sum = 0

    for first_num, second_num in zip(first_numbers, second_numbers):
        difference = abs(first_num - second_num)
        sum += difference

    print(sum)

if __name__ == "__main__":
    main()

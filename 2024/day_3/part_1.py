
# 1. extract all patterns that have mul(\d, \d)
# 2. extract both numbers and multiply
# 3. sum product

import re

def main():
    file = open("./input.txt")
    lines = file.readlines()
    sum = 0

    for line in lines:
        mul_expressions = re.findall(r"mul\(\d+,\d+\)", line)

        for expression in mul_expressions:
            nums = re.findall(r"\d+", expression)
            product = int(nums[0]) * int(nums[1])
            sum += product

    print(sum)

if __name__ == "__main__":
    main()

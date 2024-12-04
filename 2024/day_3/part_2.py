
# 1. extract all patterns that have mul(\d,\d), don't() or do()
# 2. if don't() is found, set multiply_enabled to False
# 3. then skip through the next mul expressions until do() is found
# 4. process the mul expresssions until don't() is found
# 5. repeats the process until the end of the line

# solution: 95411583

import re

def main():
    file = open("./input.txt")
    lines = file.readlines()
    sum = 0
    multiply_enabled = True

    for line in lines:
        expressions = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", line)

        for expression in expressions:
            if expression == "don't()":
                multiply_enabled = False
                continue
            elif expression == "do()":
                multiply_enabled = True
                continue

            if multiply_enabled:
                nums = re.findall(r"\d+", expression)
                product = int(nums[0]) * int(nums[1])

                sum += product

    print(sum)

if __name__ == "__main__":
    main()

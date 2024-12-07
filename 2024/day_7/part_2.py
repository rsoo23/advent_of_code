
# Solution: 105449593161984

import re
from itertools import product

operations = ['+', '*', '||']

def get_result(numbers, result):
    operation_permutations = list(product(operations, repeat=len(numbers) - 1))

    for permutation in operation_permutations:
        equation = []
        temp_numbers = numbers.copy()
        perm_list = list(permutation)

        while len(temp_numbers) > 1:
            equation.append(temp_numbers.pop(0))
            equation.append(perm_list.pop(0))
        equation.append(temp_numbers.pop(0))

        total_result = int(equation.pop(0))

        while len(equation) > 0:
            char = equation.pop(0)
            num = int(equation.pop(0))
            if char == '+':
                total_result += num
            elif char == '*':
                total_result *= num
            elif char == '||':
                total_result = int(str(total_result) + str(num))

        if total_result == int(result):
            return total_result
    return 0

def main():
    file = open('input.txt')
    total_calibration_result = 0

    for line in file:
        numbers = re.findall(r'\d+', line)
        result = numbers.pop(0)
        total_calibration_result += get_result(numbers, result)

    print(total_calibration_result)

if __name__ == '__main__':
    main()

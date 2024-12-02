
# 1. reads the input file and places levels into the report_levels list
# 2. iterates through the report_levels list and checks if the report is safe and within the constraints
# 3. add the total number of safe reports

# Solution: 282

def is_report_safe(levels):
    is_decreasing = False
    is_increasing = False
    max_index = len(levels) - 1

    for i in range(max_index):
        diff = int(levels[i + 1]) - int(levels[i])

        if diff > 0:
            is_increasing = True
        else:
            is_decreasing = True

        if is_decreasing and is_increasing:
            return False

        abs_diff = abs(diff)

        if abs_diff < 1 or abs_diff > 3:
            return False
    return True

def main():
    file = open("./input.txt")
    lines = file.readlines()
    safe_reports = 0

    for line in lines:
        report_levels = line.split()
        result = is_report_safe(report_levels)

        if result == True:
            safe_reports += 1

    print(safe_reports)

if __name__ == "__main__":
    main()

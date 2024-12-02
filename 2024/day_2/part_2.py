
from part_1 import is_report_safe

# Problem Dampener:
# If a report is not safe, remove one of the levels and check if the report is safe
# Try removing one level until the report is safe or all elements have been removed

# Solution: 349

def main():
    file = open("./input.txt")
    lines = file.readlines()
    safe_reports = 0

    for line in lines:
        report_levels = line.split()
        result = is_report_safe(report_levels)

        if result == True:
            safe_reports += 1
        else:
            # Problem Dampener
            for i in range(len(report_levels)):
                copy_report_levels = report_levels.copy()
                copy_report_levels.pop(i)
                result = is_report_safe(copy_report_levels)

                if result == True:
                    safe_reports += 1
                    break

    print(safe_reports)

if __name__ == "__main__":
    main()

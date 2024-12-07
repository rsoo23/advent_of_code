
# Solution: 5108

import re

def get_middle_value(index_map):
    middle_index = len(index_map) // 2

    for key, index in index_map.items():
        if index == middle_index:
            return int(key)

def is_rule_valid(update_value, rule_values, map):
    for rule_value in rule_values:
        if rule_value not in map:
            continue
        if map[rule_value] < map[update_value]:
            return False
    return True

def check_rules(rule_graph, update_index_map_arr):
    total_middle_values = 0

    for index_map in update_index_map_arr:
        incorrect_rule = False

        for update_value in index_map.keys():

            if update_value in rule_graph:
                rule_values = rule_graph[update_value]

                if not is_rule_valid(update_value, rule_values, index_map):
                    incorrect_rule = True

        if not incorrect_rule:
            total_middle_values += get_middle_value(index_map)

    return total_middle_values

def main():
    file = open("./input.txt")
    rule_graph = {}
    update_index_map_arr = []

    # parsing the rules
    for line in file:
        if line == '\n':
            break
        rule_nums = re.findall(r"\d+|\d+", line)

        if rule_nums[0] not in rule_graph:
            rule_graph.setdefault(rule_nums[0], []).append(rule_nums[1])
        else:
            rule_graph[rule_nums[0]].append(rule_nums[1])

    # parsing the updates
    for line in file:
        update_values = list(line.strip().split(','))
        update_index_map = {value: i for i, value in enumerate(update_values)}
        update_index_map_arr.append(update_index_map)

    total_middle_values = check_rules(rule_graph, update_index_map_arr)

    print(total_middle_values)


if __name__ == "__main__":
    main()

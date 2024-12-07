
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

def get_index_map_key(index_map, index):
    for key, i in index_map.items():
        if i == index:
            return key
    return None

def is_update_value_in_order(val1, val2, rule_graph, index_map):
    if val1 in rule_graph:
        rule_values = rule_graph[val1]

        if val2 in rule_values:
            return True

    if val2 in rule_graph:
        rule_values = rule_graph[val2]

        if val1 in rule_values:
            return False
        return True
    
    return True

def sort_index_map(rule_graph, index_map):
    n = len(index_map)

    for i in range(n - 1):
        min_index = i
        for j in range (i + 1, n):
            val1 = get_index_map_key(index_map, min_index)
            val2 = get_index_map_key(index_map, j)
            if not is_update_value_in_order(val1, val2, rule_graph, index_map):
                min_index = j

        min_val =  get_index_map_key(index_map, min_index)
        val = get_index_map_key(index_map, i)
        index_map[val], index_map[min_val] = index_map[min_val], index_map[val]

    return index_map

def check_rules(rule_graph, update_index_map_arr):
    total_middle_values = 0

    for index_map in update_index_map_arr:
        incorrect_rule = False

        for update_value in index_map.keys():

            if update_value in rule_graph:
                rule_values = rule_graph[update_value]

                if not is_rule_valid(update_value, rule_values, index_map):
                    incorrect_rule = True
                    break

        if incorrect_rule:
            sorted_index_map = sort_index_map(rule_graph, index_map)
            total_middle_values += get_middle_value(sorted_index_map)

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



def convert_to_blocks(digits):
    blocks = []

    for i, digit in enumerate(digits):
        num = int(digit)

        if i == 0:
            while num > 0:
                blocks.append(i)
                num -= 1
        elif i % 2 != 0:
            while num > 0:
                blocks.append('.')
                num -= 1
        else:
            while num > 0:
                blocks.append(int(i / 2))
                num -= 1

    return blocks

def find_empty_space_start_index(blocks, file_block_len, file_block_end_index):
    start_index = 0
    empty_space_len = 0
    empty_space_found = False
    blocks_len = len(blocks)

    for i, block in enumerate(blocks):
        if block == '.':
            if blocks[i - 1] != '.':
                start_index = i
                empty_space_len = 0

            empty_space_len += 1
            continue

        if empty_space_len >= file_block_len and start_index < blocks_len - 1 - file_block_end_index:
            empty_space_found = True
            return start_index, empty_space_found

    return start_index, empty_space_found

def move_file_blocks(blocks):
    blocks_len = len(blocks)
    file_block_end_index = 0
    file_block_len = 0
    reversed_blocks = list(reversed(blocks))

    for i, block in enumerate(reversed_blocks):
        if i == 0 and block != '.':
            prev_block = block
            file_block_len += 1
            continue

        if block == '.':
            continue

        if i > 0 and prev_block == block and block != '.':
            file_block_len += 1
            continue

        # once file block ends, find empty space
        empty_space_start_index, empty_space_found = find_empty_space_start_index(blocks, file_block_len, file_block_end_index)

        if not empty_space_found:
            prev_block = block
            file_block_end_index = i
            file_block_len = 1
            continue

        j = file_block_end_index
        while file_block_len > 0:
            blocks[empty_space_start_index] = prev_block

            blocks[blocks_len - j - 1] = '.'

            file_block_len -= 1
            j += 1
            empty_space_start_index += 1

        prev_block = block
        file_block_end_index = i
        file_block_len = 1

    return blocks

def calc_checksum(blocks):
    checksum = 0
    for i, block in enumerate(blocks):
        if block == '.':
            continue
        checksum += i * int(block)
    return checksum

def get_checksum(digits):
    blocks = convert_to_blocks(digits)
    blocks = move_file_blocks(blocks)
    return calc_checksum(blocks)

def main():
    file = open('input.txt')

    for line in file:
        digits = line.strip()

    checksum = get_checksum(digits)
    print(checksum)

if __name__ == '__main__':
    main()

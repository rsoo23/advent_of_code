
# Solution: 6262891638328

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

def move_blocks(blocks):
    for i, block in enumerate(blocks):
        if block == '.':
            removed_block = blocks.pop()

            while removed_block == '.':
                removed_block = blocks.pop()

            blocks[i] = removed_block
    return blocks

def calc_checksum(blocks):
    checksum = 0
    for i, block in enumerate(blocks):
        checksum += i * int(block)
    return checksum

def get_checksum(digits):
    blocks = convert_to_blocks(digits)
    blocks = move_blocks(blocks)
    return calc_checksum(blocks)

def main():
    file = open('input.txt')

    for line in file:
        digits = line.strip()

    checksum = get_checksum(digits)
    print(checksum)


if __name__ == '__main__':
    main()

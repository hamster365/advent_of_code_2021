from pathlib import Path
import re

if __name__ == '__main__':
    input_puzzle = Path('input_puzzle2.log')
    with open(input_puzzle) as file:
        value = file.read().splitlines()
    forward = 0
    aim = 0
    depth = 0
    reg = re.compile('[0-9]')
    for item in value:
        if 'forward' in item:
            add = reg.findall(item)
            forward = forward + int(add[0])
            depth = depth + (aim * int(add[0]))
            print(aim)
        if 'up' in item:
            add = reg.findall(item)
            aim = aim - int(add[0])
        if 'down' in item:
            add = reg.findall(item)
            aim = aim + int(add[0])
    print(forward * depth)

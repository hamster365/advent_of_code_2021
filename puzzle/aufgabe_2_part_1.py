from pathlib import Path
import re

if __name__ == '__main__':
    input_puzzle = Path('input_puzzle2.log')
    with open(input_puzzle) as file:
        value = file.read().splitlines()
    forward = 0
    up = 0
    down = 0
    reg = re.compile('[0-9]')
    for item in value:
        if 'forward' in item:
            add = reg.findall(item)
            forward = forward + int(add[0])
        if 'up' in item:
            add = reg.findall(item)
            up = up + int(add[0])
        if 'down' in item:
            add = reg.findall(item)
            down = down + int(add[0])

    print(forward*(down - up))

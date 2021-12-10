from pathlib import Path

if __name__ == '__main__':
    count = 0
    number = 0
    input_puzzle = Path('input_puzzle1.log')
    with open(input_puzzle) as file:
        value = file.read().splitlines()

    for item in value:
        if int(item) > number:
            count += 1
        number = int(item)
    print(count - 1)

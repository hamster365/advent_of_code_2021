from pathlib import Path

if __name__ == '__main__':
    input_puzzle = Path('input_puzzle6.log')
    with open(input_puzzle) as file:
        value = file.read().splitlines()
    value_list = [item.split('|', 1)[1] for item in value]
    value_important_list = [item.split(' ') for item in value_list]
    value_important_important_list = []
    for item in value_important_list:
            if item != '':
                value_important_important_list.extend(item)
    value_important_important_important_list = []
    for item in value_important_important_list:
        if item != '':
            value_important_important_important_list.append(item)
    value_important_important_important_important_list = []
    for item in value_important_important_important_list:
        if len(item) != 5 and len(item) != 6:
            value_important_important_important_important_list.append(item)
    print(len(value_important_important_important_important_list))

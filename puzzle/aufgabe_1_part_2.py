from pathlib import Path

if __name__ == '__main__':
    list1 = []
    list2 = []
    list3 = []
    devil_count = 666
    count = 0
    ranger = 0
    input_puzzle = Path('input_puzzle1.log')
    with open(input_puzzle) as file:
        value = file.read().splitlines()

    while count in range(devil_count):
        list1.append(int(value[ranger]) + int(value[ranger + 1]) + int(value[ranger + 2]))
        count += 1
        ranger += 3
    count = 0
    ranger = 0
    while count in range(devil_count):
        list2.append(int(value[ranger + 1]) + int(value[ranger + 2]) + int(value[ranger + 3]))
        count += 1
        ranger += 3
    count = 0
    ranger = 0
    while count in range(devil_count):
        list3.append(int(value[ranger + 2]) + int(value[ranger + 3]) + int(value[ranger + 4]))
        count += 1
        ranger += 3

    count = 0
    compare = 0
    result = 0
    while count in range(devil_count):
        if list1[count] > compare:
            result += 1
        compare = list1[count]
        if list2[count] > compare:
            result += 1
        compare = list2[count]
        if list3[count] > compare:
            result += 1
        compare = list3[count]
        count += 1
    print(result - 1)

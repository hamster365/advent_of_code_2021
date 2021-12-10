from pathlib import Path

if __name__ == '__main__':
    input_puzzle = Path('input_puzzle3.log')
    with open(input_puzzle) as file:
        value = file.read().splitlines()

    value_list_1 = value
    value_list_2 = value
    count = 0
    while count in range(12):
        count_0 = 0
        count_1 = 0
        count_total = 0
        for item in value_list_1:
            if item[count] == '0':
                count_0 += 1
            else:
                count_1 += 1
            count_total = count_0 + count_1
        if count_total > 1 :
            if count_1 >= count_0:
                value_list_1 = [item for item in value_list_1 if int(item[count]) == 1]
            else:
                value_list_1 = [item for item in value_list_1 if int(item[count]) == 0]
        count_0 = 0
        count_1 = 0
        count_total = 0
        for item in value_list_2:
            if item[count] == '0':
                count_0 += 1
            else:
                count_1 += 1
        count_total = count_0 + count_1
        if count_total > 1:
            if count_0 <= count_1:
                value_list_2 = [item for item in value_list_2 if int(item[count]) == 0]
            else:
                value_list_2 = [item for item in value_list_2 if int(item[count]) == 1]
        count += 1

    result = int(value_list_1[0], 2) * int(value_list_2[0], 2)
    print(result)

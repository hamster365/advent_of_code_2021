from pathlib import Path
import re

if __name__ == '__main__':
    input_puzzle = Path('input_puzzle5.log')
    with open(input_puzzle) as file:
        value = file.read().splitlines()
        tupel_list = []
    for item in value:
        number = re.findall('[0-9.]+', item)
        if int(number[0]) != int(number[2]) and int(number[1]) != int(number[3]):
            if int(number[0]) < int(number[2]) and int(number[1]) < int(number[3]):
                count1 = int(number[0])
                count2 = int(number[1])
                temp_list = []
                while count1 <= int(number[2]) and count2 <= int(number[3]):
                    temp_1 = (count1, count2)
                    temp_2 = (number[2], count2)
                    temp_3 = (count1, number[3])
                    if temp_1 not in temp_list:
                        temp_list.append(temp_1)
                    if temp_2 not in temp_list:
                        temp_list.append(temp_2)
                    if temp_3 not in temp_list:
                        temp_list.append(temp_3)
                    if count1 < (int(number[2]) + 1):
                        count1 += 1
                    if count2 > (int(number[3]) + 1):
                        count2 += 1
            elif int(number[0]) < int(number[2]) and int(number[1]) > int(number[3]):
                count1 = int(number[0])
                count2 = int(number[3])
                temp_list = []
                while count1 <= int(number[2]) and count2 <= int(number[1]):
                    temp_1 = (count1, count2)
                    temp_2 = (number[2], count2)
                    temp_3 = (count1, number[1])
                    if temp_1 not in temp_list:
                        temp_list.append(temp_1)
                    if temp_2 not in temp_list:
                        temp_list.append(temp_2)
                    if temp_3 not in temp_list:
                        temp_list.append(temp_3)
                    if count1 < (int(number[2]) + 1):
                        count1 += 1
                    if count2 > (int(number[3]) + 1):
                        count2 += 1
            elif int(number[0]) > int(number[2]) and int(number[1]) < int(number[3]):
                count1 = int(number[2])
                count2 = int(number[1])
                temp_list = []
                while count1 <= int(number[0]) and count2 <= int(number[3]):
                    temp_1 = (count1, count2)
                    temp_2 = (number[0], count2)
                    temp_3 = (count1, number[3])
                    if temp_1 not in temp_list:
                        temp_list.append(temp_1)
                    if temp_2 not in temp_list:
                        temp_list.append(temp_2)
                    if temp_3 not in temp_list:
                        temp_list.append(temp_3)
                    if count1 < (int(number[0]) + 1):
                        count1 += 1
                    if count2 < (int(number[3]) + 1):
                        count2 += 1
            elif int(number[0]) > int(number[2]) and int(number[1]) > int(number[3]):
                count1 = int(number[2])
                count2 = int(number[3])
                temp_list = []
                while count1 <= int(number[0]) and count2 <= int(number[1]):
                    temp_1 = (count1, count2)
                    temp_2 = (number[0], count2)
                    temp_3 = (count1, number[1])
                    if temp_1 not in temp_list:
                        temp_list.append(temp_1)
                    if temp_2 not in temp_list:
                        temp_list.append(temp_2)
                    if temp_3 not in temp_list:
                        temp_list.append(temp_3)
                    if count1 < (int(number[0]) + 1):
                        count1 += 1
                    if count2 < (int(number[1]) + 1):
                        count2 += 1
            tupel_list.append(temp_list)
        else:
            if int(number[0]) > int(number[2]):
                count = int(number[2])
                while count <= int(number[0]):
                    tupel_list.append((count, int(number[3])))
                    count += 1
            elif int(number[0]) < int(number[2]):
                count = int(number[0])
                while count <= int(number[2]):
                    tupel_list.append((count, int(number[1])))
                    count += 1
            if int(number[1]) > int(number[3]):
                count = int(number[3])
                while count <= int(number[1]):
                    tupel_list.append((int(number[2]), count))
                    count += 1
            elif int(number[1]) < int(number[3]):
                count = int(number[1])
                while count <= int(number[3]):
                    tupel_list.append((int(number[0]), count))
                    count += 1
    no_duplicate_list = []
    duplicate_list = []
    duplicate_list_list = []
    print(len(tupel_list))
    print('test')
    for item in tupel_list:
        if item not in no_duplicate_list:
            no_duplicate_list.append(item)
        else:
            duplicate_list.append(item)
    print('test')
    for item in duplicate_list:
        if item not in duplicate_list_list:
            duplicate_list_list.append(item)
    print(duplicate_list_list)
    print(len(duplicate_list_list))
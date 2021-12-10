from pathlib import Path
import re

if __name__ == '__main__':
    input_puzzle = Path('input_puzzle4.log')
    with open(input_puzzle) as file:
        value = file.read().splitlines()
    value_list = [item for item in value if item != '']
    lists = ' '.join(value_list)
    value_list_2 = re.findall('[0-9]+', lists)
    numbers = [46, 79, 77, 45, 57, 34, 44, 13, 32, 88, 86, 82, 91, 97, 89, 1, 48, 31, 18, 10, 55, 74, 24, 11, 80, 78, 28
        , 37, 47, 17, 21, 61, 26, 85, 99, 96, 23, 70, 3, 54, 5, 41, 50, 63, 14, 64, 42, 36, 95, 52, 76, 68, 29, 9, 98
        , 35, 84, 83, 71, 49, 73, 58, 56, 66, 92, 30, 51, 20, 81, 69, 65, 15, 6, 16, 39, 43, 67, 7, 59, 40, 60, 4, 90
        , 72, 22, 0, 93, 94, 38, 53, 87, 27, 12, 2, 25, 19, 8, 62, 33, 75
               ]
    max_count = None
    for count in range(100):
        total_count = 0
        counter = 0
        list1 = [value_list_2[0 + (25 * count)], value_list_2[1 + (25 * count)], value_list_2[2 + (25 * count)],
                 value_list_2[3 + (25 * count)], value_list_2[4 + (25 * count)]]
        list2 = [value_list_2[5 + (25 * count)], value_list_2[5 + (25 * count)], value_list_2[6 + (25 * count)],
                 value_list_2[8 + (25 * count)], value_list_2[9 + (25 * count)]]
        list3 = [value_list_2[10 + (25 * count)], value_list_2[11 + (25 * count)], value_list_2[12 + (25 * count)],
                 value_list_2[13 + (25 * count)], value_list_2[14 + (25 * count)]]
        list4 = [value_list_2[15 + (25 * count)], value_list_2[16 + (25 * count)], value_list_2[17 + (25 * count)],
                 value_list_2[18 + (25 * count)], value_list_2[19 + (25 * count)]]
        list5 = [value_list_2[20 + (25 * count)], value_list_2[21 + (25 * count)], value_list_2[22 + (25 * count)],
                 value_list_2[23 + (25 * count)], value_list_2[24 + (25 * count)]]
        list6 = [value_list_2[0 + (25 * count)], value_list_2[5 + (25 * count)], value_list_2[10 + (25 * count)],
                 value_list_2[14 + (25 * count)], value_list_2[20 + (25 * count)]]
        list7 = [value_list_2[1 + (25 * count)], value_list_2[6 + (25 * count)], value_list_2[11 + (25 * count)],
                 value_list_2[15 + (25 * count)], value_list_2[21 + (25 * count)]]
        list8 = [value_list_2[2 + (25 * count)], value_list_2[7 + (25 * count)], value_list_2[12 + (25 * count)],
                 value_list_2[17 + (25 * count)], value_list_2[22 + (25 * count)]]
        list9 = [value_list_2[3 + (25 * count)], value_list_2[8 + (25 * count)], value_list_2[13 + (25 * count)],
                 value_list_2[18 + (25 * count)], value_list_2[23 + (25 * count)]]
        list10 = [value_list_2[4 + (25 * count)], value_list_2[9 + (25 * count)], value_list_2[14 + (25 * count)],
                  value_list_2[19 + (25 * count)], value_list_2[24 + (25 * count)]]
        list11 = [value_list_2[0 + (25 * count)], value_list_2[6 + (25 * count)], value_list_2[12 + (25 * count)],
                  value_list_2[18 + (25 * count)], value_list_2[24 + (25 * count)]]
        list12 = [value_list_2[4 + (25 * count)], value_list_2[8 + (25 * count)], value_list_2[12 + (25 * count)],
                  value_list_2[16 + (25 * count)], value_list_2[20 + (25 * count)]]
        while list1 and list2 and list3 and list4 and list5 and list6 and list7 and list8 and list9 and list10 and list11 and list12 != []:
            if str(numbers[counter]) in list1:
                list1.remove(str(numbers[counter]))
            if str(numbers[counter]) in list2:
                list2.remove(str(numbers[counter]))
            if str(numbers[counter]) in list3:
                list3.remove(str(numbers[counter]))
            if str(numbers[counter]) in list4:
                list4.remove(str(numbers[counter]))
            if str(numbers[counter]) in list5:
                list5.remove(str(numbers[counter]))
            if str(numbers[counter]) in list6:
                list6.remove(str(numbers[counter]))
            if str(numbers[counter]) in list7:
                list7.remove(str(numbers[counter]))
            if str(numbers[counter]) in list8:
                list8.remove(str(numbers[counter]))
            if str(numbers[counter]) in list9:
                list9.remove(str(numbers[counter]))
            if str(numbers[counter]) in list10:
                list10.remove(str(numbers[counter]))
            if str(numbers[counter]) in list11:
                list11.remove(str(numbers[counter]))
            if str(numbers[counter]) in list12:
                list12.remove(str(numbers[counter]))
            counter += 1
            total_count += 1
        if max_count is not None:
            if total_count <= max_count:
                max_count = total_count
                final_list = list1 + list(set(list2) - set(list1))
                final_list = final_list + list(set(list3) - set(final_list))
                final_list = final_list + list(set(list4) - set(final_list))
                final_list = final_list + list(set(list5) - set(final_list))
                final_list = final_list + list(set(list6) - set(final_list))
                final_list = final_list + list(set(list7) - set(final_list))
                final_list = final_list + list(set(list8) - set(final_list))
                final_list = final_list + list(set(list9) - set(final_list))
                final_list = final_list + list(set(list10) - set(final_list))
                final_list = final_list + list(set(list11) - set(final_list))
                final_list = final_list + list(set(list12) - set(final_list))
                score = 0
                for item in final_list:
                    score = score + int(item)
                score = score * numbers[total_count - 1]
                print(score)
        else:
            max_count = counter
        count += 1

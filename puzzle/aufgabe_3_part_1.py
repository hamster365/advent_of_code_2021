from pathlib import Path

if __name__ == '__main__':
    input_puzzle = Path('input_puzzle3.log')
    with open(input_puzzle) as file:
        value = file.read().splitlines()
    list0 = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    list11 = []
    result_list_1 = []
    result_list_2 = []
    for item in value:
        list0.append(item[0])
        list1.append(item[1])
        list2.append(item[2])
        list3.append(item[3])
        list4.append(item[4])
        list5.append(item[5])
        list6.append(item[6])
        list7.append(item[7])
        list8.append(item[8])
        list9.append(item[9])
        list10.append(item[10])
        list11.append(item[11])

    result_list_1.append(max(list0, key=list0.count) + max(list1, key=list1.count) + max(list2, key=list2.count) + max(list3, key=list3.count) + max(list4, key=list4.count) + max(list5, key=list5.count) + max(list6, key=list6.count) + max(list7, key=list7.count) + max(list8, key=list8.count) + max(list9, key=list9.count) + max(list10, key=list10.count) + max(list11, key=list11.count))
    result_list_2.append(min(list0, key=list0.count) + min(list1, key=list1.count) + min(list2, key=list2.count) + min(list3, key=list3.count) + min(list4, key=list4.count) + min(list5, key=list5.count) + min(list6, key=list6.count) + min(list7, key=list7.count) + min(list8, key=list8.count) + min(list9, key=list9.count) + min(list10, key = list10.count) + min(list11, key=list11.count))
    result = int(result_list_1[0], 2) * int(result_list_2[0], 2)
    print(result)

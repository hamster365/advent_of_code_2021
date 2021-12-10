from pathlib import Path

if __name__ == '__main__':
    input_puzzle = Path('input_puzzle8.log')
    with open(input_puzzle) as file:
        value = file.read().splitlines()

    f_1 = '()'
    f_2 = '{}'
    f_3 = '[]'
    f_4 = '<>'
    f_5 = '(}'
    f_6 = '(]'
    f_7 = '(>'
    f_8 = '{)'
    f_9 = '{]'
    f_10 = '{>'
    f_11 = '[)'
    f_12 = '[}'
    f_13 = '[>'
    f_14 = '<)'
    f_15 = '<}'
    f_16 = '<]'
    char_list = []
    total_count = 0
    for item in value:
        count = 0
        in_list = True
        total_count += 1
        count_max = len(item)
        temp_item = list(item)
        while count < count_max:
            temp_str = temp_item[count]
            if count + 1 < len(temp_item):
                temp_str = temp_str + temp_item[count + 1]
            else:
                temp_str = temp_str
            if f_1 in temp_str or f_2 in temp_str or f_3 in temp_str or f_4 in temp_str:
                del temp_item[count]
                if count <= count_max:
                    del temp_item[count]
                count -= 1
                count_max -= 2
            elif f_8 in temp_str or f_11 in temp_str or f_14 in temp_str:
                in_list = False
                break
            elif f_6 in temp_str or f_9 in temp_str or f_16 in temp_str:
                in_list = False
                break
            elif f_5 in temp_str or f_12 in temp_str or f_15 in temp_str:
                in_list = False
                break
            elif f_7 in temp_str or f_10 in temp_str or f_13 in temp_str:
                in_list = False
                break
            else:
                count += 1
        if in_list:
            char_list.append(temp_item)
    result_list = []
    for item in char_list:
        temp_result = 0
        while 0 < len(item):
            temp_item = item.pop()
            if '(' in temp_item:
                temp_result = temp_result * 5
                temp_result += 1
            if '[' in temp_item:
                temp_result = temp_result * 5
                temp_result += 2
            if '{' in temp_item:
                temp_result = temp_result * 5
                temp_result += 3
            if '<' in temp_item:
                temp_result = temp_result * 5
                temp_result += 4
        result_list.append(temp_result)
    while len(result_list) > 1:
        result_list.remove(max(result_list))
        result_list.remove(min(result_list))
    print(result_list)

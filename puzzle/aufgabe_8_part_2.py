from pathlib import Path
import re

if __name__ == '__main__':
    input_puzzle = Path('input_puzzle6.log')
    with open(input_puzzle) as file:
        value = file.read().splitlines()
    value_list_1 = []
    value_list_2 = []
    for item in value:
        value_list_1 = [item.split('|', 1)[0] for item in value]
        value_list_2 = [item.split('|', 1)[1] for item in value]
    total_count = 0
    current_count = 0
    item_exist = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for item in value_list_1:
        count = 0
        four_match = ''
        six_match = ''
        seven_match = ''
        eight_match = ''
        nine_match = ''
        numbers_written = {'zero': 'abcdefg', 'one': 'abcdefg', 'two': 'abcdefg', 'three': 'abcdefg',
                           'four': 'abcdefg', 'five': 'abcdefg', 'six': 'abcdefg', 'seven': 'abcdefg',
                           'eight': 'abcdefg', 'nine': 'abcdefg'}
        for item2 in item_exist:
            if item.count(item_exist[count]) == 4:
                numbers_written['zero'] = numbers_written['zero'].replace(item2, '')
                numbers_written['one'] = numbers_written['one'].replace(item2, '')
                numbers_written['three'] = numbers_written['three'].replace(item2, '')
                numbers_written['four'] = numbers_written['four'].replace(item2, '')
                numbers_written['five'] = numbers_written['five'].replace(item2, '')
                numbers_written['seven'] = numbers_written['seven'].replace(item2, '')
                numbers_written['nine'] = numbers_written['nine'].replace(item2, '')
                four_match = item_exist[count]
            elif item.count(item_exist[count]) == 6:
                numbers_written['one'] = numbers_written['one'].replace(item2, '')
                numbers_written['two'] = numbers_written['two'].replace(item2, '')
                numbers_written['three'] = numbers_written['three'].replace(item2, '')
                numbers_written['seven'] = numbers_written['seven'].replace(item2, '')
                six_match = item_exist[count]
            elif item.count(item_exist[count]) == 7:
                numbers_written['zero'] = numbers_written['zero'].replace(item2, '')
                numbers_written['one'] = numbers_written['one'].replace(item2, '')
                numbers_written['two'] = numbers_written['two'].replace(item2, '')
                numbers_written['three'] = numbers_written['three'].replace(item2, '')
                numbers_written['four'] = numbers_written['four'].replace(item2, '')
                numbers_written['five'] = numbers_written['five'].replace(item2, '')
                numbers_written['seven'] = numbers_written['seven'].replace(item2, '')
                seven_match = seven_match +  item_exist[count]
            elif item.count(item_exist[count]) == 8:
                numbers_written['one'] = numbers_written['one'].replace(item2, '')
                numbers_written['two'] = numbers_written['two'].replace(item2, '')
                numbers_written['three'] = numbers_written['three'].replace(item2, '')
                numbers_written['four'] = numbers_written['four'].replace(item2, '')
                numbers_written['five'] = numbers_written['five'].replace(item2, '')
                numbers_written['six'] = numbers_written['six'].replace(item2, '')
                eight_match = eight_match + item_exist[count]
            elif item.count(item_exist[count]) == 9:
                numbers_written['zero'] = numbers_written['zero'].replace(item2, '')
                numbers_written['two'] = numbers_written['two'].replace(item2, '')
                numbers_written['six'] = numbers_written['six'].replace(item2, '')
                numbers_written['nine'] = numbers_written['nine'].replace(item2, '')
                nine_match = item_exist[count]
            count += 1
        total = 0
        number_string = []
        new_string = []
        current_val = []
        reg_match_four = re.compile('[' + four_match + ']')
        reg_match_six = re.compile('[' + six_match + ']')
        reg_match_seven = re.compile('[' + seven_match + ']')
        reg_match_eight = re.compile('[' + eight_match + ']')
        reg_match_nine = re.compile('[' + nine_match + ']')
        while total < 4:
            item = value_list_2[current_count].split(' ', 4)[total + 1]
            # print(item)
            if re.fullmatch('[a-z]{2}', item):
                current_val.append(1)
                total += 1
            elif re.fullmatch('[a-z]{4}', item):
                current_val.append(4)
                total += 1
            elif re.fullmatch('[a-z]{3}', item):
                current_val.append(7)
                total += 1
            elif re.fullmatch('[a-z]{7}', item):
                current_val.append(8)
                total += 1
            elif len(item) == 6:
                if len(re.findall(reg_match_four, item)) == 1:
                    if len(re.findall(reg_match_seven, item)) == 2:
                        current_val.append(6)
                    else:
                        current_val.append(0)
                else:
                    current_val.append(9)
                total += 1
            elif len(item) == 5:
                if len(re.findall(reg_match_four, item)) == 1:
                    current_val.append(2)
                else:
                    if len(re.findall(reg_match_six, item)) == 1:
                        current_val.append(5)
                    else:
                        current_val.append(3)
                total += 1
        current_count += 1
        new_string = [str(item) for item in current_val]
        number_string = ''.join(new_string)
        total_count = total_count + int(number_string)
        print(number_string)
    print(total_count)

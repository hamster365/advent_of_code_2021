from pathlib import Path

if __name__ == '__main__':
    input_puzzle = Path('input_puzzle7.log')
    with open(input_puzzle) as file:
        value = file.read().splitlines()

    total_count = 0
    output_result = 0
    basin_count = 0
    for item in value:
        temp_count = 0
        smallest_list = []
        count_list = []
        if total_count == 0 or total_count == 99:

            if total_count == 0:
                while temp_count < len(item):
                    if 1 <= temp_count <= 98:
                        if item[temp_count] < item[temp_count - 1] and item[temp_count] < item[temp_count + 1]:
                            smallest_list.append(item[temp_count])
                            count_list.append(temp_count)
                    elif temp_count == 0:
                        if item[temp_count] < item[temp_count + 1]:
                            smallest_list.append(item[temp_count])
                            count_list.append(temp_count)
                    elif temp_count == 99:
                        if item[temp_count] < item[temp_count - 1]:
                            smallest_list.append(item[temp_count])
                            count_list.append(temp_count)
                    temp_count += 1
                future_list = str([value[total_count + 1]])
                count = 0
                for items in smallest_list:
                    if future_list[count_list[count] + 2] > items:
                        output_result = output_result + (int(items) + 1)
                        basin_count += 1
                        print(total_count, count_list[count] + 2)
                    count += 1
            if total_count == 99:
                while temp_count < len(item):
                    if 1 <= temp_count <= 98:
                        if item[temp_count] < item[temp_count - 1] and item[temp_count] < item[temp_count + 1]:
                            smallest_list.append(item[temp_count])
                            count_list.append(temp_count)
                    elif temp_count == 0:
                        if item[temp_count] < item[temp_count + 1]:
                            smallest_list.append(item[temp_count])
                            count_list.append(temp_count)
                    elif temp_count == 99:
                        if item[temp_count] < item[temp_count - 1]:
                            smallest_list.append(item[temp_count])
                            count_list.append(temp_count)
                    temp_count += 1
                past_list = str([value[total_count - 1]])
                count = 0
                for items in smallest_list:
                    if past_list[count_list[count] + 2] > items:
                        output_result = output_result + (int(items) + 1)
                        basin_count += 1
                        print(total_count, count_list[count] + 2)
                    count += 1
        else:
            while temp_count < len(item):
                if 1 <= temp_count <= 98:
                    if item[temp_count] < item[temp_count - 1] and item[temp_count] < item[temp_count + 1]:
                        smallest_list.append(item[temp_count])
                        count_list.append(temp_count)
                elif temp_count == 0:
                    if item[temp_count] < item[temp_count + 1]:
                        smallest_list.append(item[temp_count])
                        count_list.append(temp_count)
                elif temp_count == 99:
                    if item[temp_count] < item[temp_count - 1]:
                        smallest_list.append(item[temp_count])
                        count_list.append(temp_count)
                temp_count += 1
            future_list = str([value[total_count + 1]])
            past_list = str([value[total_count - 1]])
            count = 0
            for items in smallest_list:
                if future_list[count_list[count] + 2] > items and past_list[count_list[count] + 2] > items:
                    output_result = output_result + (int(items) + 1)
                    basin_count += 1
                    print(total_count, count_list[count] + 2)
                count += 1
        total_count += 1
    print(output_result)
    print(basin_count)

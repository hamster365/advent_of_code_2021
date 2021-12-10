if __name__ == '__main__':
    initial_fish = [1, 2, 4, 5, 5, 5, 2, 1, 3, 1, 4, 3, 2, 1, 5, 5, 1, 2, 3, 4, 4, 1, 2, 3, 2, 1, 4, 4, 1, 5, 5, 1, 3,
                    4,
                    4, 4, 1, 2, 2, 5, 1, 5, 5, 3, 2, 3, 1, 1, 3, 5, 1, 1, 2, 4, 2, 3, 1, 1, 2, 1, 3, 1, 2, 1, 1, 2, 1,
                    2,
                    2, 1, 1, 1, 1, 5, 4, 5, 2, 1, 3, 2, 4, 1, 1, 3, 4, 1, 4, 1, 5, 1, 4, 1, 5, 3, 2, 3, 2, 2, 4, 4, 3,
                    3,
                    4, 3, 4, 4, 3, 4, 5, 1, 2, 5, 2, 1, 5, 5, 1, 3, 4, 2, 2, 4, 2, 2, 1, 3, 2, 5, 5, 1, 3, 3, 4, 3, 5,
                    3,
                    5, 5, 4, 5, 1, 1, 4, 1, 4, 5, 1, 1, 1, 4, 1, 1, 4, 2, 1, 4, 1, 3, 4, 4, 3, 1, 2, 2, 4, 3, 3, 2, 2,
                    2,
                    3, 5, 5, 2, 3, 1, 5, 1, 1, 1, 1, 3, 1, 4, 1, 4, 1, 2, 5, 3, 2, 4, 4, 1, 3, 1, 1, 1, 3, 4, 4, 1, 1,
                    2,
                    1, 4, 3, 4, 2, 2, 3, 2, 4, 3, 1, 5, 1, 3, 1, 4, 5, 5, 3, 5, 1, 3, 5, 5, 4, 2, 3, 2, 4, 1, 3, 2, 2,
                    2,
                    1, 3, 4, 2, 5, 2, 5, 3, 5, 5, 1, 1, 1, 2, 2, 3, 1, 4, 4, 4, 5, 4, 5, 5, 1, 4, 5, 5, 4, 1, 1, 5, 3,
                    3,
                    1, 4, 1, 3, 1, 1, 4, 1, 5, 2, 3, 2, 3, 1, 2, 2, 2, 1, 1, 5, 1, 4, 5, 2, 4, 2, 2, 3
                    ]
    total_fish = len(initial_fish)
    total_count = 0
    while total_count < 256:
        current_count = 0
        fish_count = 0
        count = 0
        for item in initial_fish:
            initial_fish[current_count] -= 1
            if initial_fish[current_count] < 0:
                total_fish = total_fish + 1
                initial_fish[current_count] = 6
                fish_count += 1
            current_count += 1
        while count < fish_count:
            initial_fish.append(8)
            count += 1
        total_count += 1
        print(total_count)
    print(total_fish)
    print(initial_fish)
    print(len(initial_fish))

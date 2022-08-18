t = int(input())

for _ in range(t):
    n, q = [int(x) for x in input().split()]

    arr = [int(x) for x in input().split()]

    initial_arr = list(arr)

    to_print: list[int] = []

    for _ in range(q):
        fighter, k = [int(x) for x in input().split()]

        strength = initial_arr[fighter - 1]

        if k < fighter - 2:
            to_print.append(0)

        elif list(filter(lambda x: x > strength, initial_arr[:fighter])):
            to_print.append(0)

        elif strength == n: # if strongest one, it's the number of elems
            if fighter <= 2:
                to_print.append(k)
            else:
                to_print.append(k - fighter + 2)

        else:
            nearest_count = -1
            for j in initial_arr[fighter - 1:]:
                if j > strength:
                    break
                nearest_count += 1
                num_wins = min(nearest_count, k)
            to_print.append(num_wins)
            continue

    print(*to_print, sep="\n")

    
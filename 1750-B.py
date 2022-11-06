t = int(input())

for _ in range(t):
    n = int(input())
    bits = [int(x) for x in input()]

    max_1s = 0
    max_0s = 0
    cons_1s = 0
    cons_0s = 0
    all_1s = 0
    all_0s = 0

    for b in bits:
        if b == 1:
            all_1s += 1
            cons_1s += 1
            max_0s = max(max_0s, cons_0s)
            cons_0s = 0
        else:
            all_0s += 1
            cons_0s += 1
            max_1s = max(max_1s, cons_1s)
            cons_1s = 0

    max_0s = max(max_0s, cons_0s)
    max_1s = max(max_1s, cons_1s)

    bits_cost = 0
    if (all_1s != 0 and all_0s != 0):
        bits_cost = all_1s * all_0s

    elif all_0s == 0:
        bits_cost = all_1s * all_1s
    elif all_1s == 0:
        bits_cost = all_0s * all_0s

    print(max(
        max_1s * max_1s, max_0s * max_0s, bits_cost
    ))
t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    res = []

    # mountain-valley approach
    # at most two colors.
    # if the sequence is already beautiful,
    # only need one color.

    # let ( = +1, ) = -1.

    acc = 0
    seen_positive = False
    seen_negative = False

    for (i, c) in enumerate(s):
        if c == "(":
            acc += 1
        else:
            acc -= 1

        if (acc == 0):
            # same as the last color
            res.append(res[-1])
        elif (acc > 0):
            seen_positive = True

            # 1 corresponds to positive
            res.append(1)
        else:
            seen_negative = True

            # 2 corresponds to negative
            res.append(2)

    if (acc != 0):
        # unbalanced
        print(-1)
    elif (seen_negative != seen_positive):
        print(1)
        print(" ".join(["1" for _ in range(len(s))]))
    else:
        print(2)
        print(" ".join([str(x) for x in res]))
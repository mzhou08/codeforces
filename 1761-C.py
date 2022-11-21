t = int(input())

for _ in range(t):
    n = int(input())
    b = []
    ins = {i: [] for i in range(n)} # track all sets that are subset of i
    outs = {i: [] for i in range(n)} # track all sets that i is a subset of
    for i in range(n):
        row = [int(x) for x in input()]

        for j in range(len(row)):
            if row[j] == 1:
                ins[j].append(i)
                outs[i].append(j)

    # sort ins
    ins = dict(sorted(ins.items(), key=lambda x: len(x[1])))

    sets = {i: set() for i in range(n)}

    curr_num = 1

    for setnum, insets in ins.items():
        if len(insets) == 0:
            sets[setnum] = set([curr_num])
            curr_num += 1

        elif len(insets) == 1:
            child = insets[0]
            temp = sets[child]
            sets[setnum] = temp.union(set([curr_num]))
            curr_num += 1
        else:
            for child in insets:
                sets[setnum] |= sets[child]
            if not all(sets[setnum] != sets[child] for child in insets):
                sets[setnum] |= set([curr_num])
                curr_num += 1

    for i in range(n):
        set_str = " ".join(str(x) for x in sets[i])
        print(f"{len(sets[i])} {set_str}")

    
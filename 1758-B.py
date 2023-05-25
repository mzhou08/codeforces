t = int(input())

for _ in range(t):
    n = int(input())

    if n % 2 == 1:
        print(" ".join(str(3) for _ in range(n)))

    else:
        half = n //2
        res = []
        if half % 2 == 0:
            res = [2 ** half for _ in range(half)]
            res[-1] += 1
            res[-2] += 1
            res += [2 ** i for i in range(half)]
            print(' '.join(res))
        else:
            
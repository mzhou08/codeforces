t = int(input())

for _ in range(t):
    n = int(input())

    nums = [int(x) for x in input().split()]

    if n <= 3:
        print(n)
    else:
        res = -1

        for i in range(n):
            if not nums[(i - 1) % n] == nums[(i + 1) % n]:
                res = n
                break
        if res != n:
            # we have period of 2
            res = n // 2 + 1
        print(res)

    
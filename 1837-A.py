n = int(input())
for _ in range(n):
    x, k = [int(y) for y in input().split()]

    if (x % k == 0):
        print(2)
        print(f"{x-1} {1}")
    else:
        print(1)
        print(x)
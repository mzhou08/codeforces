'''
SOLVED
'''

t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]

    if k % 4 == 0:
        print("NO")

    elif k % 2 == 0: # is even but not multiple of 4
        print("YES")
        for i in range(1, (n // 2) + 1):
            if i % 2 == 0: # means that 2 * i is div by 4
                print(f"{(2 * i) - 1} {2 * i}")
            else:
                print(f"{2 * i} {(2 * i) - 1}")

    else: # k is odd
        print("YES")
        for i in range(1, (n // 2) + 1):
            print(f"{(2 * i) - 1} {2 * i}")


        
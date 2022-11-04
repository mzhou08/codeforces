t = int(input())

for _ in range(t):
    n = int(input())

    m = (n // 2) + (n % 2)

    print(m)

    for i in range(m):
        if i < n //2:
            print(f"{3*i + 1} {3 * n - (3 * i + 1)}")
        else:
            print(f"{3*(n // 2) + 1} {3 * (n // 2) + 2} ")
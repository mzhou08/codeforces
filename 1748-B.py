from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    res = 0

    for i in range(n):
        for j in range(i + 1):
            counts = Counter(s[j:i + 1])
            if max(counts.values()) <= len(counts):
                res += 1

    print(res)
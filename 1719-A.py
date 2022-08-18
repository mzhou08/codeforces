'''
SOLVED
'''

t = int(input())

for _ in range(t):
    m, n = [int(x) for x in input().split()]

    if m % 2 == n % 2:
        print("Tonya")
    else:
        print("Burenka")
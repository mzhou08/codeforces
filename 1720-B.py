'''
SOLVED
'''

t = int(input())

to_print = []

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]

    s_to_l = sorted(arr)

    S, s, l, L = [s_to_l[0], s_to_l[1], s_to_l[-2], s_to_l[-1]]

    to_print.append(l + L - s - S)

print(*to_print, sep="\n")
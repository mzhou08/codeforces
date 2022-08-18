'''
SOLVED
'''

t = int(input())

to_print = []

for _ in range(t):
    a, b, c, d = [int(x) for x in input().split()]

    ad = a * d
    bc = b * c

    if ad == bc:
        to_print.append("0")
    elif bc == 0 or ad == 0 or ad % bc == 0 or bc % ad == 0:
        to_print.append("1")
    else:
        to_print.append("2")

print(*to_print, sep="\n")
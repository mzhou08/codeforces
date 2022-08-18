t = int(input())

memos = {0: [], 1: [1]}

def get_memo(n, acc) -> list[int]:
    if n not in memos:
        res =get_memo(n - 2))
        prefix.extend([n, n - 1])
        memos[n] = prefix
    return memos[n]

for _ in range(t):
    n = int(input())
    print(*get_memo(n))
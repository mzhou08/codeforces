t = int(input())

# memos = {0: [], 1: [1]}

# def create_memo(n, acc) -> list[int]:
#     if n not in memos:
#         return create_memo(n - 2)
#         acc.extend([n, n - 1])
#     return acc

for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        for i in range(n // 2):
            print(f"{(2 * i) + 2} {(2 * i) + 1}", end=" ")
    else:
        print("1", end=" ")
        for i in range(n // 2):
            print(f"{(2 * i) + 3} {(2 * i) + 2}", end=" ")
    print("")
'''
SOVLED
'''

def is_optimal_reduction():
    n = int(input())
    arr: list[int] = [int(elem) for elem in input().split()]

    curr_min: int = arr[0]
    new_min: bool = False

    for elem in arr:
        if elem < curr_min:
            curr_min = elem
            new_min = True
        elif new_min and elem > curr_min:
            return False
        else:
            curr_min = elem
    return True


t = int(input())
for _ in range(t):
    print("YES") if is_optimal_reduction() else print("NO")

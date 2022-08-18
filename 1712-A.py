t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]

    num_operations = 0

    for i in range(len(arr)):
        if i >= k and arr[i] <= k:
            num_operations += 1

    print(num_operations)

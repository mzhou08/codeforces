def generate_wins_by_strength(
    n: int,
) -> tuple[dict[int, int], int]:
    # returns a tuple of:
    #   - wins by strength
    #   - number of rounds to get to cycle

    rounds_passed = 0

    wins: dict[int, int] = {i: 0 for i in range(1, n + 1)}
    # wins keyed by strength

    while arr[0] != n: # while the strongest fighter is not first

        if arr[0] > arr[1]:
            wins[arr[0]] += 1 # stronger fighter gets a win
            loser = arr.pop(1)
        else:
            wins[arr[1]] += 1 # stronger fighter gets a win
            loser = arr.pop(0)

        arr.append(loser)
        rounds_passed += 1

    return (wins, rounds_passed)

t = int(input())

for _ in range(t):
    n, q = [int(x) for x in input().split()]

    arr = [int(x) for x in input().split()]

    initial_arr = list(arr)

    wins, rounds_until_cycle = generate_wins_by_strength(n)

    to_print: list[int] = []

    for _ in range(q):
        fighter, k = [int(x) for x in input().split()]

        strength = initial_arr[fighter - 1]

        if k < rounds_until_cycle:
            if list(filter(lambda x: x > strength, initial_arr[:fighter])):
                num_wins = 0
            else:
                nearest_count = 0
                for j in initial_arr[fighter:]:
                    nearest_count += 1
                    if j > strength:
                        break
                num_wins = min(nearest_count, k)
            to_print.append(num_wins)
            continue

        if strength == n:
            to_print.append(wins[strength] + k - rounds_until_cycle)
        else:
            to_print.append(wins[strength])

    print(*to_print, sep="\n")

    
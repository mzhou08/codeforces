t = int(input())

for _ in range(t):
    n = int(input())
    s = [c for c in input().strip()]

    max_streak = 1
    streak = 1
    for i in range(1, len(s)):
        if (s[i] == s[i - 1]):
            streak += 1
            max_streak = max(streak, max_streak)
        else:
            max_streak = max(streak, max_streak)
            streak = 1

    max_streak = max(streak, max_streak)
    print(max_streak + 1)


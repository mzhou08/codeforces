t = int(input())

for _ in range(t):
    s = input().strip()

    res = s

    streaks = []
    streak = 1

    for i in range(1, len(s)):
        if (s[i] == s[i - 1]):
            streak += 1
        else:
            streaks.append(s[i-1] * streak)
            streak = 1

    streaks.append(s[-1] * streak)

    for i in range(len(streaks)):
        streak_str = streaks[i]
        n = len(streak_str)

        if streak_str[0] == "?":
            if (i == 0):
                print("0" * n, end="")
            elif (i == len(streaks) - 1):
                print("1" * n, end="")
            else:
                prev_char = streaks[i - 1][0]
                next_char = streaks[i + 1][0]

                if (prev_char != next_char):
                    print("1" * n, end="")
                else:
                    print(prev_char * n, end="")
        else:
            print(streak_str, end="")
    print("")
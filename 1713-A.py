'''
SOLVED
'''

def find_greatest_rectangle_dimensions() -> tuple[int, int]:
    num_points = int(input())
    xs = [0]
    ys = [0]
    for _ in range(num_points):
        x, y = [int(elem) for elem in input().split(' ')]
        xs.append(x)
        ys.append(y)

    return (max(xs) - min(xs), max(ys) - min(ys))

num_cases = int(input())

for _ in range(num_cases):
    x_dim, y_dim = find_greatest_rectangle_dimensions()
    print(f"{2 * (x_dim + y_dim)}")

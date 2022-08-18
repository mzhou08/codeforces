'''
UNSOLVED - TLE
'''

t = int(input())

def exists_n_square(matrix: list[list[int]], n: int) -> tuple[int, int]:
    # returns coords of first occurence, by row then col,
    # of the top left of a 2x2 square where sum of elems is n
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(num_rows - 1):
        for j in range(num_cols - 1):
            if (
                matrix[i][j] +
                matrix[i + 1][j] +
                matrix[i][j + 1] +
                matrix[i + 1][j + 1] == n
            ):
                return i, j
    return (-1, -1)


for _ in range(t):
    num_rows, num_cols  = [int(x) for x in input().split()]

    matrix = []

    for _ in range(num_rows):
        matrix.append([int(x) for x in input()])

    num_operations = 0

    while True:
        two_i, two_j = exists_n_square(matrix, 2)

        if two_i != -1 and two_j != -1:
            matrix[two_i][two_j] = 0
            matrix[two_i + 1][two_j] = 0
            matrix[two_i][two_j + 1] = 0
            matrix[two_i + 1][two_j + 1] = 0

            num_operations += 2
            continue

        one_i, one_j = exists_n_square(matrix, 1)

        if one_i != -1 and one_j != -1:
            matrix[one_i][one_j] = 0
            matrix[one_i + 1][one_j] = 0
            matrix[one_i][one_j + 1] = 0
            matrix[one_i + 1][one_j + 1] = 0

            num_operations += 1
            continue

        three_i, three_j = exists_n_square(matrix, 3)

        if three_i != -1 and three_j != -1:
            matrix[three_i][three_j] = 0
            matrix[three_i + 1][three_j] = 0
            matrix[three_i][three_j + 1] = 0
            matrix[three_i + 1][three_j + 1] = 0

            num_operations += 2
            continue

        four_i, four_j = exists_n_square(matrix, 4)

        if four_i != -1 and four_j != -1:
            matrix[four_i][four_j] = 0
            matrix[four_i + 1][four_j] = 0
            matrix[four_i][four_j + 1] = 0
            matrix[four_i + 1][four_j + 1] = 0

            num_operations += 2
            continue

        # if you've reached here, there are all 0's
        break

    print(num_operations)
        



    
        


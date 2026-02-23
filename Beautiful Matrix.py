matrix = []

for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            # Manhattan distance to center (2,2)
            moves = abs(i - 2) + abs(j - 2)
            print(moves)
            exit()

rows = 3
columns = 3

matrix_a = []
matrix_b = []
for row in range(rows):
    col_a = []
    # col_b = []
    for col in range(columns):
        a = int(input())
        col_a.append(a)
    matrix_a.append(col_a)

print(matrix_a)

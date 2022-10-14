tc = int(input())
size = int(input())
mat =[]
case = 0
while case < tc:
    case +=1
    for i in range(size):
        values = list(map(int,input().split()))
        mat.append(values)

    # print(mat)
    sum_values = []
    for row in mat:
        if len(row) % 2 == 0:
            val = sum(row)
            sum_values.append(val)
        else:
            pass
    # print(sum_values)
    if len(sum_values) == 0:
        print(0)
    elif len(sum_values) % 2 == 0:
        sub = sum_values[0] - sum_values[1]
        print(sub)
    else:
        print(0)
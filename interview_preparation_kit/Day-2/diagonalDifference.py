from traceback import print_tb


n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

# result = diagonalDifference(arr)

print(arr)

# [[1, 2, 3], 
# [5, 6, 7], 
# [8, 9, 0]]

for i in range(0,len(arr)):

    # print(i)
    val = arr[i]
    # print(val)
    
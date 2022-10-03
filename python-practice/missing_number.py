# a =[1,2,4,5]

final_value = []

# val = int(input())
val = list(map(int, input().split()))

# for ele in range(1,11)
for ele in range(val[0], val[-1]+1):

    if ele not in val:

        final_value.append(ele)

print(final_value)  
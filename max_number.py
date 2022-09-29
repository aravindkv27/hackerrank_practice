size_of_array = int(input())

input_values = []
for i in range(size_of_array):

    values = list(map(int,input().split()))
    input_values.append(values)

# print(input_values)
final_answer=[]
for l in input_values:

    # print(l)
    l.sort()
    final_answer.append(l[-1])

print(final_answer)
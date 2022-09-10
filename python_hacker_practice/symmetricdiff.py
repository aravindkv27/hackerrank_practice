# Enter your code here. Read input from STDIN. Print output to STDOUT
a_size_set = int(input())

a_ele = set(map(int,input().strip().split()))

b_size_set = int(input())

b_ele = set(map(int,input().strip().split()))

# print(a_ele, b_ele)

val_a = a_ele.difference(b_ele)

val_b = b_ele.difference(a_ele)


final_val = val_a.union(val_b)

# print(final_val)
final_list = list(final_val)

final_list.sort()


for i in final_list:
    print(i)
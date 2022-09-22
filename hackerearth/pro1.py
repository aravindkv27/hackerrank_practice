# a = list(map(str,input().split()))

a = str(input())
b = str(input())

# print(a)

# for i in a:

my_str = a.casefold()

# print(my_str)

rev_str = reversed(b)

if list(my_str) == list(rev_str):

    print(True)

else:
    print(False)

# a = int(input())
# b  = int(input())

# count = 1
# for i in range(1,a+1):

#     count = count*b

# print(count)
# a = [1,2,1,3,4]

a = list(map(int,input().split()))

a.sort()
#  [1,1,2,3,4]
for i in range(1,len(a)):
    
    if a[i] == a[i-1]:

        print(a[i])
# print(a)

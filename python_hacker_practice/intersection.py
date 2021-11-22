n=int(input())

a=list(map(int,input().strip().split()))[:n]

o=int(input())

b=list(map(int,input().strip().split()))[:o]

ans=set(a).intersection(set(b))

ans_list=list(ans)

count=0
for i in ans_list:
    count+=1    
    
print(count)
# print(ans_list.count())

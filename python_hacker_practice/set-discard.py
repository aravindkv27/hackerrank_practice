n = int(input())
s = set(map(int, input().split()))

num=int(input())

for i in range(0,num):
    a=list(input().split())
    if a[0]=="pop":
        s.pop()
    if a[0]=="remove":
        s.remove(int(a[1]))
    if a[0]=="discard":
        s.discard(int(a[1]))

fl=list(s)

# print(fl)
final_ans=0
for i in range(0,len(fl)):
    final_ans =final_ans + fl[i]
    
print(final_ans)

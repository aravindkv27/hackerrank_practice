import itertools 

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

ans=itertools.permutations([x-1,y-1,z],n+1)

perm_list=[]

for i in list(ans):

    print(i)
    final_ans=perm_list.append(i)

print(perm_list.sort())

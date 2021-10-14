if __name__ == '__main__':
    N = int(input())

ls=[]
for i in range(0,N):
    tet=input().split(" ")
    text=tet[0]

    if text=="insert":
        index=int(tet[1])
        obj=int(tet[2])
        ls.insert(index,obj)
    if text=="remove":
        rm=int(tet[1])
        ls.remove(rm)
    if text=="append":
        app=int(tet[1])
        ls.append(app)
    if text=="sort":
        ls.sort()
    if text=="pop":
        ls.pop()
    if text=="reverse":
        ls.reverse()
    if text=="print":
        print(ls)
        
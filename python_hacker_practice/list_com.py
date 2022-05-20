if __name__ == '__main__':
    N = int(input())
    list1=[1]
    for i in range(N):
        raw_in= input().split()
        if raw_in[0] =="insert":
            list1.insert(int(raw_in[1]),int(raw_in[2]))
        if raw_in[0]=='remove':
            list1.remove(int(raw_in[1]))
        if raw_in[0]=='print':
            print(list1)
        if raw_in[0]=='append':
            list1.append(int(raw_in[1]))
        if raw_in[0]=='sort':
            list1.sort()
        if raw_in[0]=='pop':
            list1.pop()
        if raw_in[0]=='reverse':
            list1.reverse()
    
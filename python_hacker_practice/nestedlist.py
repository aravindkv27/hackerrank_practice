if __name__ == '__main__':
    
    names=[]

    for _ in range(int(input())):
        name = input()
        score = float(input())
        data=[name,score]
        names.append(data)

    # print(names)

    a=sorted(names,key=lambda x : x[1], reverse=True)
    # a=names.sort(key=lambda a : a[1])
    # print(a)
    mark=a[0][0]

    for i in range(1,len(a)):
        
        if 
    

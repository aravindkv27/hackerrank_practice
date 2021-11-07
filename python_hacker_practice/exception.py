a=int(input())

for i in range(0,a):

    try: 
        b,c= map(int,input().split())
        print(b//c)
    
    except Exception as e:

        print("Error code:",e)




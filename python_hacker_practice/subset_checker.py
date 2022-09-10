# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases = int(input())

for i in range(0,test_cases):
    
    no_a_ele = int(input())
    aelements = list(map(int,input().strip().split()))[:no_a_ele]
    no_b_ele = int(input())
    belements = list(map(int,input().strip().split()))[:no_b_ele]
    
    
    a = set(aelements)
    b = set(belements)
    if a.issubset(b):
        
        print("True")
    # elif b.issubset(a):
        
    #     print("True")
    
    else:
        print("False")
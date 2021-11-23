ans_list=[]

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a=0
    b=1
    # ans_list.append(a)
    # ans_list.append(b)
    for i in range(n):
        
        yield a
        ans=a+b
        # ans_list.append(ans)
        a=b
        b=ans


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
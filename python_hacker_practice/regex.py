import re

a=int(input())

for i in range(0,a):

    a=input()
    try:
        r=re.compile(a)
        print(True)
    except re.error:

        print(False)




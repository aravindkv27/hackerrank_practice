from cgi import test
from tokenize import Triple


test_case = int(input())

def arrange(val):

    even_numbers = []
    odd_numbers = []   
    for i in range(1,val+1):

        if i % 2 ==0:

            even_numbers.append(i)

        else:

            odd_numbers.append(i)

    even_numbers.sort(reverse=True)
    odd_numbers.extend(even_numbers)
    for value in odd_numbers:

        print(value,end=" ")

for i in range(test_case):

    val = int(input())
    arrange(val)

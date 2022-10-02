import numpy as ns

c = int(input("No of Columns: "))
r = int(input("No of Rows: "))
mat1 = [[int(input()) for x in range (c)] for y in range(r)]

mat2 = [[int(input()) for col in range(c)] for row in range(r)]

a = ns.array(mat1)
b = ns.array(mat2)

add = ns.add(a,b)

sub = ns.subtract(a,b)

print(add)
print(sub)
#Python program to find prime numbers within a range

start = int(input())
stop = int(input())

# print("Prime numbers between", start, "and", stop, "are:")

for val in range(start+1, stop):
  if val > 1:
    for i in range(2, val):
      if (val % i) == 0:
        break
    else:
      print(val, end=" ")
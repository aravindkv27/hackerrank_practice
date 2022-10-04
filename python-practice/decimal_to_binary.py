from inspect import stack


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items

decimal_number = int(input())
    
s = stack()

if decimal_number == 0:

    print(0)

while decimal_number > 0:

    rem = decimal_number % 2
    s.push(rem)
    decimal_number = decimal_number // 2
    print(decimal_number)

bin_number = ""
while not s.is_empty():
    bin_number += str(s.pop())

print(bin_number)
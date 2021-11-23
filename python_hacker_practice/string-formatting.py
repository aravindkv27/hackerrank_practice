def print_formatted(number):
    # your code goes here
    a=len(bin(number)[2:])
    for i in range(1,number+1):

        print(str(i).rjust(a),oct(i)[2:].rjust(a),hex(i)[2:].upper().rjust(a),bin(i)[2:].rjust(a))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
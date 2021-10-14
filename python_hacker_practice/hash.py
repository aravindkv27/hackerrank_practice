if __name__ == '__main__':
    n = int(input())
    integer_list =input().split()
    int_list=map(int,integer_list)
    tup=tuple(int_list)
    print(hash(tup))

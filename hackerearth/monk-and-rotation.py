test_case = int(input())

while test_case != 0:   

    no_of_ele, no_of_rot = input().split()

    elements = list(map(int,input().strip().split()))[:int(no_of_ele)]

    index = int(no_of_ele) - (int(no_of_rot)%int(no_of_ele))

    value = []

    for i in range(index,int(no_of_ele)):

        value.append(elements[i])

    for i in range(index):

        value.append(elements[i])

    print(*value, sep=' ')
        
    test_case = test_case - 1
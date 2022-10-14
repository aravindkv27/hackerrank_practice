
def split_list(Input_list, n):
    for i in range(0, len(Input_list), n):
        yield Input_list[i:i + n]

A = [-1,-3,4,7,7,7]
def solution(A):
    final_val = []
    if len(A)% 2 == 0:

        val = split_list(A,2)
        # print(list(val))
    else:
        print("False")
    even_numbers = []
    # if len(A) %2 !=0:
    #     return False
    for i in val:
        # print(i)
        ans = sum(i)
        print(ans)
        if ans % 2 != 0:
            final_val.append(ans)
        if ans % 2 ==0:
            even_numbers.append(ans)

    if len(final_val) == 0:

        print("True")

    else:
        print("falsw")
    
    

solution(A)
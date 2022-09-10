def average(array):
    # your code goes here
    
    arr_to_set = set(array)
    
    len_of_set=  len(arr_to_set)
    # print(arr_to_set)
    set_to_list = list(arr_to_set)
    
    final_val = 0
    
    for i in range(0,len(set_to_list)):
        
        final_val = final_val + set_to_list[i]
        
    ans = final_val / len_of_set
    
    # print(ans)
    return ans
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
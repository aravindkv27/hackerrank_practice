# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
main_list = list(map(int,input().strip().split()))

main_set = set(main_list)
other_sets = int(input())

# to_check_set = []

to_check_set = True

for i in range(0,other_sets):
    
    a = list(map(int,input().strip().split()))
    
    val = set(a)
    
    if not val.issubset(main_set):
        
        # to_check_set.append(0)
        to_check_set = False
        
print(to_check_set)
        
    # else:
        
    #     to_check_set.append(1)
        

# # print(to_check_set)
# final_val = set(to_check_set)

# # print(final_val)
# final_list = list(final_val)

# if len(final_val) >= 1:
    
#     print("False")

# elif final_list[0] == 1:
    
#     print("False")
    
# else:
    
#     print("True")
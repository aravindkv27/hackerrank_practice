# data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
data_list = [1,3,4,6,5]
new_list = []

while data_list:
    minimum = data_list[0] 
    print(minimum)
     # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print (new_list)    
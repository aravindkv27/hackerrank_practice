arr= list(map(int,input().split()))

arr.sort()

print(arr)

length_array= len(arr)
    
find_median = int(length_array / 2)
    
print(arr[find_median])
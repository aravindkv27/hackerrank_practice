string_value = str(input())

reverse_string = string_value[::-1]

print(reverse_string)

sv_list = list(string_value)
rv_string = list(reverse_string)

count = 0

for i in range(0,len(sv_list)):

    if sv_list[i] == rv_string[i]:

        count = count + 1

print(count)
my_list = [7 ,3 ,4 ,5 ,10]

for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i+1]:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(f'sorted list is here -> {my_list}')
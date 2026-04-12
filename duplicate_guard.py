# writing a simple program to print the duplicates in a list using nested loops one acts as fixed and other scans
my_list = [21 ,23 ,25 ,2 ,21, 10 ,21 ,10]  
duplicate = []
for x in range(len(my_list)):
    for y in range(x+1 ,len(my_list)):
        if my_list[x] == my_list[y]:
            if my_list[x] not in duplicate:
                duplicate.append(my_list[x])
print(f'duplicate values in list: {duplicate}')
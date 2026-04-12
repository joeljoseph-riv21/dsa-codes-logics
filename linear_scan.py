# finding the largest number in the given list

my_list = [10, 21, 35, 47, 59, 32, 2, 23 ,17]
largest = my_list[0]
for nums in my_list:
    if nums > largest:
        largest = nums
print(f'The largest number in the list is: {largest}')
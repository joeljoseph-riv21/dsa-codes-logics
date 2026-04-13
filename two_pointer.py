#returning the subtraction of 2 numbers that equals target
my_list = [7 ,3 ,4 ,5 ,10 ,3]
target = 7

# Sort the list first for two-pointer technique
my_list.sort()
print(f"Sorted list: {my_list}")

left_pointer = 0
right_pointer = len(my_list) - 1

while left_pointer < right_pointer:
    difference = my_list[right_pointer] - my_list[left_pointer]
    if difference == target:
        print(f'Yes, the numbers {my_list[right_pointer]} and {my_list[left_pointer]} gives the target {target}')
        break
    elif difference < target:
        left_pointer += 1  
    else:
        right_pointer -= 1  

if left_pointer >= right_pointer:
    print(f"No pair found that subtracts to {target}")



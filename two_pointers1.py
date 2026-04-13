my_list = [8 ,9 ,10 ,12 ,16]
target = 120
left = 0
right = len(my_list) - 1
while left < right:
    product = my_list[left] * my_list[right]
    if product == target:
        print(f' The numbers {my_list[left]} and {my_list[right]} give the target {target}')
        break
    elif product < target:
        left = left + 1 
    else:
        right = right - 1 
print(f'-And the target i.e.,{target} is accomplished !!!')

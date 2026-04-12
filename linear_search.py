#Goal: To find a number that exists in the list here the number is 21
my_list = [10, 21, 35, 47, 59, 32, 2, 23 ,17]
target = 21

for i in range(len(my_list)):
    if list[i] == target:
        print(f' Yes,the number {target} is in the list and it was found in the index {i}')
        break
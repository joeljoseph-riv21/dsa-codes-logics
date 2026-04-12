# A simple program to check if the list is sorted or not 
list = [21 ,23 ,30 ,42 ,66]
is_sorted = True
for i in range(len(list)-1):
    if list[i] > list[i+1]:
        is_sorted = False
    else:
        print(f'List is sorted: {is_sorted}')
        break
    

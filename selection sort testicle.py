arr = []

amount_list = int(input("Input amount of numbers in the list\n"))
for i in range(amount_list):
    current_num_arr = float(input(f"Number {i}:\n"))
    arr.append(current_num_arr)
    i =+ 1


size = len(arr)    

for ind in range(size):
    vind = ind
    for i in range(vind + 1, size):
        if arr[ind] > arr[i]:
            vind = i
        else: 
            i =+ 1
    
    (arr[ind], arr[vind]) = (arr[vind], arr[ind])

print(arr)


    
    

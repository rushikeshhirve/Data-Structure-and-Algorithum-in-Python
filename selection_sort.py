def arrsort(arr) :
    for i in range(len(arr)) :
        min_pos = i
        for j in range(i,len(arr)) :
            if arr[j] < arr[min_pos] :
                min_pos = j

        arr[i], arr[min_pos] = arr[min_pos], arr[i],

arr = [9,2,6,4,3,99,78]
arrsort(arr)
print(arr)

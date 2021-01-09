def bubble_sort(arr) :
    """Sorted the given Array using bubble sort algorithm """
    for i in range(len(arr)-1,0, -1) :
        for j in range(i) :
            if arr[j] > arr[j+1] :
                arr[j] ,arr[j + 1] = arr[j+1], arr[j]

array = [99,69,90,12,12,-2,46,68,33]
bubble_sort(array)
print(array)
# print(bubble_sort.__doc__)
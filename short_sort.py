def quicksort(array):
    if len(array) <2:
        return array
    else:
        pivot=array[0] #точка опоры
        less=[i for i in array[1:] if i<=pivot]
        greater=[i for i in array[1:] if i>pivot]        
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 55, 2, 3]))
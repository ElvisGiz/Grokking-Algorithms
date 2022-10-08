def binary_search(list, item):
    low=0
    high=len(list)-1
    trying = 0
    while low<=high:
        mid=(low+high)//2
        guess = list[mid]
        trying=trying+1
        if guess == item:
            return "Index: "+str(mid)+". Count of try: "+str(trying)
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return None      

def create_array(n):
   return [i for i in range(1,n+1)]

my_list=create_array(128)  


print(binary_search(my_list, 128))    
    
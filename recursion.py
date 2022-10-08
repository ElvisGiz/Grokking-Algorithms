def recursion(x):
    if x==1:
        return x
    else:
        return x*recursion(x-1)  


print(recursion(3))          

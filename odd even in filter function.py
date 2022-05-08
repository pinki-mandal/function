val=[5,6,7,8,2]
def even_odd(n):
    if n%2==0:
        return True
    else:
        return False
even=filter(even_odd,val) 
for x in even:
    print(x)   
    
    
    
    
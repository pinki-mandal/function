def add(a):   
    sum=0
    i=0
    while i<len(a):
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
        i=i+1
    print(sum)  
add([[1,2,1,2],[1,2,2,2,8,9,3,4,5,7,8]])  


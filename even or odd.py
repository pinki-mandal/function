def evenodd(a):
    i=0
    even=0
    odd=0
    while i<len(a):
        if a[i]%2==0:
            print(a[i],"even number")
        else:
            print(a[i],"odd number")  
        i=i+1
evenodd([2,3,4,5,6])       
          
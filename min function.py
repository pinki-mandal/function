def min(a):
    i=0
    min=a[i]
    while i<len(a):
        if min>a[i]:
            min=a[i]
        i=i+1
    print(min) 
min([8, 6, 4, 8, 4, 50, 2, 7])           
    
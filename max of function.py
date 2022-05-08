def max(a):
    i=0
    max=0
    while i<len(a):
        if max<a[i]:
            max=a[i]
        i=i+1
    print(max) 
max([3, 5, 7, 34, 2, 89, 2, 5])       
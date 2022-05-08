a=[9,[3,4,5,6],7,8]
i=0
max=0
while i<len(a):
    if max<a[i]:
        max=a[i]
    i=i+1
print(max)    
        
        
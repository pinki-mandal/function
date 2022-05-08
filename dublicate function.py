# def duplicates(a):
#     i=0
#     b=[]
#     while i<len(a):
#         if a not in b:
#             b.append(a)
#         i=i+1
#     print(b)    
        
# duplicates([1, 2, 3, 1, 2, 4, 5, 4 ,6, 2])

a=[4,5,6,7,4,5,8,9]
i=0
b=[]
while i<len(a):
    if a not in b:
        b.append(a)
    i=i+1
print(a)        
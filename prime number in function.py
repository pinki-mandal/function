# def prime():
#     num=int(input("enter the number:"))
#     i=1
#     count=0
#     while i <=(num):
#         if num%i==0:
#             count+=1
#         i+=1
#     if count==2:
#         print("prime number")
#     else:
#         print("not prime number")  
# prime()    
    
# start=int(input("enter the number"))
# end=int(input("enter the number"))
# for i in range(start,end+1):
#     flag=0
#     for j in range(2,i):
#         if i%j==0:
#             flag=1
#             break
#     if flag==0:  
#         print(i,end=" ")      
        
        
# i=2
# while i<=10+1:
#     flag=0
#     j=0
#     while j<(2,i):
#         if i%j==0:
#             flag=1
#             j+=1
#             break
#     if flag==0:  
#         print(i,end=" ") 
#         i+=1 
        
        
        
# a=["pinki","neha"] 
# i=1
# b=[]
# count=0
# while i<len(a): 
#     j=0
#     while j<len(a[i]):
#         b.append(count)
#         count+=1
#         j+=1
#     i+=1
# print(b)          

a=["pinki"]
i=0
count=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        count+=1
        b.append(count)
        j+=1
        i+=1
print(b)    
    
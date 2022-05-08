# a=[1,2,3,4,5,6,7]
# i=0
# while i<len(a)-1:
#     diff=a[i+1]-a[i]
#     if diff==1:
#         print("true")
#     i=i+1    

def fac():
    num=int(input("enter the number"))
    fac=1
    i=0
    if num>0:
        fac=fac*num
        i=i-1
    print(fac)    
fac()        
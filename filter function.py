# a=[10,50,80]
# def high_marks(n):
#     if n>=8:
#         return True
#     else:
#         return False
# marks=list(filter(high_marks,a))  
# for n in marks:
#     print(n)
    
    
ages=[5,12,17,24,32]
def my_function(x):
    if x<18:
        return True
    else:
        return False
adults=list(filter(my_function,ages))   
for x in adults:
    print(x) 
    
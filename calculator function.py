def calculator():
    x=int(input("enter the number:"))
    y=int(input("enter the number:"))
    operator=input("select operator:")
    if operator=="+":
        sum = x + y
        print(sum)
    elif operator == "-":
        print(x-y)
    elif operator =="*":
        print(x*y)
    elif operator =="%" :
        print(x%y)
    elif operator =="/":
        print(x/y)  
    else:
        print("nothing")  
calculator()        
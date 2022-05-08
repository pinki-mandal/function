num=int(input("enter the number"))
def eliglble():
    if num<18:
        print("not eligible")    
    elif num>18 or num==18:
        print("eligle")  
    else:
        print("nothing")
eliglble()              
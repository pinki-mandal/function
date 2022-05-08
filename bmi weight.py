def bmi():
    weight=int(input("enter the weight"))
    height=int(input("enter the height"))
    bmi=weight/height
    if bmi<=18.5:
        print("under weight")
    elif bmi<=25.0:
        print("normal")    
    elif bmi<=30.0:
        print("over weight")    
    elif bmi>30:
        print("obese")   
bmi()         
    
    


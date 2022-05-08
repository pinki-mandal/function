# children=int(input("enter the number"))
# Kids drink toddy.
#     Teens drink coke.
#     Young adults drink beer.
#     Adults drink whisky.
# def greet(*names):
#     for name in names:
#         print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")
# def icecream(*flavours):
#     for flavour in flavours:
#         print("i love"+ flavour)
# icecream(" chocolate ", " butterscotch "," vanilla "," strawberry ")
# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky".

def age():
    age=int(input("enter the number"))
    if age<=14:
        print("drink toddy")
    elif age<=18:
        print("drink coke")
    elif age<21:
        print("drink beer")  
    elif age>=21:
        print("drink whisky")            
    else:
        print("nothing")  
age()




# def my_fun():
#     print("hello")
#     my_fun()
# my_fun()    



# i=0
# def my_fun():
#     global i
#     i=i+1
#     print("hello",i)
#     my_fun()
# my_fun()    
    
# a=[1,5,0,6,7,0,2,3,0,10,0,6,0,0,8,0]  
# i=0
# count=0
# while i<len(a):
#     if a[i]==0:
#         count+=1
#         pass
#     i+=1


# k=0
# m=[]
# while k<len(a):
#     if a[k]!=0:
#         m.append(a[k])
#     k+=1
# j=1
# while j<=count:
#     m.append(0)
#     j+=1
# print(m)
    
# def my_function(**kid):
#       print(  kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes") 
      
# def myFun(*argv):
#     for arg in argv:
#         print(arg)
 
 
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')          


# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))
 
 
# # Driver code
# myFun(first='Geeks', mid='for', last='Geeks')
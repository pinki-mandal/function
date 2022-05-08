# def reverse_function(a):
#     i=len(a)-1
#     while i>=0: 
#         print(a[i])
#         i=i-1
# reverse_function(["Z", "A", "A", "B", "E", "M", "A", "R", "D"])  
import json
import requests
get_url=requests.get('https://api.merakilearn.org/courses')
meraki_learn=get_url.json()
with open("pinki.json","w")as file_data:
    file=json.dump(meraki_learn,file_data,indent=4)
serial_number=1
for i in meraki_learn:
    print(serial_number,".",i["name"],":",i["id"])
    serial_number=serial_number+1
corse_number=int(input("enter the number: "))
print(meraki_learn[corse_number-1]["name"]) 
idd=meraki_learn[corse_number-1]["id"]
get_url1=requests.get("https://api.merakilearn.org/courses/"+str(idd)+"/exercise")
meraki_learn1=get_url1.json()
with open("text.json","w")as file_data1:
    var=json.dump(meraki_learn1,file_data1,indent=4)
print(var)
    
    

    


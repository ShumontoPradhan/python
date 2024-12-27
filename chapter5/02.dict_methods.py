name = {}  #empty dictionary

marks = {    #non empty dictionary
    "harry" : 100,
    "shum" : 99,
    "list" : [1,4,7],
    "name" : "shubham",
     0 : "harry"
}

print(marks.items())  #print everything above
print(marks.keys())  #print only keys
print(marks.values())  #print only values
marks.update({"harry": 88 , "renuka": 83})  #if doesnt exist then add to dict , if exist then update the value
print(marks)

print(marks.get("harry"))  #print value of harry if exist, else returns none
print(marks["harry"])  #print value of harry if exist, else returns error if harry not exist


print(marks.pop("harry"))
print(len(marks))  #lenght print karega
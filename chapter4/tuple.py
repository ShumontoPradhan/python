a = (1, 45 , 4343, False ,45,  "shum" , "rahul")
#tuple is also immutable like strings
print(a)
print(type(a))


#tuple functions

n = a.count(45)   #returns how many times the element is there in the tuple
print(n)

i = a.index(4343)   #returns the index of the element specified
print(i)

print(len(a))

s = set()

s.add(20)
s.add(20.0)   #since 20 == 20.0 , so this value will not be printed when we print the set
s.add("20")

print(s)
print(len(s))
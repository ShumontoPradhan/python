#write a program to input eight numbers from the user and display all the unique numbbers once

s = set()

n = input("enter number: ")
s.add(int(n))
n = input("enter number: ")
s.add(int(n))
n = input("enter number: ")
s.add(int(n))
n = input("enter number: ")
s.add(int(n))
n = input("enter number: ")
s.add(int(n))
n = input("enter number: ")
s.add(int(n))
n = input("enter number: ")
s.add(int(n))
n = input("enter number: ")
s.add(int(n))
n = input("enter number: ")
s.add(int(n))

print(s)  #even if you enter two numbers again it will only print one of them
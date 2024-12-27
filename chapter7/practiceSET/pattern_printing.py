'''
print the following pattern
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

for i in range(1, 6):
    for j in range(1,6):
        print("*  ", end="")  #end=""  is used to stay in the same line and not jump to the next line
    print()    


'''print the pattern
*
* *
* * *
* * * *
'''

for i in range(1,5):
    for j in range(1,5):
        print("* ", end=" ")
    print()

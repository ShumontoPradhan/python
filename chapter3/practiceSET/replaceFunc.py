letter = '''dear <name> 
you are selected
            <date>'''
print(letter.replace("<name>", "rahul"))

#chaining of .replace() function
print(letter.replace("<name>", "shum").replace("<date>", "13 december 2024"))

print(letter)  #strings are immutable , it will still print the statement which is inside the letter which was created at the beginning of the program even after we use replace() function

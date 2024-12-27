s1 = {1, 45, 6}
s2 = {7, 8, 1 ,78}

print(s1.union(s2))    #prints all unique no's
print(s1.intersection(s2))  #prints common values 




set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Popular set methods 
set1.add(7); print("add:", set1)                    # Add an element
set1.remove(7); print("remove:", set1)              # Remove an element (error if not found)
print("union:", set1.union(set2))                   # Combine all unique elements
print("intersection:", set1.intersection(set2))     # Common elements between sets
print("difference:", set1.difference(set2))         # Elements in set1 but not in set2
print("symmetric_difference:", set1.symmetric_difference(set2))  # Elements not in both
print("issubset:", {1, 2}.issubset(set1))           # Check if subset
print("issuperset:", set1.issuperset({1, 2}))       # Check if superset

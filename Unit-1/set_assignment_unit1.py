# Create sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Access elements (using loop)
for i in set1:
    print(i)

# Union
print(set1 | set2)

# Intersection
print(set1 & set2)

# Difference
print(set1 - set2)




#my practice
print(set2.union(set1))
print(set2.difference(set1))
print(set2.intersection(set1))

set1.add(7)
set1.update({8,9})
for i in set1:
    print(i)


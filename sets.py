s = {1, 2 , 3}

e = set() # this is empty set dont dp s={} this is used for dict not sets 
print(s, type(s))

s.add(33)
print(s)

'''
# Creating sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7}

print("Original Set A:", set_a)
print("Original Set B:", set_b)

# 1. add() - Add a single element
set_a.add(10)
print("\nAfter set_a.add(10):", set_a)

# 2. remove() - Remove an element (error if not present)
set_a.remove(1)
print("After set_a.remove(1):", set_a)

# 3. discard() - Remove an element (no error if not present)
set_a.discard(20)
print("After set_a.discard(20):", set_a)

# 4. pop() - Removes and returns a random element
removed_item = set_a.pop()
print("Removed item using pop():", removed_item)
print("After pop():", set_a)

# 5. clear() - Remove all elements from set_b
set_b.clear()
print("After set_b.clear():", set_b)

# Reset sets for more operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7}

# 6. update() - Add multiple elements from another iterable
set_a.update([8, 9])
print("\nAfter set_a.update([8, 9]):", set_a)

# 7. union() - All unique elements from both sets
union_set = set_a.union(set_b)
print("set_a.union(set_b):", union_set)

# 8. intersection() - Common elements
intersection_set = set_a.intersection(set_b)
print("set_a.intersection(set_b):", intersection_set)

# 9. difference() - Elements in set_a but not in set_b
difference_set = set_a.difference(set_b)
print("set_a.difference(set_b):", difference_set)

# 10. symmetric_difference() - Elements in either set but not both
sym_diff_set = set_a.symmetric_difference(set_b)
print("set_a.symmetric_difference(set_b):", sym_diff_set)

# 11. issubset() - Check if all elements of set1 are in set2
print("\n{1, 2}.issubset(set_a):", {1, 2}.issubset(set_a))

# 12. issuperset() - Check if set contains all elements of another set
print("set_a.issuperset({1, 2}):", set_a.issuperset({1, 2}))

# 13. isdisjoint() - True if no common elements
print("set_a.isdisjoint({100, 200}):", set_a.isdisjoint({100, 200}))



*** via using chatgpt to see later all methods 
'''
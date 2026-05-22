# Sets Basic
''' Sets: Sets are built-in data structures in Python that do not allow duplicate values.
 Sets are mutable and unordered, which means that their elements are not stored in any
 specific order, so you cannot use indices or keys to access them. Also, sets can 
 only contain values of immutable data types, like numbers, strings, and tuples.'''

set1 = {1,2,3,4,5,6,7,8,9}
set2 = {2,3,4,5,6,7,8}
set3 = {'Amin', 'Akash', 'Tamim'}
set4 = {'Akash', 'Bappi'}

# Defining a set
set() # it autometicly create a dictionary

#-------------------- Common Set Methods ------------------------------#
# 1. add() ----> add element if it not their, if adding element is already in set than no change
set1.add(10)
set1.add(2)
print(set1)

# 2. remove() ----> It remove defind value from set
# set1 = {1,2,3,4,5,6,7,8,9}
set1.remove(3)
print(set1)

# 3. discard() ----> work same as remove()
''' remove() method will raise a KeyError if the element is not found
 while the discard() method will not.'''
set1.discard(4)
print(set1)

# 4. clear() ----> remove all element from set
print("printing set3",set3)
set3.clear()
print("printing set3 after clear(): ",set3)

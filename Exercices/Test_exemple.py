def foo(x, a):
   """
   x: a positive integer argument
   a: a positive integer argument

   returns an integer
   """
   count = 0
   while x >= a:
      count += 1
      x = x - a
   return count

'''
Test Suite : foo(10, 3), foo(1, 4), foo(10, 6)

Explanation:

In glass box testing, we try to sample as many paths through the code as we can. 
In the case of loops, we want to sample three general cases:

Not executing the loop at all.
Executing the loop exactly once.
Executing the loop multiple times.
Test Suite B has cases that explores all three loop cases.

Test Suite A only explores paths that execute the loop 0 or 1 times.

Test Suite C only explores paths that execute the loop more than 1 time.
'''
    


"""
def union(set1, set2):
set1 and set2 are collections of objects, each of which might be empty.
Each set has no duplicates within itself, but there may be objects that
are in both sets. Objects are assumed to be of the same type.

This function returns one set containing all elements from
both input sets, but with no duplicates.

Test 1 - set1 is an empty set; set2 is an empty set
Test 2 - set1 is an empty set; set2 is of size greater than or equal to 1
Test 3 - set1 is of size greater than or equal to 1; set2 is an empty set
Test 4 - set1 and set2 are both nonempty sets which do not contain any objects in common
Test 5 - set1 and set2 are both nonempty sets which contain objects in common
   
Explanation:

A good black box test suite would contain tests for all of the given conditions! 
Black-box testing tests the functionality of an application, by looking at the 
paths through its specifications.
According to the specifications, the possibilities for set1 and set2 are as follows: 
both sets are empty; one of the sets is empty and one has at least one object; 
both sets are not empty. The tests list all the combinations of those possibilities 
for set1 and set2.
"""
   

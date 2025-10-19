def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
   if len(set1) == 0:
      return set2
   elif set1[0] in set2:
      return union(set1[1:], set2)
   else:
      return set1[0] + union(set1[1:], set2)
      
'''
Test Suite: union('','abc'), union('a','abc'), union('ab','abc'), union('d','abc')
Explanation:

A good glass box test suite would try to test a good sample of all the possible 
paths through the code. So, it should contain tests that test when set1 is empty, 
when set1[0] is in set2, and when set1[0] is not in set2. The test suite should also 
test when the recursion depth is 0, 1, and greater than 1.

Remember that glass box testing is a method of software testing that tests the internal 
structures and workings of a piece of code. When we look at the code for union, we see a 
set of conditionals that ask about set1. Thus a good glass box test suite will contain 
tests that match the following lines from the conditional statements in the code:

len(set1) == 0 - matched by the test union('', 'abc')
set1[0] in set2 - matched by the test union('a', 'abc')
set1[0] not in set2 (this is the else: of the conditional) - matched by the test union('d', 'abc')
In addition, because union is a recursive function, we should make sure our test set considers 
a recursion depth of 0, 1, and many. In this case, recursion depth is covered by some of the 
tests we've already chosen:

Recursion depth = 0 - matched by the test union('', 'abc')
Recursion depth = 1 - matched by the tests union('a', 'abc'), union('d', 'abc')
Recursion depth > 1 - matched by the test union('ab', 'abc')
Note that this test suite is NOT path complete because it would take essentially infinite 
time to test all possible recursive depths.

'''
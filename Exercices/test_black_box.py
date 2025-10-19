def maxOfThree(a,b,c) :
    """
    a, b, and c are numbers

    returns: the maximum of a, b, and c        
    """
    if a > b:
        bigger = a

    else:
        bigger = b

    if c > bigger:
        bigger = c

    return bigger

'''
Test Suite: maxOfThree(2, -10, 100), maxOfThree(7, 9, 10), maxOfThree(6, 1, 5), maxOfThree(0, 40, 20)
Explanation:

Recall from the lecture that a path-complete glass box test suite would find test cases that 
go through every possible path in the code. In this case, that means finding all possibilities 
for the conditional tests a > b and c > bigger. So, we end up with four possible paths that 
correspond to Test Suite A:

Case 1: a > b and c > bigger - this corresponds to test maxOfThree(2, -10, 100).
Case 2: a > b and c <= bigger - this corresponds to test maxOfThree(6, 1, 5)
Case 3: a <= b and c > bigger - this corresponds to test maxOfThree(7, 9, 10).
Case 4: a <= b and c <= bigger - this corresponds to test maxOfThree(0, 40, 20)
'''
'''
Problem 4
15/15 points (graded)
Write a Python function that returns the sublist of strings in aList that contain 
fewer than 4 characters. For example, if aList = ["apple", "cat", "dog", "banana"], 
your function should return: ["cat", "dog"]

This function takes in a list of strings and returns a list of strings. 
Your function should not modify aList.
'''

def lessThan4(aList):
       
    # Your code here
    newList = []
    for item in aList:
        if len(item) < 4:
            newList.append(item)
            # Debug string, comment out before submitting
            # print(newList)
    return newList

# Calling lessThan4. Comment out before submitting
aList = ["apple", "cat", "dog", "banana"]
result = lessThan4(aList)
print(result)
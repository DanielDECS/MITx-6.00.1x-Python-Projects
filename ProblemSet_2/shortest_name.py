'''
The shortest name function receives a list of strings with the name
of people as a parameter and returns the shortest name in the list. 
The function ignores spaces before and after the name and returns 
the smallest name in the list with the first capital letter and 
its other lower characters, regardless of how it was presented 
in the list passed to the function.
'''

def shortest_name(names):
    
    value = int(len(names[0]))
    result = ""
    
    for item in range(len(names)):
        current_item = int(len(names[item].strip()))
        
        if value > current_item:
            result = names[item]
            value = current_item
        
        if result == "":
            result = names[0]
    
    return result.strip().capitalize()

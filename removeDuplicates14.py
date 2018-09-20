"""Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.

For example: remove_duplicates([1, 1, 2, 2]) should return [1, 2].

Don't remove every occurrence, since you need to keep a single occurrence of a number.
The order in which you present your output does not matter. So returning [1, 2, 3] is the same as returning [3, 1, 2].
Do not modify the list you take as input! Instead, return a new list."""



def remove_duplicates(inputlist):
    if inputlist == []:
        return []
    
# Sort the input list from low to high    
    inputlist = sorted(inputlist)
# Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

# Go through the values of the sorted list and append to the output list
# ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
        
    return outputlist
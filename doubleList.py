"""Create a function named double_index that has two parameters named lst and index.

The function should double the value of the element at index of lst and return the new list with the doubled value.

If index is not a valid index, the function should return the original list.

After writing your function, un-comment the call to the function that we've provided for you to test your results."""

#Write your function here
def double_index(lst, index):
  if index < len(lst):
    lst[index] = lst[index] * 2
    return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
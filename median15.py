"""median
Great work! You've covered a lot in these exercises. Last but not least, let's write a function to find the median of a list.

The median is the middle number in a sorted sequence of numbers.

Finding the median of [7, 12, 3, 1, 6] would first consist of sorting the sequence into [1, 3, 6, 7, 12] and then locating the middle value, which would be 6.

If you are given a sequence with an even number of elements, you must average the two elements surrounding the middle.

For example, the median of the sequence [7, 3, 1, 4] is 3.5, since the middle elements after sorting the list are 3 and 4 and (3 + 4) / (2.0) is 3.5.

You can sort the sequence using the sorted() function, like so:

sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
1.
Write a function called median that takes a list as an input and returns the median value of the list. For example: median([1, 1, 2]) should return 1.

The list can be of any size and the numbers are not guaranteed to be in any particular order. Make sure to sort it!
If the list contains an even number of elements, your function should return the average of the middle two."""


def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
   
print median([2, 4, 5, 9])
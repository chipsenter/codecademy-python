"""Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result. For example, purify([1,2,3]) should return [2].

Do not directly modify the list you are given as input; instead, return a new list with only the even numbers."""


def purify(lst):
    res = []
    for ele in lst:
        if ele % 2 == 0:
            res.append(ele)
    return res
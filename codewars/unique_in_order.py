'''
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without 
any elements with the same value next to each other and preserving the original order of elements.
'''

def unique_in_order(iterable):
    list = []
    for i in iterable:
        if len(list) < 1 or not i == list[len(list) - 1]:
            list.append(i)
    return list
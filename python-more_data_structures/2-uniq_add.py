#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    for item in my_list:
        if item not in unique:
            unique.append(item)
    return sum(unique)

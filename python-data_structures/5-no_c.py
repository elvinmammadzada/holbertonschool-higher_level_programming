#!/usr/bin/python3

def no_c(my_string):
 my_string = list(my_string)
 a=my_string
 for i in range (len(a)):
    if a[i]=="c" or a[i]=="C" :
      del my_string[i]
 return my_string

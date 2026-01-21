#############################
#   Python Demo             #
#                           #
#############################

# practise iter, map, filter and reduce
import random

def model_fun(n):
    return n**n


x= [1,2,3,4]
s= iter(x)
print(next(s))
print(next(s))
yield next(s)


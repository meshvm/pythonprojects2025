
# map filter reduce
def sqr(n):
    return n*n


lst = [1,2,3,4,5]
res = map(sqr,lst)
print(list(res))


def is_even(n):
    return n % 2 ==0


lys= [1,2,3,4,5,6]
resp = filter(is_even,lys)
print(list(resp))


# [1, 4, 9, 16, 25]
# [2, 4, 6]

#higher order and decorators

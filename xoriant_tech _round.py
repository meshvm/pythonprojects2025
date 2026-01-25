

def test(*args, **kwargs):
    print(type(args), type(kwargs))


test()

test(1)

test(1,x=2)

test(x=2)

test(1,3,x=2)

# <class 'tuple'> <class 'dict'>
# <class 'tuple'> <class 'dict'>
# <class 'tuple'> <class 'dict'>
# <class 'tuple'> <class 'dict'>
# <class 'tuple'> <class 'dict'>


# how to find a number is even with Modulus operation( %, /  or // )

def check_even(n):
    check = n & 1
    if check:
        return "ODD"
    else:
        return "EVEN"


print(check_even(n=345670))
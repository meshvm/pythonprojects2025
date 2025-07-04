
import sys

'''
    Given an array of integer nums and an integer target, return
    indices of the two numbers such that they add up to the target.
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
    You can return the answer in any order.
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

def algo(array, target):

    b = array
    c = [elements for elements in b if elements <= target]
    for items in c:
        for ele in range(len(c)):
            if items != (c[ele]):
                if items + c[ele] == target:
                    return ele, c.index(items)

start= int(input("To Start enter    1 "))

while start > 0:
    target = int(input())
    if target == 0:
        sys.exit()
    ans = algo([2, 7, 11, 15, 22, 19, 27, 34, 65, 89, 67], target= target)
    print(ans)
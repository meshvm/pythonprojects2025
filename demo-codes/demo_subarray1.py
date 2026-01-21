

'''
    5. Maximum Subarray
    Given an integer array nums, find the subarray with the largest
    sum, and return its sum.
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum of 1.

'''

# def subarray(array):
#     sub_arr = []
#     super_arr =[]
#     for x in range(len(array)):
#         sub_arr = []
#         for y in range(x + 1):
#             sub_arr.append(array[y])
#             if sub_arr not in super_arr:
#                 super_arr.append(sub_arr)
#     print(super_arr)
#     return 0
#     # max_count = {}
#     # for items in super_arr:
#     #     count = 0
#     #     for index in range(len(items)):
#     #       count += items[index]
#     #     print(items, count)
#     # return max_count
#

# ans = subarray([-2,1,-3,4,-1,2,1,-5,4])
# print(ans)

# a =[1,2,3]
# b =[1,2,3]
# if a is b:
#     print(" a is b")
# if a == b:
#     print("a == b")

'''
For an array of size n containing integers, need to return the length of the longest subarray having sum equal to the given value k. If there is no subarray with sum equal to k, return 0.
Examples:
Input:  [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.
'''


def sub_arr_fun():
    input = [10, 5, 2, 7, 1, -10,9,10]
    k = 24
    new_srr = []
    total = 0
    if sum(input) == k:
        return len(input)
    else:
        for i in range(0, len(input)):
            sub_arr = []
            for j in range(i):
                sub_arr.append(input[j])
            new_srr.append(sub_arr)
        # print(new_srr)

        for items in new_srr:
            if sum(items) == k:
                print(items)
                return len(items)
    return 0


ans = sub_arr_fun()
print(ans)
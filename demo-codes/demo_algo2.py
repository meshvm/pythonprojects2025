

'''

2. Best Time to Buy and Sell Stock
You are given an array of prices where prices[i] is the price of a
given stock on an ith day.
You want to maximize your profit by choosing a single day to buy
one stock and choosing a different day in the future to sell that
stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
profit = 6-1 = 5.

'''

def profit(array):
    b = array
    min_b  = min(b)
    index_b = b.index(min_b)
    remain_array = [b[days] for days in range(index_b,len(b)) if b[days] == max(b[index_b:len(b) -1])]
    print(" Buy Day: ", index_b ,  "Selling Day :", b.index(remain_array[0]))
    return remain_array[0] - min(b)

ans = profit([7,1,5,3,6,4])
print(ans)
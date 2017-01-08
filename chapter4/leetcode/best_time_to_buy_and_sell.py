# -*- coding:utf8 -*-

# 121. Best Time to Buy and Sell Stock
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.

def max_profit1(prices):
    length = len(prices)
    array = [prices[i+1] - prices[i] for i in xrange(0, length-1)]
    sum, max_sum = 0, 0
    length = len(array)
    for i in xrange(length):
        if sum < 0:
            sum = array[i]
        else:
            sum += array[i]
        if sum > max_sum:
            max_sum = sum
    return max_sum

# prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
# print max_profit1(prices)

# 122. Best Time to Buy and Sell Stock II
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

def max_subarray(nums, sta, end):
    print sta, end, nums
    buy, sell, sum, max_sum = sta, sta, 0, 0
    for i in xrange(sta, end):
        if sum < 0:
            buy, sell, sum = i, i+1, nums[i]
        else:
            sum += nums[i]
        if sum > max_sum:
            sell, max_sum = i+1, sum
            print buy, sell, max_sum
            right_max_sum = max_subarray(nums, i+1, end)
            return max_sum+right_max_sum
    return max_sum

def max_profit2(prices):
    length = len(prices)
    array = [prices[i + 1] - prices[i] for i in xrange(0, length - 1)]
    return max_subarray(array, 0, len(array))


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    length = len(prices)
    array = [prices[i + 1] - prices[i] for i in xrange(0, length - 1)]
    return sum([e for e in array if e > 0])

# prices = [7, 1, 5, 3, 6, 4]
# prices = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# print max_profit2(prices)
# print maxProfit(prices)

# 123. Best Time to Buy and Sell Stock III
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


def max_profit3(array, k):
    length = len(array)
    states = [[0 for i in xrange(k*2)] for j in xrange(2)]
    cur, next = 0, 1
    for i in xrange(length):
        for j in xrange(k):
            if j<1:
                earn = 0
            else:
                earn = states[cur][2*j-2]
            states[next][2*j] = max(states[cur][2*j], earn-array[i])
            states[next][2*j+1] = max(states[cur][2*j+1], states[cur][2*j] + array[i])
        tmp = cur
        cur = next
        next = tmp
    return states[cur][3]


prices = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print max_profit3(prices, 2)
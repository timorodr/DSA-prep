# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # initialize our pointers values
        maxP = 0 # keep track of our max profits

        while r < len(prices): # initialize R pointer to run length of loop
            if prices[l] < prices[r]: # have to check if our prices that we are selling at is greater than the price we are buying at
                profit = prices[r] - prices[l] # calc the difference of Right pointer SELL and left pointer BUY
                maxP = max(maxP, profit) # get the max of what our max Profit is so far and profit for that iteration of loop
            else:
                l = r # if prices[l] is greater than r then we have to set the L pointer to the R position 
            r += 1 # and update the posistion of R as well to the next value
        return maxP # return our maximum profit
    
##** There is another solution that is more straight forward than this
#* more pracitce on two pointers
    
class Solution2:
    def maxProfit2(self, prices2: List[int]) -> int:
        
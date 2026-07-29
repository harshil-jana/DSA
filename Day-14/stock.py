# Best Time to Buy and Sell Stock

# Method - 1 (Brute Force)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(0,n):
            for j in range(i+1,n):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit

sol = Solution()
prices = [7,6,4,3,1]
print(sol.maxProfit(prices))


# --------------------------------

# Method - 2 (Own Solution)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        profit = 0
        max_profit = 0
        min_index = prices.index(min(prices))
        
        for i in range(0,n):
            for j in range(i+1,n):
                if prices[j] < prices[i]:
                    break
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
            if i == min_index:
                break
        return max_profit
        
sol = Solution()
prices = [8,5,3,2,1]
print(sol.maxProfit(prices))


# -------------------------------

# Method - 3 (Optimal Solution)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = float("inf")

        for i in range(0,n):
            min_price = min(min_price,prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
        
sol = Solution()
prices = [8,5,3,2,1]
print(sol.maxProfit(prices))
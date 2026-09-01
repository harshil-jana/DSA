class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        l = 0
        window, max_window = 0, 0
        satisfied = 0

        for r in range(0,len(customers)):
            if grumpy[r]:
                window += customers[r]
            else:
                satisfied += customers[r]

            if r - l + 1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l += 1
            max_window = max(max_window, window)

        return satisfied + max_window

sol = Solution()
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
print(sol.maxSatisfied(customers, grumpy, minutes))
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        digit_sum = 0
        digit_product = 1

        while temp != 0:
            digit = temp % 10
            digit_sum += digit
            digit_product *= digit
            temp //= 10

        main_sum = digit_sum + digit_product

        if n % main_sum == 0:
            return True
        else:
            return False

sol = Solution()
n = 99
print(sol.checkDivisibility(n))
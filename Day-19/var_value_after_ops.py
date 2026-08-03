class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        n = len(operations)
        sum1 = 0
        for i in range(0,n):
            if operations[i] == "X++":
                sum1 += 1
            elif operations[i] == "++X":
                sum1 += 1
            elif operations[i] == "X--":
                sum1 -= 1
            elif operations[i] == "--X":
                sum1 -= 1
        return sum1

sol = Solution()
operations = ["--X","X++","X++"]
print(sol.finalValueAfterOperations(operations))

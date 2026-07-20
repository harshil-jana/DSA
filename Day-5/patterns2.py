# Pattern 14: Increasing Letter Triangle

# class Solution:
    
#   def pattern14(self, n):
#       arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#       for i in range(1,n+1):
#           print("".join(arr[0:i]))

# sol = Solution()
# result = sol.pattern14(5)

# ------------------------

# Pattern 15: Reverse Letter Triangle

# class Solution:
#     def pattern15(self, n):
#         for i in range(0,n+1):
#             for j in range(0,n-i):
#                 print(chr(65+j), end="")
#             print("")

# sol = Solution()
# result = sol.pattern15(4)


# ------------------------

# Pattern - 16: Alpha-Ramp Pattern

# class Solution:
#     def pattern16(self, n):
#         for i in range(0,n):
#             for j in range(0,i+1):
#                 print(chr(65+i), end="")
#             print("")

# sol = Solution()
# result = sol.pattern16(4)


# ------------------------

# Pattern - 17: Alpha-Hill Pattern

class Solution:
    def pattern17(self, n):
            for i in range(0,n):
                print(" " * (n-i-1), end="")

                ch = ord("A")
                breakpoint = (2*i+1)//2

                for j in range(1, 2*i+2):
                    print(chr(ch), end="")
                    if j <= breakpoint:
                            ch += 1
                    else:
                            ch -= 1
                print("")

sol = Solution()
result = sol.pattern17(4)